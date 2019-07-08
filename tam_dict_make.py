import csv
with open('/home/arushi/communicator-tool/dic/tam_mapping.csv','r')as f:
  data = csv.reader(f)
  #initialize a dictionary for tam mapping
  tam_map={}
  for row in data:
    print(row)
    tam_map[row[0]]=row[1:]


print(tam_map)

import pickle

f=open("tam_map.pkl","wb")
pickle.dump(tam_map,f)
f.close()