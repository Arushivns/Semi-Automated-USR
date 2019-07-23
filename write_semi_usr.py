import csv,pickle,sys
#import tam mapping
from Create_morph_obj import Morph_info,break_morph_info

# vibhakti global list
vibhakti_list=[]

infile = open("/home/arushi/PycharmProjects/mlpackage01/tam_map.pkl",'rb')
tam_dict = pickle.load(infile)
infile.close()



def load_pickle():
    data2 = []
    with open("morph_objects.pkl", "rb") as f:
        for _ in pickle.load(f):
            data2.append(pickle.load(f))
            print(_.root, 'ppppppppppppppppppppppp')
    print("list of morph objects")
    print(data2)
    for i in data2:
        for j in i:
            print(j.word)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    return data2

def group_to_list(group):
    res=group.strip()
    lis=res.split(" ")
    print(lis)
    for i in lis:
        if len(lis)==1:
            check_pronoun1(i)
#        elif len(lis)>1:



def check_pronoun1(word):
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

"""
infile = open("/home/arushi/PycharmProjects/mlpackage01/morph_objects.pkl",'rb')
morph_obj_list = pickle.load(infile)
infile.close()
print(morph_obj_list)
"""


#import concept dictionary
infile = open("WxList.pkl",'rb')
wxlist = pickle.load(infile)
infile.close()
print(wxlist)
print

import re

for i in wxlist:
    group_to_list(i)




morph_object_list=load_pickle()
print("hello")
"""
for l in morph_object_list:
    for j in l:
        print(j.root)
"""