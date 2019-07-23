#importing all the files/Modules
import pickle
import csv

#function to read first row of semi_usr_rep.csv to get the group list
def get_the_groups():
    with open("semi_usr_rep.csv","r") as f:
        first_row=csv.reader(f)
        first_row_list=list(first_row)
        f.close()
    return first_row_list


#import tam mapping
infile = open("/home/arushi/PycharmProjects/mlpackage01/tam_map.pkl",'rb')
tam_dict = pickle.load(infile)
infile.close()
#print(tam_dict)

discourse_particle_list=['hI','BI','waka','nahI','wo']
quant_and_numl=['saba','sArA','kuCa','kaI','bahUwa','WodA','WodZA','jyAxA','eka','xo','wIna','cAra','pAzca','Caha','sAwa','ATa','nO','Xasa']


#karak relations list
karak_rel=['k1','k2','k3','k4','k5','k7','k7p','k7t','mk1','pk1','jk1','ras-k1','k2p','k4a','k1s','k2s']

#import concept dictionary
infile = open("/home/arushi/PycharmProjects/mlpackage01/concept_dictionary_map.pkl",'rb')
concept_dic = pickle.load(infile)
infile.close()
#print(concept_dic)

#import pronoun list

infile = open("/home/arushi/PycharmProjects/mlpackage01/prop_list.pkl",'rb')
prop_list = pickle.load(infile)
infile.close()
#print(prop_list)


#Class to store the information of morph analysis

class Morph_info:
    word=""
    root=""
    morph_dic={}
    def __init__(self,word,root,moph_dic):
        self.word=word
        self.root=root
        self.morph_dic=dict(moph_dic)

#group list is a list of lists so we'll make a flat list (which is only a list of groups in the sentence)
#and write this values to the variable named group_flat_list

group_list=get_the_groups()
group_flat_list = [item for group_list[0] in group_list for item in group_list[0]]


print(group_list)
infile = open("/home/arushi/PycharmProjects/mlpackage01/WxList.pkl",'rb')
all_words_in_sentence_list = pickle.load(infile)
infile.close()
print(all_words_in_sentence_list)


#to import the pickled morph objects
dictionary_of_all_the_morph_objects = {}
infile = open('morph_objects.pkl', 'r')
while 1:
    try:
        #lists.append(pickle.load(infile))
        for i in all_words_in_sentence_list:
            dictionary_of_all_the_morph_objects[i]=pickle.load(infile)
    except (EOFError):
        break
infile.close()
#print(lists)

for keys,values in dictionary_of_all_the_morph_objects.items():
    print(keys,":")
    for j in values:
        print(j.root)
        print(j.morph_dic)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

#importing morph object ends
#second row list
concept_mapping=[]

for i in range(len(group_flat_list)):
    print(group_flat_list[i])
    if len(group_flat_list[i].split()) ==1:
        #check for pronoun
        #code to check bare pronoun
        for key, value in prop_list.iteritems():  # iter on both keys and values
            if key.startswith(group_flat_list[i]):
                print(key)
                print(value)
                concept_mapping.append(key)
        #code to check inflected pronoun
        for key, value in dictionary_of_all_the_morph_objects.iteritems():  # iter on both keys and values
            if key.startswith(group_flat_list[i]):
                print(key)
                for j in value:
                    print(j.morph_dic)
                concept_mapping.append(j.root + "_" + j.morph_dic['parsarg'])


print(concept_mapping)



""""
        for key, value in dictionary_of_all_the_morph_objects.iteritems():  # iter on both keys and values
            if key.startswith(group_flat_list[i]):
                print(key)
                for j in value:
                    print(j.morph_dic)
                concept_mapping.append(j.root+"_"+j.morph_dic['parsarg'])
#######################################################################################
        for i in prop_list.keys():
            if text in i:
                second_row.append(text+"_0")
        #else:
"""

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
