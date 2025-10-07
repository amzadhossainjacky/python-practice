#example of string data type
""" name = "Md. Amzad Hossain Jacky"
print(f"value: {name}, name is of type:", type(name)) """

#slice of string
""" skill = "Python Programming"
print(skill[0:6]) #Python
print(skill[2:])    #thon Programming
print(skill[0:2]) #Py
print(skill[-1:-3]) #none
print(skill[-5:-1]) """

#modify string 
#upper case
name = "   Hello, World"
""" print(name.upper())

#Lower case
print(name.lower())

#title case
print(name.title())

#remove whitespace
print(name.strip())

#replace 
print(name.replace("H", "j")) """

#split
""" print(name.split(",")) # returns [' Hello', ' World!'] """

#concatenate
""" first_name = "Md. Amzad Hossain"
last_name = "Jacky"
print("Full Name:", first_name + " " + last_name) """

#formated string
age = 29
height = 5.7
print(f"My name is Md. Amzad Hossain Jacky. I am {age} years old and my height is {height} feet.")

