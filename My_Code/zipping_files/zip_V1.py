"""
features:
1. create zip file of specified path to cwd
2. move zip file to specified dir
3. mk dir if not exist while moving zip file
"""


from zipfile import ZipFile
import os
def create_zip(folder_path, zip_name = None):
    if not zip_name:
        zip_name = os.path.basename(folder_path) + ".zip"
    zip_object = ZipFile(zip_name, "w")
    for cwd, folder, files in os.walk(folder_path):
        for file in files:
            path = os.path.join(cwd, file)
            arcname = os.path.relpath(path, folder_path)
            zip_object.write(path, arcname)
            print("done")
    zip_object.close()
    
    if os.path.isfile(zip_name):
        print("Zip creation successful")
    return zip_name

def zip_to(source, destination, file_name = None):

    #creating zip file at cwd
    zip_name = create_zip(source, file_name)

    #to remove old file with same name
    zip_path_loc = os.path.join(destination, zip_name)
    if os.path.isfile(zip_path_loc):
        if int(input("File already exists\nDo you want to remove old file (1/0):")):
            os.unlink(zip_path_loc)
        else:
            print("exited as file aready exists, chose to not delete")
            return 0

    #to move zip to derired loc
    from shutil import move
    if not os.path.exists(destination):
        os.makedirs(destination)
    move(zip_name, destination)
    if os.path.isfile(zip_path_loc):
        print(f"New zip file moved to dir: {destination}")
if __name__ == "__main__":
    zip_to(r"D:\My_Folder_Parent\Study\Programming\Python_files\My_Repositories\Rns_Class\Python\Module_3", r"D:\New")
    