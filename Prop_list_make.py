#this file creates a dictionary from Pronoun_lemma file in the communicator tool
#to make a nested list for pronoun list

# read the pronoun lemma file in comminicator tool
with open(r"/home/arushi/communicator-tool/dic/pronoun_lemma_dic.txt","r") as prop_lemma:
    s=prop_lemma.readlines()

print(s)

import collections
prop_dic = collections.defaultdict(list)
#prop_dic['pronoun'] = 'type','numGen','eng'
print(prop_dic)

import re
#regular expression module

#the following loop will create a dictionary in which pronouns are the keys and the details pertaining to them are the values if
#to given keys multiple values (because such value exists in the pronoun lemma file) we have used the if-else condition as shown
#below....

for i in s:
    r=i.replace('\t',',')
   # print(r)
    str=re.split(",",r)#using regular expression's split function to split stirng on comma..
    #print(str)
    if prop_dic.has_key(str[0]):
        prop_dic[str[0]].append(str[1:])
    else:
        prop_dic[str[0]] = list([str[1:]])

print(prop_dic)

#Once we are done with the dictionary creation part we can store the dictionary as a serializable object using the Pickle
#module of Python

import pickle
"""
The pickle module may be used to save dictionaries (or other objects) to a file. The 
module can serialize and deserialize Python objects.
"""

f=open("prop_list.pkl","wb")
pickle.dump(prop_dic,f)
f.close()