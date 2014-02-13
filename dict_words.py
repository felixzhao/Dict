#!/usr/bin/python
# -*- coding: utf-8 -*-

fin = open('_Dict-SC2TC.Sort.V1_Simple_Chinese_UTF8.txt','r',encoding='utf-8')

fout = open('words.txt','wb')

words = []

lines = fin.readlines()

for l in lines:
  for char in l:
    if char not in words:
      words.append(char)

for w in words:
  fout.write(w.encode('utf-8'))
  fout.write('\n'.encode('utf-8'))