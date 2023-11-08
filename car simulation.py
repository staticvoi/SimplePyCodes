command_by_user =''

while command_by_user.lower() == 'quit':
    command_by_user = input("> ")
    if command_by_user.lower() == 'start':
        print("Car has started")
    elif command_by_user.lower() == 'stop':
        print("Car has stopped")
    elif command_by_user.lower() == 'quit':
        break
    elif command_by_user.lower() =='help':
        print('''
        start - to start
        stop - to stop
        quit - to quit
        ''')
    else:
        print(" I don't understand")

#lower method is repeating and DRY DONT REPEAT YOURSELF
# #convert command to lower
# while command_by_user == 'quit':
#     command_by_user = input("> ").lower()
#     if command_by_user == 'start':
#         print("Car has started")
#     elif command_by_user == 'stop':
#         print("Car has stopped")
#     elif command_by_user == 'quit':
#         break
#     elif command_by_user =='help':
#         print('''
#         start - to start
#         stop - to stop
#         quit - to quit
#         ''')
#    else:
#        print(" I don't understand")


# already in elif and while quit would break so twice same thing is there
# so use 
#while True:

# after start if again start returns it gives car has started twice but car is 
# already started
# same for stop
# should show some proper msg like its already started

started = False #first time so not started so false

while True:
    command_by_user = input("> ").lower()
    if command_by_user == 'start':
        if started: #started is true
            print("Car has already started")
        else:
            started = True
            print("Car is started")
    elif command_by_user == 'stop':
        if not started:
            print("Car has already stopped")
        else:
            started= False
            print("Car has stopped")
    elif command_by_user == 'quit':
        break
    elif command_by_user =='help':
        print('''
        start - to start
        stop - to stop
        quit - to quit
        ''')
    else:
       print(" I don't understand")

