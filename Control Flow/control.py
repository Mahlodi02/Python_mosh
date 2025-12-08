'''Comparioson Operators'''

print(10 > 3) # Greater than
print(10 < 3) # Less than
print(10 >= 3) # Greater or equal to
print(10 <= 3) # Less than or equal to
print(10 != 3) # not equal to
print(10 == 3) # equal to 
  
print(">"* 20)
# Comparioson Operators on strings
print("bag" > "apple") # True because strings has numerical presentation that computer can understand
print("bag" > "BAG")

print("^"* 20)

"""CONDITIONAL STATEMENT"""

# in programming thers's time we nned to make a decision we use if, elif and else

# if is used to make a decision
# elif is used when you want to have multiple conditions
# else is use if one of the condition is not met


temperature = 170

if temperature > 30:
    print("It's hot outside")
elif temperature < 15:
    print("It's windy")
else:
    print("It's nice")


"""TERNARY OPERATOR"""
age = 22

if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

    # you can put eevrything in one line

age = 16 
message = "Eligible" if age >= 18 else "Not eligible"

print(message)
print("#" * 20)
"""LOGICAL OPERATOR"""

# In python we have three logical operators (and, or, not).

# and is used when both conditions are True
# or is used when one of the condition is True
# not is used when the condition is false


# high_income = True
# good_credit = True
# student = False

# if high_income and good_credit and not student:
#     print("Eligible")
# else:
#     print("Not eligible")

high_income = False
good_credit = True
student = False

if high_income or good_credit and not student:
    print("Eligible")
else:
    print("Not eligible")

print("#" * 20)

"""SHORT CIRCUIT EVALUATION"""

high_income = True
good_credit = True
student = False

if high_income and good_credit and not student:
    print("Eligible")
else:
    print("not eligible")

# here python interpreter will check if the first condition is true and if its true it will continue to check whether the next one is also true and if all condintions are true it will print true

# if one of the conditions is false python interpreter stop and return false 


"""CHAINING COMPARISON OPERATOR"""

age = 21

if age >= 18 and age < 65:
    print("you can vote")
else:
    print("you are to young to vote")


# instead of this you can write your code like this


if 18 <= age < 65:
    print("you can vote")
else:
    print("you are too young to vote")



"""FOR LOOPS"""
# Instead of repeating one thing multiple times we use loops to create repetition
# lets print attempt 3 times 
# without saying print("Attempt") three times

for number in range(3):
    print("Attempt")

for number in range(3):
    print(number * ".")

for number in range(1, 10, 2):
    print(number, number * ".")


"""FOR...ELSE"""

# Now let's say we want to jump out of a loop

successful = False

for number in range(3):
    print("Attempt")
    if successful:
        print("Done")
        break
else:
    print("Attempted 3 times and failed")


"""NESTED LOOPS"""

for x in range(5):
    for y in range(3):
        print(f"{x}, {y}")

# python interpreter will start by interpreting the outer loop which initial will be 0, and then go to the inner loop and iterate it 3 times 
# and go back to outer loop and which is now 1 and goes to inner loop again and interate it 3 times


"""ITERABLE"""
# let's chack what range function returns

print(type(5))
print(type(range(5)))
# In python we have primitive type, like numbers, boolen, strings and complex numbers
# range is one of a complex number , range object is iterable you can iterate over it and use it in a loop


"""WHILE LOOPS"""

#Is use to repeat something as long that condition is true

number = 100
while number > 0:
    print(number)
    number //= 2


"""INFINITE LOOPS"""

# Is a loop that runs forever, Infinite loop you don't need to initialize command to empty string

while True:
    command = input(">")
    print("Echo", command)
    if command.lower == "quit":
        break