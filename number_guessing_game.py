import random
print("Welcome to the Number Guessing Game!")
print("\nI am thinking of a number between 1 and 100\n")
diff=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if diff=='easy':
    num_of_guess=10
else:
    num_of_guess=5
def guess_game(m):
    num=random.randrange(1,101)
    Flag=0
    while m>0:
        guess=int(input(f"You have {m} attempts left.\nMake a guess: "))
        if num>guess:
            print("Too Low!\n Guess Again!")
            m-=1
        elif num<guess:
            print("Too High!\n Guess Again!")
            m-=1
        else:
            print(f"You Got it! The number is {num}")
            m=0
            Flag=1
            return
    if Flag==1:
        print("You have run out of chances! Refresh the page to try again!")

go_again=True

while go_again:
    guess_game(num_of_guess)
    try_again=input("Do you want play another round? y or n: ").lower()
    if try_again=='n':
        go_again=False
           
