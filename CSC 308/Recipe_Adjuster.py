#    A cookie recipe calls for the following ingredients:
#    1.5 cups of sugar
#    1 cup of butter
#    2.75 cups of flour
#    The recipe produces 48 cookies at current
#    ingredient levels.  Produce a program
#    to ask how many cookies are wanted
#    scale ingredients accordingly.


#Set Variables from problem
SETBATCH = 48
SETSUGAR = 1.5
SETBUTTER = 1
SETFLOUR = 2.75
#Find customer want
cookies = int(input('How many cookies do you want to bake today? '))
#Create IngredAdjuster Variable
IngredAdjuster = cookies/SETBATCH
#Find New Ingredient needs using IngredAdjuster
sugar = SETSUGAR * IngredAdjuster
butter = SETBUTTER * IngredAdjuster
flour = SETFLOUR * IngredAdjuster
#Display new amounts
print('Sugar:  \t', format(sugar, '.2f') , ' cups')
print('Butter:  \t', format(butter, '.2f') , ' cups')
print('Flour:  \t', format(flour, '.2f') , ' cups')
print('Good Luck Baking!')

