def CubeSum(n) :
    return (n*(n+1)//2)**2
n=int(input("enter N: "))

print("Sum of cubes of first {} natural numbers: ".format(n),CubeSum(n))