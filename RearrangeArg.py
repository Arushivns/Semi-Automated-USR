import sys #to use command line arguments
#print("This is the name of the script: ", sys.argv[0])
#print("Number of arguments: ", len(sys.argv))
#print("The arguments are: ", str(sys.argv))
res=" "
val=res.join(sys.argv[1:])

#print(val)
l=[]
i=0
valf=""

if(val.find("Z")!=-1):
    valf=val.replace("Z","")
else:
    valf=val
#print(valf)
import re
#print(valf[1:-1])

l=re.split("\)\s\(",valf[1:-2])
#print(l)
print(l)
import csv
file="semi_usr_rep.csv"

with open(file,'w') as usr:
    # creating a csv writer object
    csvwriter = csv.writer(usr)

    # writing the fields
    csvwriter.writerow(l)


import pickle
list_of_all_words=[]
for i in l:
    if len(i.split()) > 1:
        for j in i.split():
            list_of_all_words.append(j)
    else:
        list_of_all_words.append(i)
f=open("WxList.pkl","wb")
pickle.dump(list_of_all_words,f)
f.close()