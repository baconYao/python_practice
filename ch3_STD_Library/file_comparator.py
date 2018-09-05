"""
This is example about difference_engine.py
How to use:
    type 'python file_comparator.py test test2' in command line
"""
import hashlib
import sys
import os

def md5(file_path):
    """Return an md5 checksum for a file."""
    if os.path.isdir(file_path):
        return '1'
    read_file = file(file_path)
    the_hash = hashlib.md5()
    for line in read_file.readlines():
        the_hash.update(line)
    return the_hash.hexdigest()

def directory_listing(dir_name):
    """Return all of the files in a directory"""
    # Finding root of directory
    dir_file_list = {}
    dir_root = None
    dir_trim = 0
    for path, dirs, files, in os.walk(dir_name):
        if dir_root is None:
            dir_root = path
            dir_trim = len(dir_root)
            print "dir", dir_name, "root is", dir_root
            print
        # Building dictionary of files
        trimmed_path = path[dir_trim:]
        if trimmed_path.startswith(os.path.sep):
            trimmed_path = trimmed_path[1:]
        for each_file in files + dirs:
            file_path = os.path.join(trimmed_path, each_file)
            dir_file_list[file_path] = True
    return (dir_file_list, dir_root)        # Returning multiple values

if len(sys.argv) < 3:
    print "You need to specify two directories:"
    print sys.argv[0], "<directory 1> <directory 2>"
    sys.exit()

directory1 = sys.argv[1]
directory2 = sys.argv[2]

print "Comparing--->", directory1, "and", directory2
print "--------------------"

dir1_file_list, dir1_root = directory_listing(directory1)
dir2_file_list, dir2_root = directory_listing(directory2)
results = {}

for file_path in dir2_file_list.keys():
    # Files not in directory 1
    if file_path not in dir1_file_list:
        results[file_path] = "not found in directory 1"
    else:
        # Compare checksum
        # print file_path, "found in directory 1 and 2"
        file1 = os.path.join(dir1_root, file_path)
        file2 = os.path.join(dir2_root, file_path)
        if md5(file1) != md5(file2):
            # print file1, "and", file2, "differ!"
            results[file_path] = "is different in directory2"
        # del dir1_file_list[file_path]
        else:
            results[file_path] = "is the same in both"

for file_path, value in dir1_file_list.items():
    if file_path not in results:
        results[file_path] = "not found in directory 2"

print 
for file_path, value in sorted(results.items()):
    if os.path.sep not in file_path and "same" not in value:
        print file_path, value

for file_path, value in sorted(results.items()):
    if os.path.sep in file_path and "same" not in value:
        print file_path, value

# print results.items()