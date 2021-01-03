# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:25:45 2020

@author: RAJARSI
" Here we will develop a program to methodically implement Huffman Encoding"
"input: a dictionary of characters and their corresponding frequncy in the text"
"output: a dictionary of characters and their corrsponding string representation"
""
"""
######## INITIALIZATONS ########
"a dictionary to store the string representation of each character"

######## HELPER FUNCTIONS ########
def freq_counter(txt):
  " Function to produce the frequency count of charactes in a given text"
  freq = {}
  rep = {}
  chars = set(txt)
  chars = sorted(list(chars))
  for _ in chars:
    freq[_] = txt.count(_)
    rep[_] = ''
  return freq,rep 

def key_finder(dct,val):
  " Function to find a key corresponding to value"  
  for _ in list(dct.keys()):
        if dct[_] == val:
            return _

def rev(txt):
  " Function to reverse the order of a given string "
  return txt[::-1]
          
def dict_update(dictionary,rep):
  " Function to update the input dictionary by removing two keys (a & b) with minimum values and appending a key (a+b) "
  #### find  the minimum values
  vl0 = sorted(dictionary.values())[0]
  vl1 = sorted(dictionary.values())[1]
  #### find the keys to l1 and l2 and remove them from dictionary
  ky0 = key_finder(dictionary,vl0)
  del (dictionary[ky0])
  ky1 = key_finder(dictionary,vl1)
  del (dictionary[ky1])
  #### update the rep.dictionary 
  ## for ky0
  for _ in ky0.split('+'):
    rep[_] = rep[_] + '0'
  ## for ky1  
  for _ in ky1.split('+'):
    rep[_] = rep[_] + '1'
  #### append the key 'ky1 + ky2' with value vl1+vl2
  dictionary[ky0+'+'+ky1] = vl0 + vl1
  #### return the dictionary
  return dictionary,rep

def huff_update(dic,rep):
    " Function to iteratively update the given dictionary #dic to obtain the final string representation #rep "
    while len(dic) >1 :
      rep = dict_update(dic,rep)[1]
    for _ in rep.keys() :
      rep[_] = rev(rep[_])
    return rep  
######## MAIN OUTPUT TERMINAL  ##########
def huffman_char_encoding(text):    
      " Input the text #text directly into this function and it will return a dictionary depicting the encoding for every character"
      dc = huff_update(freq_counter(text)[0],freq_counter(text)[1])
      return dc
######## MAIN ENCODER TERMINAL ##########  
def huffman_text_encoder(text):
  " Input the text #text directly into this function to obtain the encoded text"
  dc, txt = huffman_char_encoding(text),''
  for _ in list(text):
    txt = txt + dc[_]
  return txt 
######### DECODING TERMINAL ###########
def huffman_text_decoder(entxt,dic):
  " Input the encoded Text #entxt and the corresponding Dictionary #dic to obtain the decoded text "
  dtxt = ""
  cd = ""
  _ = 0
  while _< len(entxt) :   
    if cd in dic.values():
      phrase = key_finder(dic,cd)
      dtxt = dtxt + phrase
     # print('*'+dtxt+'|'+str(_))
      cd = ""
    else :
      cd = cd + entxt[_] 
     # print(cd+'|'+str(_))
      _ = _ + 1
  return dtxt    
      
    
