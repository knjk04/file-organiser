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


def run():
    display_options()
    print('Move | Which option do you want?')

    option = input()
    if option == '--extension' or option == '-e':
        raise NotImplemented
    elif option == '--without-extension' or option == '-we':
        raise NotImplemented
    else:
        print('Invalid option. Please try again.')
