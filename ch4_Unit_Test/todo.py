def create_todo(todos, title, description, level):
    """Create an todo item"""
    todo = {
        "title": title,
        "description": description,
        "level": level
    }
    todos.append(todo)

def test(todos, abcd, ijkl):
    return "Command 'test' returned:\n" + \
        "abcd: " + abcd + "\nijkl: " + ijkl

# Given the name of the command you want to run, get_function will return the function you need to call
commands = {
    # Key: command, value: the function that will be called
    'new': [create_todo, ['title', 'description', 'level']],
    'test': [test, ['abcd', 'ijkl']]
}

# Get command's first value, means that the function will be called
def get_function(command_name):
    return commands[command_name][0]
# Get command's second value, means that the details we need
def get_fields(command_name):
    return commands[command_name][1]

def get_input(fields):
    user_input = {}
    for field in fields:
        user_input[field] = raw_input(field + " > ")
    return user_input

todos = []

def run_command(user_input, data=None):
    user_input = user_input.lower()
    if user_input not in commands:
        return user_input + "? " \
            "I don't know what that command is."
    else:
        # Figure out which command function you need to run
        the_func = get_function(user_input)

    # Get input from user, if necessary
    if data is None:
        the_fields = get_fields(user_input)
        data = get_input(the_fields)
    # Call function
    return the_func(todos, **data)

def main_loop():
    user_input = ""
    while 1:
        # Do something with user input
        print run_command(user_input)
        # Get new input
        user_input = raw_input("> ")
        # Check to see if you should quit
        if user_input.lower().startswith("quit"):
            print "Exiting..."
            break

# Only run main_loop if you're run directly
if __name__ == '__main__':
    main_loop()