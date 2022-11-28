def prime(num, i = 2):

    if (num <= 2):
        return True if(num == 2) else False
    if (num % i == 0):
        return False
    if (num == 1):
        return True
    if (i * i > num):
        return True
 
    return prime(num, i + 1)

num = int(input("Enter a number: "))
if (prime(num)):
    print("Number is prime")
else:
    print("Number is not prime")