from time import sleep

while 1:
    userInput = input('Enter 1, 2 or 3: ')
    
    if userInput == '1':
        print ('Hello World')
        print ("How are you?")
    elif userInput == '2':
        print ('Python Rocks!')
        print ("I love Python")
    elif userInput == '3':
        print ("That's all folks!")
        break
    else:
        print ('You did not enter a valid number')
    sleep(2)
    print (10 * "\n")