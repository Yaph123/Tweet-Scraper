# WRITE YOUR CODE HERE
def is_nested(d):
    for value in d.values():
        if isinstance(value, (list, tuple, dict)):
            return True
    return False


# test code below

# test code below
if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  print(is_nested(example_dict))
