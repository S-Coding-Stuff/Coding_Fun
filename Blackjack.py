import sys, random

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'

def main():
    print()
    print('BLACKJACK')
    print()
    print('''Rules: 
    Try to get as close to 21 without going over.
    Kings, Queens and Jacks are worth 10.
    Aces are worth 1 or 11.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to top taking cards.
    On your first play you can (D)ouble down to increase your bet, but must
    hit exactly one more time before standing.
    If there's a tie the bet is returned to the player.
    The dealer stops hitting at 17.''')

    money = 5000
    # Main game loop
    while True:
        if money <= 0:
            print("You're broke!")
            print("Thanks for playing!")
            sys.exit()
        
        print('Balance: ', money)
        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print('Bet: ', bet)
        while True: # Will continue to loop until player stands or busts
            displayHands(playerHand, dealerHand, False)
            print()

            # Check if player has bust
            if getHandValue(playerHand) > 21:
                break

            move = getMove(playerHand, money - bet) # Get the player's move


            if move == 'D':
                additionalBet = bet
                #additionalBet = getBet(min(bet, money - bet))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)
                input('Press Enter to Continue...')
                print('\n\n')

            # The above will play out followed by the next bit of code
            # The above doubles the bet, below takes another card IF it doubles down or hits
            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)
                

                if getHandValue(playerHand) > 21:
                    # Player has busted
                    continue
                
            # Stand / doubling down stops the player's turn
            if move in ('S', 'D'):
                break 

        # Handling the dealer's actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('The DEALER hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                input('Press Enter to Continue...')
                print('\n\n')

                if getHandValue(dealerHand) > 21:
                    break # Dealer has bust

            # Showing the final hands
            displayHands(playerHand, dealerHand, True)
            # Final hand values
            playerValue = getHandValue(playerHand)
            dealerValue = getHandValue(dealerHand)

            # Win / Lose conditions
            if dealerValue > 21:
                print('DEALER busts! You win ${}'.format(bet))
                money += bet
            elif (playerValue > 21) or (playerValue < dealerValue):
                print('You lost!')
                money -= bet
            elif playerValue > dealerValue :
                print('You win!') 
                money += bet
            elif playerValue == dealerValue :
                print("It's a tie! The bet is returned to you.")

            input('Press Enter to Continue...')
            print('\n\n')


def getBet(maxBet):
    while True:
        print('How much do you wanna bet? (1 - {} or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if (bet == 'QUIT'):
            print('Thanks for playing!')
            sys.exit()
        if not bet.isdecimal():
            continue # If player didn't enter a number ask again

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # Player entered a valid bet
        else:
            print('Not a valid amount!')
        
# Will return (rank, suit) tuples for all cards
def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # Add numbered cards
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) # Add face and ace cards
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Dealer: ???')
        displayCards([BACKSIDE] + dealerHand[1:])

    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)



# Will return the hand value of the specified person i.e. the player or dealer
def getHandValue(cards):
    value = 0
    numberOfAces = 0

    # Adds up the value for non-ace cards
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank)
    # Adds the value of the ace cards
    value += numberOfAces

    # If value + ace < 21, the ace will instead go to +11 value
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value

def displayCards(cards):
    rows = ['', '', '', '', ''] # Text to display on each row

    for i, card in enumerate(cards):
        rows[0] += ' ___ ' # Top line of the card
        if card == BACKSIDE:
            # Print back of card
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '| ##|'
        else:
            # Print front of card
            rank, suit = card # Card is a tuple data structure
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)

# Ask player for their move and return H, S or D (listed below)
def getMove(playerHand, money):
    while True: # Keep looping until a correct move is entered
        moves = ['(H)it', '(S)tand']
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble Down')

        # Get the player's move
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D':
            return move
        
# If the program is run instead of imported, then run the game
if __name__ == '__main__':
    main()