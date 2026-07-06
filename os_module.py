import os
#os.mkdir('docs')  # create a new directory or folder called 'docs'

#os.chdir('docs')  # change the current working directory to 'docs'

#print(f"Current working directory: {os.getcwd()}")  # print the current working directory

#os.chdir('..')  # change the current working directory back to the parent directory
print(f"Current working directory: {os.getcwd()}")  
print(os.listdir())  # list the files and directories in the current working directory

for item in os.listdir():
    print(f"{item}")

os.rmdir('docs')  # remove the 'docs' directory (only works if the directory is empty)