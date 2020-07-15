'''
The parent_directory function returns the name of the directory that's located just above the current working directory. Remember that '..' is a relative path alias that means "go up to the parent directory". Fill in the gaps to complete this function.
'''

import os
def parent_directory():
  # Create a relative path to the parent 
  path = os.getcwd() 
  # of the current working directory 
  relative_parent = os.path.join(path, '..')

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)