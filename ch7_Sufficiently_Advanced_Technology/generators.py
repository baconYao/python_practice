import os

# Wrap os.walk in generator
def log_files(dir_name, file_type):
    if not os.path.exists(dir_name):
        raise ValueError(dir_name + " not found!")
    if not os.path.isdir(dir_name):
        raise ValueError(dir_name + " is not a directory!")

    for path, dirs, files in os.walk(dir_name):
        log_files = [f for f in files if f.endswith(file_type)]

        for each_file in log_files:
            yield os.path.join(path, each_file)

# Generator for each line of files
def log_lines(dir_name, file_type):
    for each_file in log_files(dir_name, file_type):
        for each_line in file(each_file).readlines():
            yield (each_file, each_line.strip())

# Fileter out non-error lines
def list_errors(dir_name, file_type):
    return (each_file + ": " + each_line.strip() for each_file, each_line in log_lines(dir_name, file_type) if 'error' in each_line.lower())

if __name__ == '__main__':
    dir_name = '/var/log'
    file_type = '.log'
    # Create generators
    for each_file in log_files(dir_name, file_type):
        print each_file
    print
    # Create generators
    for each_error in list_errors(dir_name, file_type):
        print each_error