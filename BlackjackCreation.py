import random

def deal_cards():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 # 4 of each number in each deck of cards
    random.shuffle(deck)
    player_cards = [deck.pop(), deck.pop()] #this allows for the game to automatically deal 2 cards to each the player and the dealer
    dealer_cards = [deck.pop(), deck.pop()]
    return player_cards, dealer_cards#This reads of the cards that the dealer and the player recieved

def score(hand):
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11) #this allows for the game to change the Ace from an 11 to a 1 if the players scores is over 21
        hand.append(1)
    return sum(hand)

print("Welcome to my game of Blackjack!\n")
player_money = int(input("How much money would you like to start with? ")) #implemented an input where users can input whatever amount of money they would like to bet with
while player_money >= 0:
    print("\nYou currently have $" + str(player_money) + ".")
    user_bet = int(input("How much would you like to bet? "))
    if player_money == 0 and user_bet == 0: #I could not get this part to work, but this was designed to not let the user proceed unless they entered $1 or more.
        print("I'm sorry, please enter at least $1 to bet with.")#use this for the toughest part of the assignment
    print()
    player_hand, dealer_hand = deal_cards()
    player_score = score(player_hand)
    dealer_score = score(dealer_hand)
    print("Your cards: {} (total = {})".format(player_hand, player_score))
    print("Dealer's cards: {}".format(dealer_hand[0]))
    if player_score == 21:
        print("Blackjack! You win! Woohoo!\n")
        player_money += user_bet
    else:
        while True:
            hitstand = input("Would you like to hit or stand? ")#the program shows the user the current number they are at
            #this allows for the user to either hit to draw another card, or stand and let the dealer draw another card
            if hitstand.lower() == "hit":
                player_hand.append(deal_cards()[0][0])#This allows for the user to hit, which means to draw another card if they are under the number 21.
                player_score = score(player_hand)
                print("\nYour cards: {} (total = {})".format(player_hand, player_score))
                if player_score > 21:
                    print("Haha! You Bust! You lose!:(((\n")
                    player_money -= user_bet
                    break
            elif hitstand.lower() == "stand": #This allows the player to stand, which means that they are happy with their current number.
                while score(dealer_hand) < 17:
                    dealer_hand.append(deal_cards()[0][0])
                    dealer_score = score(dealer_hand)
                print("\nDealer's cards: " + str(dealer_hand) + " (total = " + str(dealer_score) + ")")

                if dealer_score > 21:
                    print("Dealer busts! You win! Woohoo!\n")#this shows that when the dealer goes over 21, the user wins!
                    player_money += user_bet
                    break
                elif dealer_score > player_score:
                    print("Dealer wins! Keep trying!\n")#This is when the dealer beats the player by havign a larger score.
                    player_money -= user_bet
                    break
                elif dealer_score < player_score:
                    print("You win! Woohoo!\n") #This elif statement shows that the user has beaten the dealer with a bigger score!
                    player_money += user_bet
                    break
                else:
                    print("Push! Beat the dealer next time!\n")# The user and the dealer got the same score, this prints that no one lost any money.
                    break
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")#This is when the user did not enter the words hit or stand.
    if player_money == 0:
        print("You're out of money! Exit the program and try again!")#I could not get the program to completely stop when the user inputted 'no'.
    else:
        play_again = input("Would you like to play again? (yes/no) ")
        if play_again.lower() == "no":
            print("Thank you for playing my game of blackjack! Your final winnings/losses: $" + str(player_money))#this prints the total amount of money the player had either won or lost.
        if play_again.lower() == "yes" and player_money == 0:
            print("Please deposit more money before you bet on another hand.")#I could not get this to work, but it would have allows the user to deposit more money
            #before playing another hand.
            break
