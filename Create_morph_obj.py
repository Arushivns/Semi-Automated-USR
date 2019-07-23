import re
import pickle
import json
#Class to store the information
class Morph_info:
    word=""
    root=""
    morph_dic={}
    def __init__(self,word,root,moph_dic):
        self.word=word
        self.root=root
        self.morph_dic=dict(moph_dic)



def break_morph_info():
    f = open("jnk.morf", "r")#to read the file with morph analysis
    morph_info = f.read()
    #print(morph_info)
    # Extracts the word for which this morph analysis is obtained.
    word = morph_info[2:morph_info.index('/')]
    print("word= "+word)
    morph_anl_dic = {}
    morph_stri = morph_info[morph_info.index("/") + 1:]
    #print(morph_stri)
    spilt_info = re.split("/", morph_stri)
    #print(spilt_info)
    # dictionary of morph objects
    morph_objects = []
    for i in spilt_info:
        root = i[0:i.index("<")]
        print("root= "+root)
        dic_list = re.findall(r"\w+:\w+", i[i.index("<"):])
        # print(dic_list)
        for j in dic_list:
            morph_anl_dic[j[0:j.index(":")]] = j[j.index(":") + 1:]
        print(morph_anl_dic)
        morph_objects.append(Morph_info(word, root, morph_anl_dic))
    with open("morph_objects.pkl", 'ab') as mo:
        pickle.dump(morph_objects, mo)
    f.close()
    mo.close()






#function calling
break_morph_info()
