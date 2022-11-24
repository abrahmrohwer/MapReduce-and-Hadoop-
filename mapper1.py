#!/usr/bin/env python

import sys
import re

tweets = sys.stdin
next(tweets)
for line in tweets:
	line=line.strip()
	words=line.split(",")
	if len(words)>1:
		userid = words[1]
		metric = int(words[-1]) + int(words[-2]) + int(words[-3])
		if (metric > 0) and (userid != ''):
			print('%s\t%s' % (userid,metric))