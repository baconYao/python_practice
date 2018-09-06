# Import todo.py in same directory
import todo

def test_create_todo():
    # List of to-dos
    todo.todos = []
    # Run small part of program
    todo.create_todo(todo.todos, title="Make some stuff", description="Stuff needs to be programmed", level="Important")

    # Test results
    assert len(todo.todos) == 1, "Todo was not created!"
    assert todo.todos[0]['title'] == "Make some stuff"
    assert (todo.todos[0]['description'] == "Stuff needs to be programmed")
    assert todo.todos[0]['level'] == "Important"

    print "Ok - create_todo"

def test_get_function():
    assert todo.get_function('new') == todo.create_todo
    print "OK - get_function"

def test_get_fields():
    assert (todo.get_fields('new') == ['title', 'description', 'level'])
    print "OK - test_get_fields"

def test_run_command():
    # Create "test" command
    result = todo.run_command(
        'test',
        {'abcd': 'efgh', 'ijkl': 'mnop'}        # Design by wishful thinking
    )
    expected = """Command 'test' returned:
abcd: efgh
ijkl: mnop"""
    assert result == expected, \
                    result + " != " + expected
    print "OK - run_commnad"

def test_show_todos():
    # Set up data
    todo.todos = [
        {
            'title': 'test todo',
            'description': 'This is test',
            'level': 'Important'
        }
    ]
    # Run show_todos function
    result = todo.show_todos(todo.todos)
    lines = result.split("\n")

    # Test results
    first_line = lines[0]
    assert "Item" in first_line
    assert "Title" in first_line
    assert "Description" in first_line
    assert "Level" in first_line

    second_line = lines[1]
    assert "1" in second_line
    assert "test todo" in second_line
    assert "This is a test" in second_line
    assert "Important" in second_line

    print "OK - show_todos"

# Run test
test_create_todo()
test_get_function()
test_get_fields()
test_run_command()

