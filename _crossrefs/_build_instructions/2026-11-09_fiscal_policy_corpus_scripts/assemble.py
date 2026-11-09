import re
S="/tmp/claude-1000/-home-hectorjuan/67f74bf9-d8cf-429f-9df8-c3e47d4d699b/scratchpad"
body=open(f"{S}/merged_body.md").read()
body=body.replace("#### Box 4.18 Fiscal Rules and Institutions in the United Kingdom",
 "#### Box 4.18 Fiscal Rules and Institutions in the United Kingdom\n\n*[Editorial note: printed as \"Box 4.18\" on p. 213 although the text on p. 212 refers to it as box 4.17; the euro-area box on p. 219 is also printed as 4.18. Kept as printed.]*")
f="benassy-quere_2019_ch4_fiscal_policy.md"; e=open(f).read()
head, sep, _ = e.partition("## Transcription\n")
src_note = "*Source: Bénassy-Quéré, Cœuré, Jacquet & Pisani-Ferry (2019), Economic Policy: Theory and Practice, 2nd ed., Oxford University Press, Chapter 4, pp. 148–236. Personal study copy transcribed from Héctor's own book. Not for redistribution.*"
open(f,"w").write(head + "## Transcription\n\n" + src_note + "\n\n---\n\n" + body)
print("assembled; words:", len(open(f).read().split()))
