import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  filesize = ''
  with open(filename, 'w') as file:
    file.write(comments)
    new_file = file
    filesize = os.path.getsize(new_file)
  return(filesize)

print(create_python_script("program.py"))