#What we wan't our input prompt to say
prompt = "\nTell me something and I'll repeat it!: "

#Used to keep the script alive
active = True
while active:
    message = input(prompt)

    #Used to kill the script
    if message == 'quit':
        active = False
    
    #Will repeat itself unless told to quit
    else:
        print(message)