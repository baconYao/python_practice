# Import todo.py in same directory
import todo
import os

def test_create_todo():
    # List of to-dos
    todo.todos = []
    # Run small part of program
    todo.create_todo(todo.todos, title="Make some stuff", description="Stuff needs to be programmed", level="Important")
    # Test results
    assert len(todo.todos) == 1, "Todo was not created!"
    assert todo.todos[0]['title'] == "Make some stuff"
    assert (todo.todos[0]['description'] == "Stuff needs to be programmed")
    assert todo.todos[0]['level'] == "IMPORTANT"

    print "Ok - create_todo"

def test_get_function():
    assert todo.get_function('new') == todo.create_todo
    print "OK - get_function"

def test_get_fields():
    assert (todo.get_fields('new') == ['title', 'description', 'level'])
    print "OK - get_fields"

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
            'description': 'This is a test',
            'level': 'Important'
        }
    ]
    todo.sort_todos()
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
    assert "IMPORTANT" in second_line

    print "OK - show_todos"

def test_todo_sort_order():
    todo.todos = [
        {
            'title': 'test unimportant todo',
            'description': 'An unimportant test',
            'level': 'Unimportant'
        },
        {
            'title': 'test medium todo',
            'description': 'A test',
            'level': 'Medium'
        },
        {
            'title': 'test important todo',
            'description': 'This is an important test',
            'level': 'Important'
        }
    ]
    todo.sort_todos()
    result = todo.show_todos(todo.todos)
    lines = result.split("\n")

    assert "IMPORTANT" in lines[1]
    assert "Medium" in lines[3]
    assert "Unimportant" in lines[4]

    print "OK - todo sort order"

def test_todo_wrap_long_lines():
    todo.todos = [
        {
            'title': 'test important todo',
            'description': (
                'This is an important '
                'test. We\'d really like '
                'this line to wrap '
                'several times, to '
                'imitate what might '
                'happen in a real '
                'program.'
            ),
            'level': 'Important'
        }
    ]
    result = todo.show_todos(todo.todos)
    lines = result.split("\n")

    assert 'test important' in lines[1]
    assert 'This is an important' in lines[1]

    assert 'todo' in lines[2]
    assert 'test. We\'d really like' in lines[2]

    assert 'this line to wrap' in lines[3]
    assert 'several times, to' in lines[4]
    assert 'imitate what might' in lines[5]
    assert 'happen in a real' in lines[6]
    assert 'program.' in lines[7]

    print "OK - todo wrap long lines"

def test_save_todo_list():
    todos_original = [
        {
            "title": "test todo",
            "description": "This is a test",
            "level": "Important"
        }
    ]
    todo.todos = todos_original
    assert "todos.pickle" not in os.listdir('.')
    
    # Test saving
    todo.save_todo_list()
    assert "todos.pickle" in os.listdir('.')

    # Test loading
    todo.load_todo_list()
    assert todo.todos == todos_original
    os.unlink("todos.pickle")

    print "OK - save todo list"

def test_todo_sort_after_creation():
    todo.todos = [
        {
            'title': 'test unimportant todo',
            'description': 'This is an unimportant test',
            'level': 'Unimportant'
        },
        {
            'title': 'test medium todo',
            'description': 'This is a test',
            'level': 'Medium'
        }
    ]
    # Create another to-do
    todo.create_todo(todo.todos, title="Make some stuff", description = "Stuff needs to be programmed", level = "Important")
    # Check to-do order
    assert todo.todos[0]['level'] == "IMPORTANT"
    assert todo.todos[1]['level'] == "Medium"
    assert todo.todos[2]['level'] == "Unimportant"

    print "OK - todo sort after creation"

def test_delete_todo():
    todo.todos = [
        {
            'title': 'test important todo',
            'description': 'This is an important test',
            'level': 'IMPORTANT'
        },
        {
            'title': 'test medium todo',
            'description': 'This is a test',
            'level': 'Medium'
        },
        {
            'title': 'test unimportant todo',
            'description': 'This is an unimportant test',
            'level': 'Unimportant'
        }
    ]

    reponse = todo.delete_todo(todo.todos, which = "2")

    assert reponse == "Deleted todo #2"
    assert len(todo.todos) == 2
    assert todo.todos[0]['level'] == 'IMPORTANT'
    assert todo.todos[1]['level'] == 'Unimportant'

    print "OK - test delete todo"


def test_delete_todo_failure():
    todo.todos = [
        {
            'title': 'test important todo',
            'description': 'This is an important test',
            'level': 'IMPORTANT'
        }
    ]

    for bad_input in ['', 'foo', '0', '43']:
        response = todo.delete_todo(todo.todos, bad_input)
        assert response == ("'" + bad_input + "' needs to be the number of a todo!")
        assert len(todo.todos) == 1

    print "OK - test delete todo failures"

def test_edit_todo():
    todo.todos = [
        {
            'title': 'make some stuff',
            'description': 'This is an important test',
            'level': 'IMPORTANT'
        }
    ]
    # Edit this todo item
    response = todo.edit_todo(todo.todos, which="1", title="", description="Stuff needs to be programmed prperly", level="")

    assert response == "Edited todo #1", response
    assert todo.todos[0]['title'] == "make some stuff"
    assert todo.todos[0]['description'] == "Stuff needs to be programmed prperly"
    assert todo.todos[0]['level'] == "IMPORTANT"

    print "OK - edit todo"

def test_edit_importance():
    todo.todos = [
        {
            'title': 'djkajs owjo',
            'description': 'This is an medium test',
            'level': 'Medium'
        },
        {
            'title': 'Test another medium todo',
            'description': 'This is another medium test',
            'level': 'Medium'
        }
    ]
    # Edit the second todo item's importance
    response = todo.edit_todo(todo.todos, which="2", title="", description="", level="Important")

    assert todo.todos[0]['level'] == "IMPORTANT"
    assert todo.todos[1]['level'] == "Medium"

    print "OK - edit importance"

# Run test
test_create_todo()
test_get_function()
test_get_fields()
test_run_command()
test_show_todos()
test_todo_sort_order()
test_todo_wrap_long_lines()
test_save_todo_list()
test_todo_sort_after_creation()
test_delete_todo()
test_delete_todo_failure()
test_edit_todo()
test_edit_importance()