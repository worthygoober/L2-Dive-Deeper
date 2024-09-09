# Task 1


attendees = int(input("Enter number of attendees: "))
print("large hall") if attendees > 100 else print("conference room")


# Task 2


print("reserve an audio system") if attendees > 100 else print("a projector will do")


# Task 3


food_rec = input("Would you like vegetarian food? (yes/no) ")
if food_rec == "yes":
    print("why not try Veggie Delight Caterers?")
else:
    print("give Gourmet Meals Caterers a try.")