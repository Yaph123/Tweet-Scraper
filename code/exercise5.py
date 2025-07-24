# WRITE YOUR CODE HERE
import json

def compare(file1, file2):
    with open(file1, 'r') as f1:
        dict1 = json.load(f1)
    with open(file2, 'r') as f2:
        dict2 = json.load(f2)

    if dict1 == dict2:
        return "The dictionaries are equal"
    
    len1 = len(dict1)
    len2 = len(dict2)

    if len1 > len2:
        return "Dictionary 1 is longer than dictionary 2"
    elif len2 > len1:
        return "Dictionary 2 is longer than dictionary 1"
    else:
        return "Dictionary 1 and dictionary 2 have the same length"


# test code below
# test code below
if __name__ == "__main__":
  import sys
  
  file1 = sys.argv[1]
  file2 = sys.argv[2]

  print(compare(file1, file2))
