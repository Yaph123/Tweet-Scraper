# WRITE YOUR CODE HERE

def find_key(my_dict,val):

  for key in my_dict:
    if my_dict[key] == val:
      return key

  return 0



# test code below
if __name__ == "__main__":
  example_dict = {
    1 : ['red', 'blue', 'green'],
    'Josh Jung' : (9, 10),
    3 : {0 : 0},
    9000 : 'impale mat a'
  }

  key = find_key(example_dict, 'impale mat a')
  print(key)


