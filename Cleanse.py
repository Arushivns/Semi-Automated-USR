import re
import sys

#print(sys.argv[1])
val=re.findall("\w+",sys.argv[1])
print(val)


