print("Hello")

import sys #to use command line arguments
print( "This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))
# read the pronoun lemma dictionary from
import pickle
infile = open("prop_list.pkl",'rb')
prop_dict = pickle.load(infile)
infile.close()
#pronoun dictionary read from plk file
print(prop_dict)

import subprocess #used to execute linux command in Python env.


#Class to store the information
class Morph_info:
    word=""
    root=""
    morph_dic={}
    def __init__(self,word,root,moph_dic):
        self.word=word
        self.root=root
        self.morph_dic=dict(moph_dic)


#function to remove underscore from the given WX sentense
def cleanse(str):
#    res=str.replace("_"," ")
    return str[1:len(str)-1]


import re
#to check if the stirng has a pronoun or not
def prop_check(str):
    l=re.split(" ",str)
    print(l)
#    for i in l:
#        if i in prop_dict:

def send_to_morph(group_str):
    l=re.split("_",group_str)
    print(l)
    for i in l:
        f = open("WxWord", "w+")
        f.write(i)
        f.seek(0)
        print(f.read(25))
        f1=open('jnk.morf',"r")
        #out = subprocess.Popen(['bash','./doMorphAnal.sh'])
        print("----------------------------")
        print(f1.read())
        print("*********************")
        f.close()
        f1.close()

def break_morph_info():
    f=open("jnk.morf","r")
    morph_info=f.read()
    print(morph_info)
    word=morph_info[2:morph_info.index('/')]
    #print(word+":)")
    morph_anl_dic={}
    morph_stri=morph_info[morph_info.index("/")+1:]
    print(morph_stri)
    spilt_info=re.split("/",morph_stri)
    print(spilt_info)
    #list of morph objects
    morph_objects=[]
    for i in spilt_info:
        root=i[0:i.index("<")]
        print(root)
        dic_list=re.findall(r"\w+:\w+",i[i.index("<"):])
        #print(dic_list)
        for j in dic_list:
            morph_anl_dic[j[0:j.index(":")]] = j[j.index(":") + 1:]
        print(morph_anl_dic)
        morph_objects.append(Morph_info(word,root,morph_anl_dic))


"""
    l=re.findall(r"\w+:\w+",t)
    print(l)
    morph_anl_dic={}
    for i in l:
        morph_anl_dic[i[0:i.index(":")]]=i[i.index(":")+1:]
    print(morph_anl_dic)
"""

'''
import subprocess #used to execute linux command in Python env.
out = subprocess.Popen(['lt-proc', '/home/arushi/new_hnd_mo/mydata'],
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)

The output from subprocess.Popen is subprocess.Popen object. And this object has 
number of methods associated with it and we will be using communicate() method to get 
the standard output and error in case as a tuple.


stdout,stderr = out.communicate()
print(stdout)
'''


#wil check each groups' semantic information...to be constructed

for i in range(1,len(sys.argv)):
    #print(sys.argv[i])
    str=cleanse(sys.argv[i])
    print(str)
    send_to_morph(str)


break_morph_info()