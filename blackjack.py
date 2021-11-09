import random
import time
cards = ['2 of Spades','3 of Spades','4 of Spades','5 of Spades',
'6 of Spades','7 of Spades','8 of Spades','9 of Spades','10 of Spades',
'King of Spades','Queen of Spades','Ace of Spades',
'Jack of Spades','2 of Clubs','3 of Clubs','4 of Clubs','5 of Clubs',
'6 of Clubs','7 of Clubs', '8 of Clubs','9 of Clubs','10 of Clubs',
'King of Clubs', 'Queen of Clubs','Jack of Clubs', 'Ace of Clubs',
'2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts,','6 of Hearts',
'7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'King of Hearts',
'Queen of Hearts', 'Jack of Hearts', 'Ace of Hearts', '2 of Diamonds',
'3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds',
'7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds',
'King of Diamonds', 'Queen of Diamonds', 'Ace of Diamonds', 'Jack of Diamonds']
plyrpts = 0

def ace_check():
    global plyrpts
    get_input = input("Your card is an Ace. Do you want it's value to be 1 or 11?")
    try:
        if int(get_input) == 1:
            plyrpts += 1
        elif int(get_input) == 11:
            plyrpts += 11
    except:
        if int(get_input) != 11 or 1 and plyrpts <= 10:
            print("You either did not input anything or inputted a value that was neither 1 nor 11. Since your points are less than 11, we set your ace's value to 11 points.")
            plyrpts += 11
        else:
            plyrpts += 1

def blackjack():
    random.shuffle(cards)


    global plyrpts
    plyrbal = 100
    plyrhand = []
    dlrpts = 0
    dlrbal = 500
    dlrhand = []
    pot = 0
    Bust = False
    dlrBust = False
    gamble = True
    while(plyrbal > 0 and gamble == True):
        wager = input("How many chips are ya' puttin' on the table buckaroo?")
        wager = int(wager)
        while(wager > plyrbal):
            print("Woah! Slow your roll, pardner! You can't go wagering more than what you got in your pocket.")
            wager = input("How many chips are ya' puttin' on the table buckaroo?")
            wager = int(wager)
        if(wager < plyrbal):
            plyrbal -= wager
            pot += wager
            print("Now that's what I like to see, hombre.\nPuttin' %s chips on the table!" % (wager))
        else:
            print("Going all in?! Yeehaw! You sure are a confident one, pardner.\nAdding %s chips to the pot." % (wager))
            wager = plyrbal
            plyrbal -= wager
            pot += wager
        #give player their first two cards
        print("Shufflin' Cards...")
        time.sleep(1)
        for i in range(2):
            plyrhand.append(cards[0])
            cards.pop(0)
                #check value of card
        for i in range(0,len(plyrhand)):
            str_plyrpts = (plyrhand[i])
            str_plyrpts = str_plyrpts[0]
            if str_plyrpts.startswith('A'):
                ace_check()
            elif not str_plyrpts.startswith(('Q', 'K', 'J', 'A', '1')):
                plyrpts += int(str_plyrpts)
            else:
                plyrpts += 10

        #dealer
        while (dlrpts < 17):
            for line in cards[:1]:
                if line.startswith('Ace') and dlrpts <= 10:
                    dlrpts += 11
                elif line.startswith('Ace') and dlrpts > 10:
                    dlrpts += 1
                elif not line.startswith(('K', 'Q', 'J', 'A', '1')):
                    str_dlrpts = str(cards[:1])
                    str_dlrpts = str_dlrpts[2:4]
                    dlrpts += int(str_dlrpts)
                else:
                    dlrpts += 10
                dlrhand.append(cards[0])
                cards.pop(0)
        print("Dealer's up card is %s" % (dlrhand[1]))
        time.sleep(1)
        if dlrpts > 21:
            print("Dealer busted!")
            dlrBust = True
        #stand or hit?
        time.sleep(1)
        while(plyrpts < 21 and dlrBust == False):
            next_move = input("your hand is %s, your points are %s. would you like to stand or hit? " % (plyrhand, plyrpts))
            next_move = next_move.lower()
            if next_move.startswith("hit"):
                plyrhand.append(cards[0])
                cards.pop(0)
                time.sleep(1)
                print("Your drew a %s" % (plyrhand[-1]))
                if plyrhand[-1].startswith('A'):
                    ace_check()
                elif not plyrhand[-1].startswith(('Q', 'K', 'J', 'A', '1')):
                    str_plyrpts = str(plyrhand[-1])
                    str_plyrpts = str_plyrpts[0]
                    plyrpts += int(str_plyrpts)
                else:
                    plyrpts += 10
            if next_move.startswith("stand"):
                break
            if(plyrpts > 21):
                print("You bust!")
                Bust = True
                #pay-out dealer
        #stand():
        if(plyrpts < dlrpts and dlrBust == False or Bust == True and dlrBust == False):
            print("You lose!\nThe dealer's hand was: %s \nYour hand was: %s" % (dlrhand, plyrhand))
            dlrbal += wager
            print(dlrbal)
        elif(plyrpts > dlrpts and Bust == False or dlrBust == True and Bust == False):
            print("You win!\nThe dealer's hand was: %s \nYour hand was: %s!" % (dlrhand, plyrhand))
            dlrbal -= wager
            pot += wager
            plyrbal += pot
            pot = 0
            print(plyrbal)
        else:
            print("It was a tie.")
            plyrbal += pot
        if (plyrbal == 0):
            print("Yikes pal! It looks like you're out of dabloons, so you can't go for another round.\nBetter luck next time!")
            quit()
        play_again = input("Would you like to play another around? (Y/N)")
        if play_again.startswith("Y"):
            cards.extend(plyrhand)
            cards.extend(dlrhand)
            random.shuffle(cards)
            plyrhand = []
            dlrhand = []
            dlrpts = 0
            plyrpts = 0
            wager = 0
            pot = 0
            Bust = False
            dlrBust = False
            print("That's the spirit!")
            gamble = True
        elif play_again.startswith("N"):
            print("Thanks for playing!")
            quit()

play_game = input("Howdy Pardner! Welcome to Trey's casino.\nWould you like to play a game of blackjack? (Y/N)")
if play_game.startswith("Y"):
    print("Yeehaw! Let's get you started then pal.")
    print("We'll start you off with 100 chips.")
    time.sleep(1)
    blackjack()
