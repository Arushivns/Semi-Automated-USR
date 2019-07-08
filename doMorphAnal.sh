#!/bin/bash

#Ask for user input in devnagri script, the input will be supplied as command line argument
echo The sentence provided reads as follows.

#converting the hindi sentence to its equivalent Wx Notation.
wxstr=$(utf8_wx /home/arushi/PycharmProjects/mlpackage01/str_test)
echo $wxstr
#echo $wxstr | cut -d "(" -f2 | cut -d ")" -f1
#sed 's/.*(\(.*\))/\1/' $wxstr 

#python ./RearrangeArg.py $wxstr
#this program removes "Z" (because morph analyser does not recognize it) and it rearranges the command line argument and returns a list of all the groups along with the number of groups appended at the of list.

OUTPUT=($(python /home/arushi/PycharmProjects/mlpackage01/RearrangeArg.py $wxstr | tr -d '[],'))
#the out of the python script is stored as a bash array
echo ${OUTPUT[@]}
#the above command will print all the values stored in the bash array
echo ${#OUTPUT[@]} to know the number of arguments returned as the output of the python program

#for loop begins for writing the morph object file
for i in "${OUTPUT[@]}"
	do
echo $i
OUTPUT=($(python /home/arushi/PycharmProjects/mlpackage01/Cleanse.py $i| tr -d '[],'))
#the above program removes extra quotes and punctuation marks.
echo ${OUTPUT[0]}
# The following script will write individual words to morph analyser
python /home/arushi/PycharmProjects/mlpackage01/Write_wx.py ${OUTPUT[0]}
#Now we'll write each word to WxWord file and send it to the morphological analyser using the commands below
#this whole command does the morphological analysis of all WX word representation present in WxWord text file
cat /home/arushi/PycharmProjects/mlpackage01/WxWord | lt-proc -ac /home/arushi/new_hnd_mo/mydata | apertium-retxt > jnk.morf
#After the execution of this command the analysis is stored in jnk.morf file
cat jnk.morf
#to create objects from morph analysis file and store them
echo "*****************************************"
python /home/arushi/PycharmProjects/mlpackage01/Create_morph_obj.py
echo "*****************************************"
	done
#for loop ends


#now we'll start printing the rows required for Universal Semantic Representation semi-automatically....






#delete the morph_objects.pkl file because it is in append mode so even if we run the program for testing the file size will keep increasing.
#rm -rf /home/arushi/PycharmProjects/mlpackage01/morph_objects.pkl




