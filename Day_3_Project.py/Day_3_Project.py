# ******* MINI TREASURE HUNNTING GAME USING CONDITIONAL OPERATORS *******


print("\tHey there, welcome to the treasure hunting game\t")
print("\tLet's start the game\t")
print("\n")
print("Your task is to find the treasure by choosing right way")

choice1=input("\nYou are in a cross road. Which way you want to go??? {Left / Right} : ").upper()
if choice1=='RIGHT':
    print('\nYAY, your first guess is correct. Now you reached a lake. Now you should cross the the lake')
    choice2=input('\nWould you like to wait for boat or would you like to swim??? {Wait/Swim} : ').upper()
    if choice2=='WAIT':
        print('\nHmm... Right decision. Now you reached the ISLAND. \nThere are three boxes in front of you, but you have to choose only one')
        print('\nOne made with Gold, other with Silver and final one with Bronze.')
        choice3=input('\nWhich one would you like to choose??? {Gold/Silver/Bronze} : ').upper()
        if choice3=='GOLD':
            print('\nAah! The box is filled with snakes. GAME OVER')
        elif choice3=='SILVER':
            print('\nWOOHOO, YOU FOUND THE TREASURE \n $$$YOU WON$$$')
        elif choice3=='BRONZE':
            print('\nLost one step away, really good try. Better luck next time.')

    else:
        print("\nOMG! you became food for crocodiles...GAME OVER\n")

else:
    print("\nOH NO!, This time you lost the game\n")

#NOTE: Here in every choice, I converted input into upper case letters because the user might give input in any way.
#      For example, Right can be typed in many ways like right,RIGHT,RiGhT etc. So in order to avoid error I converted everything into upper case letters.
