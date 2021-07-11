import os
import shutil

path = 'copy.txt'
try:
    #os.remove(path) #delete a file
    #os.rmdir(path) #delete folder, only is empty
    #shutil.rmtree(path) #be careful, this function is danger
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("you do not have permission to delete that  ")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")