# WRITE YOUR CODE HERE

def move_to_bottom(mydict,key):

  if key not in mydict:
    return 'The key is not in the dictionary'
  
  value = mydict.pop(key)
  mydict[key] = value
  return mydict


# test code below

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  move_to_bottom(example_dict, 1)
  print(example_dict)
