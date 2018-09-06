import textwrap

todos = []

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

def capitalize(todo):
    todo['level'] = todo['level'].upper()
    return todo

def show_todo(todo, index):
    # wrapping title and description
    wrapped_title = textwrap.wrap(todo['title'], 16)
    wrapped_descr = textwrap.wrap(todo['description'], 24)
    # output first line
    output = str(index+1).ljust(8) + " "
    output += wrapped_title[0].ljust(16) + " "
    output += wrapped_descr[0].ljust(24) + " "
    output += todo['level'].ljust(16)
    output += "\n"

    max_len = max(len(wrapped_title), len(wrapped_descr))
    # output any remaining lines
    for index in range(1, max_len):
        output += " " *8 + " "
        if index < len(wrapped_title):
            output += wrapped_title[index].ljust(16) + " "
        else:
            output += " " *16 + " "
        if index < len(wrapped_descr):
            output += wrapped_descr[index].ljust(24) + " "
        else:
            output += " " *24 + " "
        output += "\n"
    return output

def sort_todos(todos):
    # Use list comprehension style to filter to-dos
    important = [capitalize(todo) for todo in todos if todo['level'].lower() == 'important']
    unimportant = [todo for todo in todos if todo['level'].lower() == 'unimportant']
    medium = [todo for todo in todos if todo['level'].lower() != 'important' and todo['level'].lower() != 'unimportant']
    # Join to-dos back up
    sorted_todos = important + medium + unimportant
    return sorted_todos

def show_todos(todos):
    output = ("Item     Title            Description              Level\n")
    sorted_todos = sort_todos(todos)
    for index, todo in enumerate(sorted_todos):
        output += show_todo(todo, index)
    # print output
    return output

# Given the name of the command you want to run, get_function will return the function you need to call
commands = {
    # Key: command, value: the function that will be called
    'new': [create_todo, ['title', 'description', 'level']],
    'test': [test, ['abcd', 'ijkl']],
    'show': [show_todos, []]
}


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