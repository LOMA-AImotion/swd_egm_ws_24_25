# grader
exam_points = 70
achieved_points = int(input("How many points did you get?"))

perc = achieved_points / exam_points

# This would not work
# if perc > 0.5:
#     print("You passed")
# elif perc > 0.7:
#     print("3,0")
# elif perc > 0.8:
#     print("2,0")
# elif perc > 0.95:
#     print("1,0")
# else: 
#     print("You did not pass")

if perc > 0.95:
    print("1,0")
elif perc > 0.8:
    print("2,0")
elif perc > 0.7:
    print("3,0")
elif perc > 0.6:
    print("4,0")
elif perc > 0.5:
    print("You passed")
else: 
    print("You did not pass")

if perc < 0.5:
    print("You did not pass")
elif perc <= 0.6:
    print("5,0")
elif perc <= 0.7:
    print("4,0")
elif perc <= 0.8: 
    print("3,0") 
elif perc <= 0.95:
    print("2,0")
else: 
    print("1,0")
