from time import sleep #Import sleep from time

message = "this message repeats over and over 50 times with a delay so i can bore you" #Message to repeat over and over

for i in range(50): #Start a for loop to repeat the message
    print(message) #Print out the message
    sleep(0.2) #After printing out the message, create a delay before repeating the message