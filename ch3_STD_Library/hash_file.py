import hashlib
import sys

file_name = sys.argv[1]
# Create the hash obj
read_file = file(file_name)
the_hash = hashlib.md5()
# Update hash
for line in read_file.readlines():
    the_hash.update(line)
print the_hash.hexdigest()

