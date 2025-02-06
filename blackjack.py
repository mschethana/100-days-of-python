import random
def blackjack():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    player_card=[]
    computer_card=[]
    cont=input("Do you want to play the game of blackjack: 'y' or 'n'? ").lower()
    next_go=True
    if cont=='n':
        next_go=False
        return()
    else:
        for i in range(1,3):
            w=random.choice(cards)
            computer_card.append(w)
            cards.remove(w)
        print(f"The faceup card of computer is {computer_card[0]}")
        for i in range(1,3):
            w=random.choice(cards)
            player_card.append(w)
            cards.remove(w)
        print(f"The player cards are {player_card} with sum {sum(player_card)}")
        while next_go:
            if sum(player_card)>21:
                print(f"You went over -- You Lose!")
                blackjack()
            else:
                cont1=input("Type 'y' to hit another card and 'n' to stand: ")
                if cont1=='y':
                    w=random.choice(cards)
                    player_card.append(w)
                    cards.remove(w)
                    print(f"The current player cards are {player_card} with sum {sum(player_card)}")
                else:
                    next_go=False
        while sum(computer_card)<19:
            w=random.choice(cards)
            computer_card.append(w)
            cards.remove(w)
        if sum(computer_card)>21 or sum(computer_card)<sum(player_card):
            print(f"The final computer cards are {computer_card} with sum: {sum(computer_card)} and the final player cards are {player_card} with sum {sum(player_card)}. \nYOU WIN!!!")
        elif 22>sum(computer_card)>sum(player_card):
            print(f"The final computer cards are {computer_card} with sum: {sum(computer_card)} and the final player cards are {player_card} with sum {sum(player_card)}. \nYOU LOSE!!!")
        blackjack()    

blackjack()


