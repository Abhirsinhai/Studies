#Traditional Approach
import random #Import random so we can create a random number

my_list = [] #Create a list to store random numbers
for i in range(10): #Create a list to append random numbers
    my_list.append(random.randint(1, 100)) #Append the random numbers with randint function
print(my_list) #Print out my_list after adding all the random numbers

#List Comprehension
res = random.sample(range(1, 100), 10) #Create a list and add 10 random numbers
print(my_list) #print out my_list after adding all the random numbers