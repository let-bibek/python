#guessing game
exact=48
guess=1
number=int(input ("guess a number :\n"))
game_over=False
while not game_over:
    if(number==exact):
        print(f"you win in {guess} times.")
        game_over=True
    else:
        if(number<exact):
            print("the numbber is lower.\n")
           number= input("enter the number again\n")
           number=int(number)
           guess=guess+1
        else:
            print("high number.")  
            number=int(input("Enter again\n"))
            guess=guess+1 