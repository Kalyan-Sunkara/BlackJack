import random
gameRunning = True


class bank():
    def __init__(self, deposit):
        self.total = deposit
        self.currentBet = 0
    def bet(self):
        valid = False
        while(not valid):
            try:
                amount = int(input('How Much Would You Like To Bet?'))
                if(amount > self.total):
                    print('Please Enter Valid Bet...')
                else:
                    self.total -= amount
                    self.currentBet = amount
                    valid = True
                    print('Good Luck!')
            except:
                print('(Error)Please Enter Valid Bet...')
    def dispBalance(self):
        print(f'Your bank balance is: {self.total}')
    def giveBalance(self):
        return self.total
    def addToBank(self, amount):
        self.total += amount
    def getCurrentBet(self):
        return self.currentBet
            
class deck():
    def __init__(self):
        self.whole_deck = []
        self.number_of_cards = 52
        x = 2
        while(x < 11):
            y = 0
            while(y < 4):
                self.whole_deck.append(x)
                y += 1
            x += 1
        for x in range(0,4):
            self.whole_deck.append('J')
        for x in range(0,4):
            self.whole_deck.append('Q')
        for x in range(0,4):
            self.whole_deck.append('K')
        for x in range(0,4):
            self.whole_deck.append('A')
    def remove(self,card):
        self.whole_deck.remove(card)
        self.number_of_cards -= 1
    def displayDeck(self):
        print(self.whole_deck)
    def randomCard(self):
        return random.choice(self.whole_deck)
class hand():
    def __init__(self):
        self.cards = []
        self.valueOfHand = 0
        
    def addCard(self,card):
        self.cards.append(card)
        try:
            self.valueOfHand += card
        except:
            if card == 'A':
                self.valueOfHand += 11
            else:
                self.valueOfHand += 10
                
    def getHandValue(self):
        return self.valueOfHand
    
    def displayHand(self):
        print(self.cards)
        print(self.valueOfHand)
        
class gameMechanicsPlayer():
    def __init__(self):
        self.deck1 = deck()
        self.player = hand()
    def bustCheck(self):
        if self.player.valueOfHand > 21:
            
            print("Bust")
            return False
        else:
            return True
        
    def draw(self):
        answer = ''
        while(answer != 'Yes' and answer != 'yes'):
            self.player.addCard(self.deck1.randomCard())
            self.player.displayHand()
            if not self.bustCheck():
                return False
            answer = input('Would you like to stop drawing, Yes or No?')
            while(answer != 'yes' and answer != 'Yes' and answer !=  'no' and answer != 'No'):
                answer = input('Please pick a valid choice...(Yes/No)')
        return True
    def getDeck(self):
        return self.deck1
    def getHand(self):
        return self.player
    
    def showHand(self):
        print('Your hand: ')
        self.player.displayHand()

#simple computer opponent
class gameMechanicsComputer():
    def __init__(self, gameDeck, playerHand):
        self.gameDeck = gameDeck
        self.playerHand = playerHand
        self.computerHand = hand()
        self.TIE = False
    def beatPlayer(self):
        while(self.playerHand.getHandValue() > self.computerHand.getHandValue()):
            self.computerHand.addCard(self.gameDeck.randomCard())
            if(self.computerHand.getHandValue() == 21 and self.playerHand.getHandValue() == 21):
                self.TIE = True
                break
            elif(self.computerHand.getHandValue() > 21):
                print('Computer Bust')
                return False
                break
            else:
                continue
        return True
    def tie(self):
        return self.TIE
    def getComputerHand(self):
        return self.computerHand.displayHand()
    def getComputerHandValue(self):
        return self.computerHand.getHandValue()
        
def YorN():
    choice = ''
    while(choice != 'N' and choice != 'n'):
        choice = input('Would you like to play again?(Y/N)')
        if choice == 'Y' or choice == 'y':
            return True
        elif choice == 'N' or choice == 'n':
            return False
        else:
            print('Enter Valid choice....')
            
def play():
    global gameRunning
    amount = -1;
    while(amount <= 0):
        amount = int(input('Please enter starting balance'))
    playerBank = bank(amount)
    playerBank.dispBalance()
    
    while(gameRunning):
        playerBank.bet()
        playerBank.dispBalance()
        gamePlayer = gameMechanicsPlayer()
        choice = ''
        while(choice != 'E' and choice != 'e'):
            busted = False
            print('\n')
            print("Press 'D' to draw a card\n")
            print("Press 'S' to show your deck\n")
            print("Press 'E' to end your turn\n")
            choice = input('Choose what an action')
            if choice == 'E' or choice == 'e':
                print('Player turn done!\n')
            elif choice == 'D' or choice == 'd':
                if not gamePlayer.draw():
                    busted = True
                    statusForBet = 0
                    break
            elif choice == 'S' or choice == 's':
                gamePlayer.showHand()
            else:
                print('Please enter a valid choice!\n')
        if not busted:
            comp = gameMechanicsComputer(gamePlayer.getDeck(),gamePlayer.getHand())

            if(comp.beatPlayer()):
                statusForBet = 0
                print('Computer Hand: ')
                print(comp.getComputerHand())
                print('\n')
                print('Computer Hand Value: ')
                print(comp.getComputerHandValue())
                print('\n')
                print('The Computer Won!\n')
            elif(comp.tie()):
                statusForBet = 1
                print('Computer Hand: ')
                print(comp.getComputerHand())
                print('\n')
                print('Computer Hand Value: ')
                print(comp.getComputerHandValue())
                print('\n')
                print('Game Tied')
            else:
                statusForBet  = 2
                print('Computer Hand: ')
                print(comp.getComputerHand())
                print('\n')
                print('Computer Hand Value: ')
                print(comp.getComputerHandValue())
                print('\n')
                print('You Win!\n')
            
        if(statusForBet == 0):
            pass
        elif(statusForBet == 1):
            playerBank.addToBank(playerBank.getCurrentBet())
        else:
            playerBank.addToBank(playerBank.getCurrentBet()*2)
            
        gameRunning = YorN()
        
        if playerBank.giveBalance() <= 0 and gameRunning == True:
            print("Oops sorry you are out of money, Goodbye!")
            gameRunning = False
                 
play()
