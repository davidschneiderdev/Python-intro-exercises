
# variable names in python have underscores
# snake_case
user_name = input("What is your name? ")

# in JavaSCript we would write username
# camelCase

# String subsitution has three parts:
# 1. A string...with placeholders
# 2. The interpolation operator
# 3. Values to interpolating into the string
#    Values should be in parens, separated by commas.
# greeting = "Hello, %s!" % (user_name,) 
# print(greeting)

# If interpolating a single value, 
# You don't need the parens or the coma.
# print("Hello,", user_name, "!")

# String concatenation combines strings.
# print("Hello, " + user_name + "!")
# print(user_name)

greeting = f"Hello, {user_name}!"
print(greeting)