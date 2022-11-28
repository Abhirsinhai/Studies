#Using temp variable
var1 = 1
var2 = 2
temp = 0

temp = var2
var2 = var1
var1 = temp
print("Variable 1:", var1, "Variable 2:", var2)

#Not using temp variable
var1, var2 = var2, var1
print("Variable 1:", var1, "Variable 2:", var2)