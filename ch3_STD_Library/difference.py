import sys
import os

if len(sys.argv) < 3:
    print "You need to specify two directories:"
    print sys.argv[0], "<directory 1> <directory 2>"
    sys.exit()

dir1 = sys.argv[1]
dir2 = sys.argv[2]

print "Comparing:"
print dir1
print dir2
print

# The path of argv[1]
path1 = ""
# The path of argv[2]
path2 = ""

for dir in [dir1, dir2]:
    # print os.path.abspath(dir)
    # dirName = os.path.abspath(dir).split("/").pop()
    # print dirName
    if dir == "d1":
        path1 = os.path.abspath(dir)
    else:
        path2 = os.path.abspath(dir)

    if not os.access(dir, os.F_OK):
        print dir, "isn't a valid directory!"
        sys.exit()

    print "Directory", dir
    for item in os.walk(dir):
        print item
    print

# Read content from specific file
read_file = file(os.path.join(path1, "foo2.py"))            # Open the file
file_contents = list(read_file.readlines())                  
print "Read in", len(file_contents), "lines from foo2.py"    
print "The first line reads:", file_contents[0]

# Write data into some file

write_file = file(os.path.join(path2, "write_file.txt"), "w")           # Open the file
write_file.write("First Line\n")        # Write one line
# Write multiple lines
write_file.writelines([     
    "The Second\n",
    "The Third\n"
])
write_file.close()          # Close file