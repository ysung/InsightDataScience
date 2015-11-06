#!/usr/bin/env python

from datetime import datetime
import json
import re
from collections import Counter
import itertools
import sys

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def avgDegree(infile, outfile):
    with open(infile, 'r') as f, open(outfile, 'w') as text_file:
        q = [] 
        avg_degree = 0
        counter = 0
        rdict = {r'\\': '\\',
                 r'\'': '\'',
                 r'\/': '/',
                 r'\"': '"'
        }
        pat = re.compile(r"#(\w+)") # hashtag pattern
        
        for line in f:
            line = json.loads(line)
            if 'text' in line and 'created_at' in line:
                text = replace_all(line['text'], rdict) # replace escape characters
                text = re.sub(r'\s+', ' ', text) # replace whitespace escape characters with a single space.
                cleaned_text = re.sub(r'[^\x20-\x7F]+','', text) # remove non-ASCII unicode characters
                tag = set(pat.findall(cleaned_text)) # hashtags found in the tweet
                t = datetime.strptime(line['created_at'], '%a %b %d %H:%M:%S +0000 %Y') # replace string to datetime format
                q.append((tag, t)) # store hashtag and time into the queue

                # matain a queue with hashtag within 60 seconds
                while (q[-1][1]-q[0][1]).seconds > 60:
                    q.pop(0)
                edge = set()
                c = Counter()

                # create a set of edge list 
                for tag_60, t_60 in q:
                    if tag_60 > 1:
                        edge.update(list(itertools.combinations(tag_60, 2)))

                # caculate average defree
                for x, y in edge:
                    c[x] += 1
                    c[y] += 1
                if c:
                    avg = round(sum(c.values())/float(len(c)), 2)
                    text_file.write('{0:.2f}\n'.format(avg))
                else:
                    text_file.write('0.00\n')
avgDegree(sys.argv[1], sys.argv[2])
