# Exercise #1
# name1 = raw_input("What is your name?")
# name2 = raw_input("What is your partner's name?")
#
# if name1 > name2:
#     print "My name is greater!"
# elif name2 > name1:
#     print "Their name is greater."
# else:
#     print "Our names are equal!"

# Exercise #2
# date = raw_input("What is the date?")
#
# if date >= 15:
#     print "Oh, we're halfway there!"
# else:
#     print "The month is still young."

# Exercise #3
# today = raw_input("What day is it today? ")
#
# if today == "Monday":
#     print "Yaaas Monday! Here we go!"
# elif today == "Tuesday":
#     print "Sigh, it's only Tuesday."
# elif today == "Wednesday":
#     print "Humpday!"
# elif today == "Thursday":
#     print "#tbt"
# elif today == "Friday":
#     print "TGIF"
# else:
#     print "Yeah, it's the freakin' weekend!"

# Exercise #4, #5
# age = input("What is your age? "))
#
# if age >= 18 :
#     print "Yay! I can vote!"
# else :
#     print "Aww, I cannot vote."

# # Exercise #6
# age = input("What is your age? ")
#
# if age >= 21:
#     print "I can vote and go to a bar!"

# Exercise #7
# age = input("What is your age? ")
#
# if age >= 21:
#     print "I can go to a bar."
# elif age >= 18:
#     print "I can vote, but I cannot go to a bar."
# else :
#     print "I cannot vote or go to a bar."
#
# # # Exercise #8
# number = input("Enter a number.")
#
# if number % 2 == 0:
#     print "The number is even."
# else:
#     print "The number is odd."

# # # Exercise #9
# number = input("Enter a number. ")
#
# if number % 2 != 0:
#     print "The number is odd."
# else:
#     print "The number is even."


 # Exercise #10
# num1 = input("Enter a number. ")
# num2 = input("Enter another number. ")
#
# if num1 % 2 == 0 and num2 % 2 == 0:
#     print "Both numbers are even."
# else:
#     print "Both numbers are not even."

 # Exercise #11
# num1 = input("Enter a number. ")
# num2 = input("Enter another number. ")
#
# if num1 % 2 == 0 and num2 % 2 == 0:
#     print "Both numbers are even."
# elif num1 % 2 == 0 and num2 % 2 != 0:
#     print "%i is even AND %i is odd." % (num1, num2)
# elif num1 % 2 != 0 and num2 % 2 == 0:
#     print "%i is odd AND %i is even." % (num1, num2)
# else:
#     print "Both numbers are odd."

# Exercise #12, #13
color = raw_input("What is your favorite color? ")

if color == ("blue" or "red" or "yellow"):
    print "My favorite color is a primary color!"
else:
    print "My favorite color is a secondary color."
