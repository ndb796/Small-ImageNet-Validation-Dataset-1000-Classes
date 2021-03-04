import os
import json


def get_list(path):
    return os.listdir(path)


def rename_directory(root_path, directory, targets):
    source = os.path.join(root_path, directory)
    target = os.path.join(root_path, targets[directory])
    os.rename(source, target)


def remove_files(root_path, directory, n_remained):
    files = get_list(os.path.join(root_path, directory))
    files = files[n_remained:]
    for file_name in files:
        os.remove(os.path.join(root_path, directory, file_name))


# Run the program
root_path = './ILSVRC2012_img_val'
with open('./imagenet_class_index.json') as f:
    json_data = json.load(f)
targets = {}
for key in json_data.keys():
    targets[json_data[key][0]] = key

directories = get_list(root_path)
for directory in directories:
    remove_files(root_path, directory, 5)
for directory in directories:
    rename_directory(root_path, directory, targets)
