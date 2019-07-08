import csv,pickle,sys
#import tam mapping
from Create_morph_obj import Morph_info,break_morph_info

# vibhakti global list
vibhakti_list=[]

infile = open("/home/arushi/PycharmProjects/mlpackage01/tam_map.pkl",'rb')
tam_dict = pickle.load(infile)
infile.close()

def group_to_list(group):
    res=group.strip()
    lis=res.split(" ")
    print(lis)
    for i in lis:
        if len(lis)==1:
            check_pronoun1(i)
#        elif len(lis)>1:

import subprocess #used to execute linux command in Python env.

def check_pronoun1(word,flag=False):
    for i in prop_list:
        if word in i:
           vibhakti_list.append(word+"_0")
           print("vibhakti list:---->")
           print(vibhakti_list)

           
#def check_pronoun2(word):



print(vibhakti_list)
print("***")

#print(tam_dict)
#print
#import pronoun list
infile = open("/home/arushi/PycharmProjects/mlpackage01/prop_list.pkl",'rb')
prop_list = pickle.load(infile)
infile.close()

#print(prop_list)
print
discourse_particle_list=['hI','BI','waka','nahI','wo']
quant_and_numl=['saba','sArA','kuCa','kaI','bahUwa','WodA','WodZA','jyAxA','eka','xo','wIna','cAra','pAzca','Caha','sAwa','ATa','nO','Xasa']


#karak relations list
karak_rel=['k1','k2','k3','k4','k5','k7','k7p','k7t','mk1','pk1','jk1','ras-k1','k2p','k4a','k1s','k2s']
#import concept dictionary
infile = open("/home/arushi/PycharmProjects/mlpackage01/concept_dictionary_map.pkl",'rb')
concept_dic = pickle.load(infile)
infile.close()
#print(concept_dic)
#print

infile = open("/home/arushi/PycharmProjects/mlpackage01/morph_objects.pkl",'rb')
morph_obj_list = pickle.load(infile)
infile.close()
for i in morph_obj_list:
    print(i.root)


#import concept dictionary
infile = open("WxList.pkl",'rb')
wxlist = pickle.load(infile)
infile.close()
print(wxlist)
print

import re

for i in wxlist:
    group_to_list(i)


