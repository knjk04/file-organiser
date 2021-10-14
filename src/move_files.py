import os


class Move:
    def __init__(self):
        self.recursive = False
        self.extension = ''
        self.with_extension = True
        self.src = os.getcwd()
        self.to = os.getcwd()


def display_options():
    print(
        '''\nMove | Options:
            -e or --extension: move all files with the specified file type
            -we or --without-extension: move all the files without the specified file type
        '''
    )


def apply_recursively():
    question = 'Do you want to apply this operation to all sub-folders (y/n)?'
    print(question)
    while True:
        answer = input().lower()
        if answer == 'y' or answer == 'n':
            break
        elif answer.isalpha():
            print("Please enter 'y' or 'n'. Numbers are not accepted")
            print(question)
        else:
            print("Please enter 'y' or 'n'")
            print(question)
    return answer == 'y'


def move_from():
    print("Enter the absolute path to the source folder of the files"
          " (press enter if it's the current directory)")


def get_file_ext():
    print('Enter in the file extension:')
    ext = input()
    if not ext.startswith('.'):
        ext = '.' + ext
    return ext


def run():
    display_options()
    print('Move | Which option do you want?')

    state = Move()
    option = input()
    if option == '--extension' or option == '-e':
        state.with_extension = True
    elif option == '--without-extension' or option == '-we':
        state.with_extension = False
    else:
        # TODO: loop back.
        print('Invalid option. Please try again.')
        raise NotImplementedError
    state.extension = get_file_ext()

    
    # TODO: navigate back to home when done
