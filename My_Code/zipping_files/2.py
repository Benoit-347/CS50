#extracting folders

import zipfile, os
path = os.getcwd()
path_final = os.path.join(path, r"test_result\test_folder.zip")
zip_object = zipfile.ZipFile(path_final)
zip_object.extractall("test_result")