import random
import time
#Named Constants 
HORSE1= "HORSE1"
HORSE2= "HORSE2"
HORSE3= "HORSE3"
HORSE4= "HORSE4"
HORSE5= "HORSE5"
HORSE6= "HORSE6"
#variables that will change within different functions
chips=15
choice=0

#Menu function 1)General: menu is the main control menu for the program, it passes control between betting options
#2)Preconditions:  The menu will only accept choices 1-4, and uses loops to reprompt user for a different choice
#3)Postconditions: Menu transfers the chip balance into and out, and shifts control from the main menu to the other betting functions

def menu():
    choice=0
    chips=15
    again=1
    
    while choice!=1 or choice!=2 or choice!=3 or choice!=4 or choice!=5 or chips<1 or chips>25:
        print("Chip Balance:  ", chips)
        print("1 for 1st place bet")
        print("2 for place bet, 1st or 2nd")
        print("3 for show bet, 1st, 2nd, or 3rd")
        print("4 for 1st and 2nd parlay")
        print("5 for help/questions")
        try:
    
            choice=int(input("Enter a the corresponding menu number to select your bet:\t"))
        except:
            print("please enter a number 1-5")
        else:
            if choice==1:
                chips=firstplace(chips)
            elif choice==2:
                chips=place(chips)
            elif choice==3:
                chips=show(chips)
            elif choice==4:
                chips=parlay(chips)
            elif choice==5:
                read=0
                whatsthis(read)
            else:
                print("Error")

        #play again needs work        
       # try:
           # again=input("Play again? Yes or No")
           # if 'y' or 'Y' in again:
            #    again=1
            #else:
              #  again=0
              #  break
        #except:
           # print("type yes or no")
#horsechoice 1)General: The horsechoice functions allows the user to select a horse from the list that is printed in the screen before
#2)Preconditions: to access this screen, you must have already made a bet function, and have seen the horse list
#3)Postconditions: this functions forces the user to pick a selected horse, prints the horse value, and returns to selection to the betting function
                
def horsechoice():
    selectHorse=0
    while selectHorse < 1 or selectHorse > 6:
        try:
            selectHorse=int(input("Which of these winning horses do you want to bet on.\t\t"))
        except:
            selectHorse=0
            print("Pick a Horse with numbers 1-6!")
        
    return selectHorse
#chipchoice 1)General: This is the function where you select the amount you wish to bet given your desired function
#2)Preconditions: must have chips, made horsechoice, to enter this function, if you have less than 3 chips, you are prompted to bet 1 to your total amount vs 1 to 3
#3)Postconditions: Prompts user to select amount for bet, checks the input to verify it is appropriate type and value, then sends the chipBet back to the function

def chipchoice(chips):
    print("You have ", chips," to bet")
    chipBet=0
    if chips>3:
        while chipBet<1 or chipBet>3:
            try:
                chipBet=int(input("How many chips would you like to bet? MAX of 3\t\t\t"))
            except:
                print("Please Pick a Number between 1 and 3")
    else:
       while chipBet<1 or chipBet>chips:
            try:
                chipBet=int(input("How many chips would you like to bet? MAX of ", chips,"\t\t\t"))
            except:
                print("Please Pick a Number between 1 and ",chips)
    return chipBet
#horsechoiceparlay 1)General: this function only is displayed in the parlay betting option, it prompts user for horse choice, and compares it to other selected horse
#2)Preconditions: imports the previous selection from horsechoice module, prompts user to enter other horse number, and checks vs all numbers and previous selected
#3)Postconditions:input is double verified for type and value, then returned to parlay function

def horsechoiceparlay(selectHorse):  
    selectHorse2=0
    while selectHorse2<1 or selectHorse2>6 or selectHorse2==selectHorse:
        try:
            selectHorse2=int(input("Which horse would you like to bet finishes 2nd?\t\t\t"))
        except:
            print("Pick a number of the Horse for 2nd Place.")
        if selectHorse2==selectHorse:
            print("Choose a different Horse from your first place choice")
            selectHorse2=0
    return selectHorse2
    
#horselist 1) General: This is a print list of horses, no data collected or processed
#2)Preconditions: N/A
#3)Postconditions: just prints list onto screen
def horselist():
    print("1 for ",HORSE1)
    print("2 for ",HORSE2)
    print("3 for ",HORSE3)
    print("4 for ",HORSE4)
    print("5 for ",HORSE5)
    print("6 for ",HORSE6)

#search: 1) this searches the shuffled list for your selected horse
#2) Preconditions: must import horse choice and horse shuffled list
#3)Postconditions: does logic check, and returns place value
def search(horses, selectHorse):
    if selectHorse == 1:
        place=(horses.index(HORSE1)+1)
    elif selectHorse == 2:
        place=(horses.index(HORSE2)+1)
    elif selectHorse == 3:
        place=(horses.index(HORSE3)+1)
    elif selectHorse == 4:
        place=(horses.index(HORSE4)+1)
    elif selectHorse == 5:
        place=(horses.index(HORSE5)+1)
    elif selectHorse == 6:
        place=(horses.indes(HORSE6)+1)
    else:
        print("Error")
    print("Your horses place:\t", place, end='')
    if place==1:
        print("st")
    elif place==2:
        print("nd")
    elif place==3:
        print("nd")
    else:
        print("th")
    return place
        
#poniesrun 1) General: This is the most important part, this takes the horse list, and shuffles it
#2 Preconditions: no imports, must have good sense of patience and humor
#3Postconditions: shuffles list then returns the shuffled list to the betting module for processing
def poniesrun():
    
    horses= [HORSE1, HORSE2, HORSE3, HORSE4, HORSE5, HORSE6]
    random.shuffle(horses)  #https://pynative.com/python-random-shuffle/
    print("\tHere goes the fastest 2 minutes in all of sports!")
    print("\t\t\tAnd they are off!")
    time.sleep(5)            #https://www.cyberciti.biz/faq/python-sleep-command-syntax-example/
    print("\t\tThey are around the first corner")
    time.sleep(5)
    print("\t\t Now into the back straight away")
    time.sleep(8)
    print("\t\t\tInto the final bend...")
    time.sleep(5)
    print("And there we have it folks, Congrats to", horses[0])
    print("Results")
    for n in horses:
        print(n)
    return horses
#firstplace 1)General: This function manages the first place betting option, recieves a variety of information, including chips, chipBet, horses, etc
#2) Preconditions: recieves the chip total from menu function, and recieves various returns from the variety of functions
#3)Postconditions: manages horse choices, chips wagered, place finding, and determines if the bet was a winning one
            
def firstplace(chips):
    print("First Place Bet")
    horselist()
    selectHorse = horsechoice()
    print("Horse ", selectHorse)
    chipBet = chipchoice(chips)
    print("Chips Wagered ", chipBet)
    horses = poniesrun()
    place=search(horses, selectHorse)
    print(place)
    if place == 1:
        print("WIN")
        multiplier=5
        chips= winmodifier(chips, chipBet, multiplier)
        
    else:
        print("Lose")
        chips=chips-chipBet
        
    return chips
    
    
#parlay 1)General: This function manages the parlay betting option, recieves a variety of information, including chips, chipBet, horses, etc
#2) Preconditions: recieves the chip total from menu function, and recieves various returns from the variety of functions, must get second horse choice
#3)Postconditions: manages horse choices, chips wagered, place finding, and determines if the bet was a winning one    
    
def parlay(chips):
    print("Parlay")
    horselist()
    selectHorse = horsechoice()
    selectHorse2 = horsechoiceparlay(selectHorse)
    print("Parlay Bet ", selectHorse, " for 1st place and ", selectHorse2," for 2nd")
    chipBet = chipchoice(chips)
    print("Chips Wagered ", chipBet)
    horses=poniesrun()
    place=search(horses,selectHorse)
    print("&")
    place2=search(horses,selectHorse2)
    if place == 1 and place2 == 2:
        print("Congrats")
        multiplier=15
        chips= winmodifier(chips, chipBet, multiplier)
        
    else:
        print("Lose")
        chips=chips-chipBet
      
    return chips
        
#place 1)General: This function manages the place betting option, recieves a variety of information, including chips, chipBet, horses, etc
#2) Preconditions: recieves the chip total from menu function, and recieves various returns from the variety of functions
#3)Postconditions: manages horse choices, chips wagered, place finding, and determines if the bet was a winning one    
    
def place(chips):
    print("Place Bet")
    horselist()
    selectHorse = horsechoice()
    print("Horse ", selectHorse)
    chipBet = chipchoice(chips)
    print("Chips Wagered ", chipBet)
    horses=poniesrun()
    place=search(horses,selectHorse)
    print(place)
    if place == 2 or place == 1:
        print("WIN")
        multiplier = 3
        chips=winmodifier(chips, chipBet, multiplier)
        
    else:
        print("Lose")
        chips=chips-chipBet
        
    return chips

#showplace 1)General: This function manages the show betting option, recieves a variety of information, including chips, chipBet, horses, etc
#2) Preconditions: recieves the chip total from menu function, and recieves various returns from the variety of functions
#3)Postconditions: manages horse choices, chips wagered, place finding, and determines if the bet was a winning one
def show(chips):
    print("Show Bet")
    horselist()
    selectHorse = horsechoice()
    print("Horse ", selectHorse)
    chipBet = chipchoice(chips)
    print("Chips Wagered ",chipBet)
    horses=poniesrun()
    place=search(horses,selectHorse)
    print(place)
    if place==1 or place==2 or place==3:
        print("WIN")
        multiplier = 2
        chips=winmodifier(chips, chipBet, multiplier)
        
    else:
        print("Lose")
        chips=chips-chipBet
        
    choice=0
    return chips, choice

#winmodifier 1)General: this funtion handles the winning modifications to the total chip totals
#2) Preconditions: This is accessed by being a winner in your betting function, must import chips from the menu and the individual bet function
#3) Postconditions: this modifies the total chip count, and returns the value back to the bet, and then back to menu in preparation for another loop iteration
def winmodifier(chips, chipBet, multiplier):
    chips=chips+chipBet+(chipBet*multiplier)
    return chips
#whatsthis 1)General:this is an overview of the game for those who would like it, prints on screen, returns nothing
#2) Preconditions: imports a 'n' for read variable to initiate while loop
#3)Postconditions: This menue provides overview of the game, and then prompts the user to return to the main menu to play the game
def whatsthis(read):

    while read!=1:
        print("Welcome to the Pony Run gambling game")
        print("Be prepared for the only gambling game geared for elementary students")
        print("The game is relatively simple. The computer will prompt you for a type of bet,")
        print("You will then be given the option to pick which horse(s) you would like to bet on.")
        print("Finally you will be asked how much you would like to wager.")
        print("Then the excitement begins as we open the gates and let our 8 bit horses")
        print("and they race around a purely imaginary race track.")
        print("After they finish, we let you know how they finished, and if you were a winner")
        print("or loser.  You can then chose to play again, and lets be honest, you will.")
        print("you are allowed to keep placing bets until you go bankrupt or get 25 chips!")
        print("Just be aware that if you cannot pay your chips, you will be taken to clean out")
        print("the horse stalls.  So GOOD LUCK we know you will have a fantastic experience!")
        try:
            read=int(input("\n\nDid you get all that? 1 for back to menu, 0 for no.\t\t"))
            if read!=1:
                print("Appearantly you didn't understand the directions\n\n")

            else:
                break
        except:
            print("Appearantly you didn't understand the first time")

      

menu()                   
