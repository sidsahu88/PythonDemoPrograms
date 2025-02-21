start = False

while True:
    command = input('command> ').lower()

    if command == 'help':
        print('''start -> to start the car.\nstop -> to stop the car.\nquit -> to quit the game.''')
    elif command == 'start':
        if start:
            print('Car is already started!')
        else:
            print('Car started...Ready to go!')
            start = True
    elif command == 'stop':
        if not start:
            print('Car is already stopped!')
        else:
            print('Car stopped!')
            start = False
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")
