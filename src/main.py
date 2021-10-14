import sys
import move_files as move


def display_options():
    print(
        '''Options:
            move or m: move files
        '''
    )


# Press the green button in the gutter to run the script.
def check_if_quit():
    if option == 'quit' or option == 'q':
        print('Exiting...')
        sys.exit()


if __name__ == '__main__':
    print('*** Welcome to the file organiser! ***')
    print("Enter 'home' or 'h' to navigate back to the home")
    print("Enter 'quit' or 'q' to quit")

    display_options()
    print('Home | Which option do you want?')
    option = input()
    check_if_quit()

    if option == 'move' or option == 'm':
        move.run()
    else:
        # TODO: loop to give the user a chance to enter a valid option
        print('Invalid option')



