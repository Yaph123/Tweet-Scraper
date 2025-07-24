# WRITE YOUR CODE HERE

def swap(mydict):
    unhashable_types = (list, dict, set)
    
    for value in mydict.values():
        if isinstance(value, unhashable_types):
            return "Cannot swap the keys and values for this dictionary"
    
    return {value: key for key, value in mydict.items()}

# test code below

 # test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  swapped = swap(example_dict)
  print(swapped)
