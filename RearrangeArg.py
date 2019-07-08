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

l=re.split("\)\(",valf[1:-1])
#print(l)
print(l)
import csv
file="semi_usr_rep.csv"

import pickle
f=open("WxList.pkl","wb")
pickle.dump(l,f)
f.close()

with open(file,'w') as usr:
    # creating a csv writer object
    csvwriter = csv.writer(usr)

    # writing the fields
    csvwriter.writerow(l)