#using fn from different dir
import sys, os
#sys.path.append(os.path.join(os.path.dirname(__file__), 'Class_4'))
sys.path.append("D:\My_Folder_Parent\Study\Programming\Python_files\CS50_harward_class\Class_4")
import my_fns
my_fns.check_input(5)