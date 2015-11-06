#!/usr/bin/env python

import json
import re
import sys

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def tweetClean(infile, outfile):
    with open(infile, 'r') as f, open(outfile, "w") as text_file:
        uni_count = 0
        rdict = {r'\\': '\\',
                 r'\'': '\'',
                 r'\/': '/',
                 r'\"': '"'
        }
        for line in f:
            line = json.loads(line)
            if 'text' in line and 'created_at' in line:
                text = replace_all(line['text'], rdict) # replace escape characters
                text = re.sub(r'\s+', ' ', text) # replace whitespace escape characters with a single space.
                cleaned_text = re.sub(r'[^\x20-\x7F]+','', text) # remove non-ASCII unicode characters
                if text != cleaned_text:
                    uni_count += 1
                t = line['created_at']
                text_file.write('{0} (timestamp: {1})\n'.format(cleaned_text, t))
        text_file.write('\n{0} tweets contained unicode.'.format(uni_count))

tweetClean(sys.argv[1], sys.argv[2])