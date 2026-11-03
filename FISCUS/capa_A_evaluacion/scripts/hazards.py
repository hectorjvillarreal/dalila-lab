#!/usr/bin/env python3
"""Count Stata constructs relevant to a Python port. Usage: hazards.py <source_root> <out_csv>
Counts are over code lines (block/line comments stripped) of .do/.ado files; each pattern reports
total occurrences, number of files, and up to 3 example locations."""
import os, re, sys, csv
from collections import defaultdict
root, out = sys.argv[1], sys.argv[2]
PAT = {
 # data manipulation
 'gen/generate/g (new var)':          r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*(?:g|gen|generate)\s+(?:(?:byte|int|long|float|double|str\d*)\s+)?\w',
 'replace':                           r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*replace\s+',
 'egen (any)':                        r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*egen\s+',
 'egen rowtotal/rsum':                r'\begen\b.*=\s*(?:rowtotal|rsum)\(',
 'egen total/sum':                    r'\begen\b.*=\s*(?:total|sum)\(',
 'egen mean/max/min/count':           r'\begen\b.*=\s*(?:mean|max|min|count)\(',
 'egen group/tag/cut/rank':           r'\begen\b.*=\s*(?:group|tag|cut|rank)\(',
 'collapse':                          r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*collapse\s',
 'collapse (sum)':                    r'\bcollapse\b.*\(sum\)',
 'reshape':                           r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*reshape\s+(?:wide|long)',
 'merge 1:1':                         r'\bmerge\s+1:1\b',
 'merge m:1':                         r'\bmerge\s+m:1\b',
 'merge 1:m':                         r'\bmerge\s+1:m\b',
 'merge m:m':                         r'\bmerge\s+m:m\b',
 'merge with update/replace':         r'\bmerge\b.*\b(?:update|replace)\b',
 'merge with assert(':                r'\bmerge\b.*\bassert\(',
 'merge with keep(':                  r'\bmerge\b.*\bkeep\(',
 'merge nogen (no _merge check)':     r'\bmerge\b.*\bnogen',
 'append using':                      r'\bappend\s+using\b',
 'joinby':                            r'^\s*joinby\b',
 'expand':                            r'^\s*(?:(?:qui(?:etly)?)\s+)?expand\s',
 'fillin':                            r'^\s*fillin\b',
 'xtile / pctile / _pctile':          r'\b(?:xtile|pctile|_pctile)\b',
 'tabstat ... save (r(StatTotal))':   r'\btabstat\b.*\bsave\b',
 'r(StatTotal)/r(Stat#)':             r'r\(Stat(?:Total|\d+)\)',
 'summarize/sum ... r(mean/sum)':     r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*(?:su|sum|summ|summarize)\s',
 'preserve':                          r'^\s*(?:(?:qui(?:etly)?)\s+)?preserve\b',
 'restore':                           r'^\s*(?:(?:qui(?:etly)?)\s+)?restore\b',
 'tempfile':                          r'^\s*tempfile\b',
 'tempvar':                           r'^\s*tempvar\b',
 'tempname':                          r'^\s*tempname\b',
 # sort-dependent
 'sort / gsort / sort stable':        r'^\s*(?:(?:qui(?:etly)?)\s+)?(?:g?sort)\s',
 'sort, stable':                      r'\bsort\b.*\bstable\b',
 'bys/bysort/by ...:':                r'^\s*(?:bys|bysort|by)\s+[^:]+:',
 '_n / _N subscripts [_n-1], [`k\']': r'\[\s*_n\s*[-+]|\[\s*_N\b|\[\s*`[\w=]+\'\s*\]',
 '_N bare':                           r'\b_N\b',
 'L. / F. / D. time-series operators':r'\b[LFD]\d*\.\w',
 'tsset':                             r'^\s*tsset\b',
 'running sum sum() in gen':          r'\b(?:g|gen|generate|replace)\b.*=\s*sum\(',
 'in 1 / in -1 / in `k\' (position)': r'\bin\s+(?:1|-1|`[^\']+\'|\d+)\b',
 'continue, break':                   r'\bcontinue,\s*break',
 # missing values
 'comparison > or >= with var (missing hazard)': r'\bif\b[^=!<]*\b\w+\s*>=?\s*[\w.`]',
 'explicit missing test (== . / != . / < .)':     r'(?:==|!=|<)\s*\.(?!\d)',
 'editmissing / cond( / missing(':    r'\b(?:editmissing|missing)\(',
 'replace x = 0 if x == .':           r'replace\s+\S+\s*=\s*0\s+if\s+\S+\s*==\s*\.',
 # numeric precision
 'gen double':                        r'\b(?:g|gen|generate)\s+double\b',
 'gen without type (float default)':  r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*(?:g|gen|generate)\s+(?!(?:byte|int|long|float|double|str)\b)\w+\s*=',
 'set type double':                   r'set\s+type\s+double',
 'round(':                            r'\bround\(',
 'floor( / int( / ceil(':             r'\b(?:floor|int|ceil)\(',
 'float(':                            r'\bfloat\(',
 'string( conversions of numbers':    r'\bstring\(',
 'real( conversions':                 r'\breal\(',
 'compress':                          r'^\s*compress\b',
 'saveold version(13)':               r'\bsaveold\b',
 # survey design
 '[fw=] frequency weights':           r'\[\s*fw\s*=',
 '[pw=] probability weights':         r'\[\s*pw\s*=',
 '[aw=] analytic weights':            r'\[\s*aw\s*=',
 '[iw=] importance weights':          r'\[\s*iw\s*=',
 '[`weight\'=`exp\'] generic weights':r'\[\s*`weight\'',
 'svyset / svy:':                     r'\bsvy(?:set)?\b',
 'round(factor' :                     r'round\(\s*(?:abs\()?factor',
 # macro programming
 'foreach':                           r'^\s*foreach\b',
 'forvalues':                         r'^\s*forvalues\b',
 'while':                             r'^\s*while\b',
 'levelsof':                          r'\blevelsof\b',
 'extended macro fn (: word/list/variable label/di)': r'local\s+\w+\s*:\s*(?:word|list|variable|value|di|dir|char|colnames|rownames|label|subinstr|sortedby|type|format)',
 'nested macro (``x\'\')':            r'``\w+\'\'',
 'var name built from macro (`k\'PIB etc.)': r'\b\w+`\w+\'\w*|`\w+\'\w+',
 'global $ read':                     r'\$\{?\w+',
 'global define':                     r'^\s*global\s+\w+',
 '`=expr\' inline evaluation':        r'`=',
 'ds / unab':                         r'^\s*(?:ds|unab)\b',
 'macro drop / clear all':            r'\b(?:macro\s+drop|clear\s+all)\b',
 'gettoken / tokenize':               r'\b(?:gettoken|tokenize)\b',
 'strtoname / subinstr accents':      r'\bstrtoname\(|subinstr\([^)]*"[áéíóú]"',
 # programs
 'program define':                    r'^\s*(?:capture\s+)?program\s+(?:define\s+)?\w+',
 'syntax':                            r'^\s*syntax\b',
 'args':                              r'^\s*args\b',
 'return scalar/local/matrix':        r'^\s*return\s+(?:scalar|local|matrix|add)',
 'r() read (r(xxx))':                 r'\br\(\w+\)',
 'e() read':                          r'\be\(\w+\)',
 'capture (error swallowing)':        r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?)\s+)*cap(?:ture)?\s',
 'capture confirm':                   r'\bcapture\s+confirm\b',
 '_rc test':                          r'\b_rc\b',
 'exit <code>':                       r'^\s*exit\s+\d+',
 # estimation
 'regress/reg':                       r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?|xi:)\s+)*(?:reg|regress|areg|xtreg)\b',
 'logit/probit':                      r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?|xi:)\s+)*(?:logit|probit|dprobit|mlogit|oprobit)\b',
 'estimates save/use':               r'\bestimates\s+(?:save|use)\b',
 'predict':                           r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*predict\b',
 'ipolate':                           r'\bipolate\b',
 'nl / ml / optimize':                r'^\s*(?:nl|ml|optimize)\b|\boptimize\(',
 'lpoly (kernel smoothing)':          r'\blpoly\b',
 'ci means':                          r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?)\s+)*ci\b',
 # mata & matrices
 'mata: (inline)':                    r'^\s*mata:',
 'mata block (mata:/end)':            r'^\s*mata:\s*$',
 'mata function def':                 r'^\s*(?:void|real\s+(?:scalar|matrix|colvector|rowvector)|string\s+(?:scalar|matrix|rowvector|colvector))\s+\w+\(',
 'st_data/st_matrix/st_local/st_store': r'\bst_(?:data|matrix|local|store|addvar|addobs|numscalar|global)\(',
 'matrix (Stata matrices)':           r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*matrix\s+\w',
 'mkmat / svmat':                     r'\b(?:mkmat|svmat)\b',
 'panelsum/panelsetup':               r'\bpanel(?:sum|setup)\(',
 # randomness
 'set seed':                          r'\bset\s+seed\b',
 'rseed(':                            r'\brseed\(',
 'runiform / rnormal':                r'\br(?:uniform|normal|beta|gamma)\(',
 'bsample':                           r'\bbsample\b',
 # excel coupling
 'putexcel':                          r'\bputexcel\b',
 'import excel':                      r'\bimport\s+excel\b',
 'export excel':                      r'\bexport\s+excel\b',
 'import delimited':                  r'\bimport\s+delimited\b',
 'export delimited':                  r'\bexport\s+delimited\b',
 'cellrange(':                        r'\bcellrange\(',
 # labels/encoding
 'label define':                      r'^\s*label\s+define\b',
 'label values':                      r'^\s*label\s+values\b',
 'decode / encode':                   r'^\s*(?:(?:qui(?:etly)?)\s+)?(?:decode|encode)\b',
 ': label  (value label read in logic)': r':\s*label\s+',
 'string == "1" style flags':         r'\b\w+\s*==\s*"\d+"',
 'destring / tostring':               r'\b(?:destring|tostring)\b',
 'unicode / charset':                 r'\bunicode\b|set\s+charset',
 'Spanish accents in identifiers/labels': r'[áéíóúñÁÉÍÓÚÑ]',
 '{c o\'} SMCL accent escapes':       r"\{c [a-z][~']\}",
 # i/o & side effects
 'save (file write)':                 r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*save\s',
 'use (file read)':                   r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*use\s',
 'file open/write/read':              r'^\s*(?:(?:qui(?:etly)?|cap(?:ture)?)\s+)*file\s+(?:open|write|read|close)\b',
 'log using/on/off':                  r'\blog\s+(?:using|on|off|close)\b',
 'filefilter':                        r'\bfilefilter\b',
 'graph export / graph save':         r'\bgraph\s+(?:export|save)\b',
 'twoway/graph bar/hbar/combine':     r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*(?:twoway|graph\s+(?:bar|hbar|combine|dot|pie))\b',
 'python: blocks':                    r'^\s*python:',
 'shell / ! escapes':                 r'^\s*(?:!|shell\s|winexec)',
 'display di (output formatting)':    r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*(?:di|dis|display)\b',
 'noisily di ... output.txt keys (NAME: [)': r'di\s+in\s+w\s+"\w+:\s*\[',
 'timer':                             r'^\s*timer\b',
 'net install / ssc install':         r'\b(?:net|ssc)\s+install\b',
 'escalar (custom registry)':         r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*escalar\s+',
 'Distribucion (custom macro-micro imputation)': r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*Distribucion\s+',
 'scalar define':                     r'^\s*(?:(?:qui(?:etly)?|noi(?:sily)?|cap(?:ture)?)\s+)*scalar\s+\w+\s*=',
 'scalar( read':                      r'\bscalar\(',
 'hard-coded 4-digit year literal (20xx) in code': r'(?<![\w.])20[0-4]\d(?![\w.])',
}
files = []
for dp, dn, fn in os.walk(root):
    for f in fn:
        if os.path.splitext(f)[1].lower() in ('.do', '.ado'):
            files.append(os.path.join(dp, f))
res = {k: [0, set(), []] for k in PAT}
cre = {k: re.compile(v) for k, v in PAT.items()}
for p in sorted(files):
    rel = os.path.relpath(p, root)
    txt = open(p, encoding='utf-8', errors='replace').read()
    txt = re.sub(r'/\*.*?\*/', lambda m: '\n'*m.group(0).count('\n'), txt, flags=re.S)
    for i, line in enumerate(txt.splitlines(), 1):
        s = line.strip()
        if not s or s.startswith('*') or s.startswith('//'): continue
        s = re.split(r'\s//\s|\t//', s)[0]
        for k, c in cre.items():
            n = len(c.findall(s))
            if n:
                res[k][0] += n; res[k][1].add(rel)
                if len(res[k][2]) < 3: res[k][2].append(f'{rel}:{i}')
with open(out, 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['construct', 'occurrences', 'n_files', 'examples'])
    for k in PAT:
        n, fs, ex = res[k]
        w.writerow([k, n, len(fs), '; '.join(ex)])
        print(f'{n:6d} {len(fs):3d}  {k}   e.g. {"; ".join(ex[:2])}')
