usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username: ")

for i in range(0, len(usernames)+1):
    if usernames[i] == username:
        print("Access denied")
        break
    else:
        print("Access granted")
        break