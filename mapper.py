#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
	line=line.strip()
	words=line.split(",")
	if len(words)>1:
		for word in re.findall(r'[$][A-Z]{1,5}\s*', words[3].upper()):
			print('%s\t%s' % (word.strip(),1))