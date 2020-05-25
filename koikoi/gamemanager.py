#2020 Levi D. Smith - levidsmith.com
import pygame
import random
import math
import os.path

from card import Card
from player import Player
from button import Button
from drawhelper import DrawHelper
from globals import Globals

from operator import itemgetter, attrgetter

class GameManager:

    WAIT_DELAY = 60 * 2

    players = []
    cards = []
    table = []
    draw_card = None
    
    card_images = []
    card_back_images = []
    sound_effects = {}
    
    background = []

    iCurrentPlayer = 0
    
    deck_position = (64, 296)
    draw_card_position = (256, 296)
    table_position = (400, 200)
    
    buttons = []
    
    def __init__(self):
        self.load_images()
        self.load_audio()
        self.restart()
    
        self.makeButtons()
        self.isCursorHovered = False
        

    
    def makeButtons(self):
        b = Button("Arrange", 0, 0)
        b.action = self.arrangeCards
        b.show()
        self.buttons.append(b)

        b = Button("Koi", 200, 0)
        b.action = self.doContinue
        b.hide()
        self.buttons.append(b)
        
        b = Button("Stop", 400, 0)
        b.action = self.doStop
        b.hide()
        self.buttons.append(b)



    
    def load_images(self):
        for i in range(12):
            for j in range(4):
                print(str(i) + ", " + str(j))
                strFile = 'images/hanafuda_' + str(i + 1) + '-' + str(j + 1) + '.jpg'
                if (os.path.isfile(strFile)):
                    img = pygame.image.load(strFile)
                    img = pygame.transform.scale(img, (Card.w, Card.h))
                    #self.card_images[(i * 4) + j] = img
                    self.card_images.append(img)


        img = pygame.image.load('images/hanafuda_back.jpg')
        img = pygame.transform.scale(img, (Card.w, Card.h))
        self.card_back_images.append(img)

        img = pygame.image.load('images/card_border.png')
        self.card_back_images.append(img)


        imgBackground = pygame.image.load('images/background.jpg')
        self.background.append(imgBackground)

    def load_audio(self):
        pygame.mixer.music.load('audio/PyKoiKoi_game.mp3')
        pygame.mixer.music.set_volume(0.5)
        self.sound_effects['card_drop'] = pygame.mixer.Sound('audio/card_drop.wav')
        self.sound_effects['next_player'] = pygame.mixer.Sound('audio/next_player.wav')

    def set_audio_volume(self, vol):
        pygame.mixer.music.set_volume(0)
    
    def restart(self):
        self.iCurrentPlayer = 0
        self.players.clear()
        self.cards.clear()
        self.table.clear()
    
        for i in range(12):
            for j in range(4):
#                print(str(i) + ", " + str(j))
                card = Card((i * 4) + j,  i * 80, j * 150)
                card.iMonth = i
                card.img = self.card_images[(i * 4) + j]
                card.img_back = self.card_back_images[0]
                card.img_border = self.card_back_images[1]

#                strFile = 'images/hanafuda_' + str(i + 1) + '-' + str(j + 1) + '.jpg'
#                if (os.path.isfile(strFile)):
#                    card.img = pygame.image.load(strFile)
 #                   card.img = pygame.transform.scale(card.img, (card.w, card.h))
                
            
            
                if (i == 0):
                    if (j == 2):
                        card.isRedRibbon = True
                        card.isPoetryRibbon = True
                    if (j == 3):
                        card.isLight = True

                if (i == 1):
                    if (j == 2):
                        card.isRedRibbon = True
                        card.isPoetryRibbon = True
                    if (j == 3):
                        card.isSpecial = True

                if (i == 2):
                    if (j == 2):
                        card.isRedRibbon = True
                        card.isPoetryRibbon = True
                    if (j == 3):
                        card.isLight = True
                        card.isSakuraCurtain = True

                if (i == 3):
                    if (j == 2):
                        card.isRedRibbon = True
                    if (j == 3):
                        card.isSpecial = True

                if (i == 4):
                    if (j == 2):
                        card.isRedRibbon = True
                    if (j == 3):
                        card.isSpecial = True

                if (i == 5):
                    if (j == 2):
                        card.isBlueRibbon = True
                    if (j == 3):
                        card.isSpecial = True
                        card.isBoarDeerButterfly = True

                if (i == 6):
                    if (j == 2):
                        card.isRedRibbon = True
                    if (j == 3):
                        card.isSpecial = True
                        card.isBoarDeerButterfly = True

                if (i == 7):
                    if (j == 2):
                        card.isSpecial = True
                    if (j == 3):
                        card.isLight = True
                        card.isMoon = True

                if (i == 8):
                    if (j == 2):
                        card.isBlueRibbon = True
                    if (j == 3):
                        card.isSakeCup = True
                        card.isNormal = True

                if (i == 9):
                    if (j == 2):
                        card.isBlueRibbon = True
                    if (j == 3):
                        card.isSpecial = True
                        card.isBoarDeerButterfly = True

                if (i == 10):
                    if (j == 1):
                        card.isSpecial = True
                    if (j == 2):
                        card.isRedRibbon = True
                    if (j == 3):
                        card.isRainMan = True

                if (i == 11):
                    if (j == 3):
                        card.isLight = True

                
            
                self.cards.append(card)
        
        random.shuffle(self.cards)
        


        

        #Create players
        p1 = Player(self)
        p1.name = "Player One"
        p1.isHidden = True
        p1.position = (64, 32)
        p1.score_offset = (960, -20)
        p1.card_types_offset = (1080, -20)
        p1.match_card_position = (660, 0)
#        for i in range(8):
#            draw_card = self.cards.pop()
#            draw_card.x = 0
#            draw_card.y = p1.position[1]
#            draw_card.targetPosition = (p1.position[0] + (i * 80), p1.position[1])
#            p1.cards.append(draw_card)

        self.players.append(p1)
    



        p2 = Player(self)
        p2.name = "Player Two"
        p2.isHidden = False
        p2.isHuman = True
        p2.position = (64, 512)
        p2.score_offset = (960, -140)
        p2.card_types_offset = (1080, -140)
        p2.match_card_position = (660, 0)
        

        self.players.append(p2)
        
        self.dealCards()
        
        self.players[self.iCurrentPlayer].isPlayerTurn = True
        self.players[self.iCurrentPlayer].iWaitDelay = self.WAIT_DELAY
        
        pygame.mixer.music.play(-1)

    def dealCards(self):
        #Deal to the table
        for i in range(8):
            draw_card = self.cards.pop()
            draw_card.x = 0
            draw_card.y = (Globals.SCREEN_SIZE[1] - Card.h) / 2
            draw_card.isHidden = False
            self.table.append(draw_card)

        self.setCardPositions()

        for player in self.players:

            for i in range(8):
                draw_card = self.cards.pop()
                draw_card.x = 0
                draw_card.y = player.position[1]
                if (player.isHuman):
                    draw_card.isHidden = False
                else:
                    draw_card.isHidden = True
            
                draw_card.targetPosition = (player.position[0] + (i * 80), player.position[1])
                player.cards.append(draw_card)

    
    
    def nextRound(self):
        for player in self.players:
            for card in player.cards:
                self.cards.append(card)
                player.cards.remove(card)

            for card in player.match_cards:
                self.cards.append(card)
                player.match_cards.remove(card)
                
            player.nextRound()

        for card in self.table:
            self.cards.append(card)
            self.table.remove(card)

        random.shuffle(self.cards)
        
#        i = 0
#        for card in self.cards:
#            card.x = self.deck_position[0] + (i * 2)
#            card.y = self.deck_position[1]
#            card.targetPosition = (card.x, card.y)
#            i += 1

        
        self.setCardPositions()
        self.dealCards()


    def update(self):
#        print ("GameManager update")
        for card in self.table:
            card.update()
            
        if (self.draw_card != None):
            self.draw_card.update()
        
        for player in self.players:
            player.update()


        if (not self.players[self.iCurrentPlayer].isPlayerTurn):
            self.doNextPlayer()
          

                
    def draw(self, display, font):
        display.blit(self.background[0], (0, 0))

        for card in self.cards:
            card.draw(display, font)

        for card in self.table:
            card.draw(display, font)
        
        if (self.draw_card != None):
            self.draw_card.draw(display, font)
        
        for player in self.players:
            player.draw(display, font)
            
        for button in self.buttons:
            button.draw(display, font)

        strCopyright = '2020 Levi D. Smith'
#        c = (255, 255, 255)
#        text = font.render(strCopyright, True, c)
#        display.blit(text, (1000, 680))
        DrawHelper.drawTextShadow(strCopyright, 500, 720-32, (255, 255, 255), display, font[1])

    def doNextPlayer(self):
        self.iCurrentPlayer += 1
        if (self.iCurrentPlayer >= len(self.players)):
            self.iCurrentPlayer = 0
        
        self.players[self.iCurrentPlayer].isPlayerTurn = True
        self.players[self.iCurrentPlayer].iStep = Player.STEP_HAND_MATCH
        self.players[self.iCurrentPlayer].iWaitDelay = self.WAIT_DELAY
        

        print("doNextPlayer " + str(self.iCurrentPlayer))
        self.sound_effects['next_player'].play()
        
            

    def setCardPositions(self):
        i = 0
        iCardsPerRow = math.ceil(len(self.table) / 2)
#        iTableCardCount = 10
        
        for card in self.table:
            card.targetPosition = (self.table_position[0] + ((i % iCardsPerRow) * 80), self.table_position[1] + 160 * math.floor(i / iCardsPerRow))
            i += 1
            
        for card in self.cards:
            card.x = self.deck_position[0] + (i * 2)
            card.y = self.deck_position[1]
            card.targetPosition = (card.x, card.y)
            i += 1




    def mousePressed(self, mousePosition):
        mouseX = mousePosition[0]
        mouseY = mousePosition[1]
        self.selectCard(mouseX, mouseY)
        self.checkButtonsPress(mouseX, mouseY)
    
    def mouseReleased(self, mousePosition):
        mouseX = mousePosition[0]
        mouseY = mousePosition[1]
        self.dropCard(mouseX, mouseY)
        
    def mouseMoved(self, mousePosition):
        mouseX = mousePosition[0]
        mouseY = mousePosition[1]

        isHovered = self.isCursorHovered
        self.isCursorHovered = False #Set cursor hovered to false, and then set it to true if any cards or buttons are hovered

        self.dragCard(mouseX, mouseY)
        self.checkButtonsHover(mouseX, mouseY)
        self.checkCardsHover(mouseX, mouseY)
        
        #compare the previous cursor state with the current cursor state
        #only change the cursor if the state changes, to reduce flicker
        if (isHovered != self.isCursorHovered):
            if (self.isCursorHovered):
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
            
            
    
        
        
    def selectCard(self, x, y):
    
#        for player in self.players:
        currentPlayer = self.players[self.iCurrentPlayer]



        if (currentPlayer.iStep == Player.STEP_HAND_MATCH):
            for card in currentPlayer.cards:
                if (self.isCardAtPosition(card, x, y)):
                    print("Selected card " + str(card))
                    currentPlayer.selectedCard = card
                    currentPlayer.selectedCard.previousPosition = (currentPlayer.selectedCard.x, currentPlayer.selectedCard.y)

#            if (len(self.cards) > 0 and self.isCardAtPosition(self.cards[len(self.cards) - 1], x, y)):
#                currentPlayer.drawCard()


        elif (currentPlayer.iStep == Player.STEP_DRAW):
            if (len(self.cards) > 0 and self.isCardAtPosition(self.cards[len(self.cards) - 1], x, y)):
                currentPlayer.drawCard()

        elif (currentPlayer.iStep == Player.STEP_DRAW_MATCH):
            if (self.draw_card != None):
                card = self.draw_card
                if (self.isCardAtPosition(card, x, y)):
                    print("Selected card " + str(card))
                    currentPlayer.selectedCard = card
                    currentPlayer.selectedCard.previousPosition = (currentPlayer.selectedCard.x, currentPlayer.selectedCard.y)
        

        
        

                    
    def dropCard(self, x, y):
        currentPlayer = self.players[self.iCurrentPlayer]
        if (currentPlayer.selectedCard != None):

            landedCard = None
            for card in self.table:
                if (self.isCardAtPosition(card, x, y)):
                    landedCard = card
                
                
                
            if (currentPlayer.iStep == Player.STEP_HAND_MATCH):
                if (landedCard != None):
                    successfulMatch = currentPlayer.doMatch(currentPlayer.selectedCard, landedCard)
                    if (successfulMatch):
                        currentPlayer.iStep = Player.STEP_DRAW
                        currentPlayer.selectedCard = None
                    else:
                        currentPlayer.selectedCard.targetPosition = currentPlayer.selectedCard.previousPosition
                        currentPlayer.selectedCard = None
                else:
                    currentPlayer.doDiscard(currentPlayer.selectedCard)
                    currentPlayer.selectedCard = None
                    self.setCardPositions()
                    currentPlayer.iStep = Player.STEP_DRAW


            elif (currentPlayer.iStep == Player.STEP_DRAW_MATCH):
                if (landedCard != None):
                    successfulMatch = currentPlayer.doMatch(currentPlayer.selectedCard, landedCard)
                    if (successfulMatch):
                        currentPlayer.selectedCard = None
                        currentPlayer.iStep = Player.STEP_DONE
                    else:
                        currentPlayer.selectedCard.targetPosition = currentPlayer.selectedCard.previousPosition
                        currentPlayer.selectedCard = None
                
                else:
                    currentPlayer.doDiscard(currentPlayer.selectedCard)
                    
#                    currentPlayer.selectedCard.targetPosition = currentPlayer.selectedCard.previousPosition
                    currentPlayer.selectedCard = None
                    currentPlayer.iStep = Player.STEP_DONE
                    
          
                    




                    
                    

                
            
                
                
        
    def dragCard(self, x, y):
        currentPlayer = self.players[self.iCurrentPlayer]
        if (not currentPlayer.selectedCard == None):
            currentPlayer.selectedCard.x = x
            currentPlayer.selectedCard.y = y
            currentPlayer.selectedCard.targetPosition = (x, y)
            
    def isCardAtPosition(self, card, x, y):
        isCardAtPosition = False
        if (x > card.x and x < card.x + card.w and y > card.y and y < card.y + card.h):
            isCardAtPosition = True
            
        return isCardAtPosition
        
        
    def arrangeCards(self):
        print("arrangeCards")
        self.table.sort(key=attrgetter('iMonth'))
        self.setCardPositions()
        
        for player in self.players:
            player.cards.sort(key=attrgetter('iMonth'))
            player.setCardPositions()
        
        
        
    def doContinue(self):
        print("Koi (Continue)")
        self.buttons[1].hide()
        self.buttons[2].hide()

        currentPlayer = self.players[self.iCurrentPlayer]
        currentPlayer.doContinue()


        
        
    def doStop(self):
        print("Stop - End Round")
        self.buttons[1].hide()
        self.buttons[2].hide()

        for player in self.players: 
            player.iRoundScores.append(player.score.iTotalPoints)


        
        self.nextRound()
        
    def checkButtonsPress(self, x, y):
        for button in self.buttons:
            if (button.isClicked(x, y)):
                print(button.strLabel + " button clicked")
                button.action()
                
    def checkButtonsHover(self, x, y):
        for button in self.buttons:
            self.isCursorHovered = self.isCursorHovered or button.isHovered(x, y)

    def checkCardsHover(self, x, y):
        for card in self.table:
            self.isCursorHovered = self.isCursorHovered or card.isHovered(x, y)

        for card in self.cards:
            self.isCursorHovered = self.isCursorHovered or card.isHovered(x, y)

        if (self.draw_card != None):
            self.isCursorHovered = self.isCursorHovered or self.draw_card.isHovered(x, y)

        
        for player in self.players:
            for card in player.cards:
                self.isCursorHovered = self.isCursorHovered or card.isHovered(x, y)
        
            for card in player.match_cards:
                self.isCursorHovered = self.isCursorHovered or card.isHovered(x, y)
    
    
    def continuePrompt(self):
        #show the "Koi" and "Stop" buttons
        self.buttons[1].show()
        self.buttons[2].show()
        