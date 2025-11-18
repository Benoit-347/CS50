import os
for i in range(1, 100+1):
    path = f"test_folder\parent_folder_{i}"
    for i in range(1,11):
        sub_path = os.path.join(path, f"sub_folder_{i}")
        with open(os.path.join(sub_path, "text_file_1.txt"), 'w') as file_object:
                  file_object.write("Hello world")