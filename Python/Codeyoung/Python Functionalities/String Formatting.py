#Tradition method
message = "Hello"
name = "Abhir! How are you today? I am "
mood = "okay sir."

print(message, name, mood)

#String Formatting Method
message = "Hello {name}! How are you today? I am {mood} sir."
print(message.format(name="Abhir", mood="okay"))