import os


try:
    os.remove('novel.txt')
except:
    print('File not found')  

os.rename('firt_draft.txt', 'final_masterpiece')
filename = ''
os.path.exist(filename)    

    