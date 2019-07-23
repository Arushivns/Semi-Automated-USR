concept_map={}

with open("/home/arushi/communicator-tool/dic/concept_dictionary_user.txt","rb") as c:
    for data in c:
        l=data.split(",")
        concept_map[l[0]]=l[1:len(l)-1]


print(concept_map)


import pickle
f=open("concept_dictionary_map.pkl","wb")
pickle.dump(concept_map,f)
f.close()