#!/usr/bin/env bash
# Data inputs / outputs / paths / version statements across Stata files. Usage: grep_io.sh <source_root>
R="$1"
cd "$R" || exit 1
FILES=$(find . -name '*.do' -o -name '*.ado' | sort)
echo "### VERSION statements"
grep -nE '^\s*version\s+[0-9]' $FILES
echo; echo "### INPUTS: use / import / insheet / infile / merge using / append using / fileread / copy"
grep -nE '^\s*(noisily |quietly |qui |capture |cap |noi )*(use |import (excel|delimited|sas|spss|haver|fred)|insheet|infile|infix|merge .*using|append using|joinby|copy |fileread|unzipfile|jsonio|insheetjson)' $FILES
echo; echo "### OUTPUTS: save / export / putexcel / outsheet / graph export / file open-write / log using"
grep -nE '^\s*(noisily |quietly |qui |capture |cap |noi )*(save |saveold|export (excel|delimited)|putexcel|outsheet|graph export|file open|file write|log using|cmdlog|texdoc|estout|esttab|outreg)' $FILES
echo; echo "### PATHS: cd / absolute paths / SIMROOT definitions"
grep -nE '^\s*(cd |sysdir set|global SIMROOT|adopath)|/Users/|/SIM/|C:\\\\|Dropbox' $FILES
echo; echo "### SHELL escapes"
grep -nE '^\s*(!|shell |winexec|python:|python script|mata:|mata$)' $FILES
echo; echo "### NET / SSC"
grep -nE 'ssc install|net install|net from|copy *"?http|curl|wget' $FILES
