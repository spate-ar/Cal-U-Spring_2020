JOE = "Joe's Gormet Burgers\n"
MAINSTREET = "Main Street Pizza Company\n"
CORNERCAFE = "Corner Cafe\n"
MAMAS = "Mama's Fine Italian\n"
CHEFS = "The Chef's Kitchen\n"
print("Input yes or no")
condition1 = input("Is anyone in your party a vegetarian?  ")
condition2 = input("Is anyone in your party a vegan?  ")
condition3 = input("Is anyone in your pary gluten-free?  ")

if condition1 == 'yes' and condition2 =='yes' and condition3 =='yes':
    print("Great, your restaurant choices are:\n, ", CORNERCAFE, CHEFS)
elif condition1 == 'yes' and condition2 == 'no' and condition3 == 'no':
    print("Great, your restaurant choices are:\n ", MAINSTREET, CORNERCAFE, MAMAS, CHEFS)
elif condition1 == 'yes' and condition2 == 'yes' and condition3 == 'no':
    print("Great, your restaurant choices are:\n ", CORNERCAFE, CHEFS)
elif condition1 == 'yes' and condition2 == 'no' and condition3 == 'yes':
    print("Great, your restaurant choices are:\n ", MAINSTREET, CORNERCAFE, CHEFS)
elif condition1 == 'no' and condition2 == 'yes' and condition3 == 'yes':
    print("Great, your restaurant choices are:\n ", CORNERCAFE, CHEFS)
elif condition1 == 'no' and condition2 == 'yes' and condition3 == 'no':
    print("Great, your restaurant choices are:\n ", CORNERCAFE, CHEFS)
elif condition1 == 'no' and condition2 == 'no' and condition3 == 'yes':
    print("Great, your restaurant choices are:\n ", MAINSTREET, CORNERCAFE, CHEFS)
else condition1 == 'no' and condition2 == 'no' and condition3 == 'no':
    print("Great, your restaurant choices are:\n ", JOE, MAINSTREET, CORNERCAFE, CHEFS)
      
print("Enjoy your meal!")
