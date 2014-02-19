#!/usr/bin/python
# -*- coding: utf-8 -*-

length_limit = 6

word_flag = 0

fin = open('_Dict-SC2TC.Sort.V1_Simple_Chinese_UTF8.txt','r',encoding='utf-8')

fout = open('terms.txt','wb')

## test
#fin = open('_test_dict.txt','r',encoding='utf-8')
#fout = open('test.txt','wb')

terms = {}

lines = fin.readlines()

for s in lines:
  l = len(s)
  if l > length_limit:
    continue
  for i in range(l):
    cur_term = s[0:i]
    if i == l - 1:
      terms[cur_term] = word_flag
    elif cur_term not in terms or (cur_term in terms and l > terms[cur_term]):
      terms[cur_term] = l - 1

for k in terms.keys():
  if k != '':
    str_out = k + ' ' + str(terms[k])
    fout.write(str_out.encode('utf-8'))
    fout.write('\n'.encode('utf-8'))