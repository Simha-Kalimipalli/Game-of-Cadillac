!pip install colorama
from colorama import Fore, Back, Style
import random


class Card:
   def __init__(self, name, value, suit):
       self.name = name
       self.value = value
       self.suit = suit

   # GAME CLASS


class Player:
   # constructor
   def __init__(self, cards):
       self.cards = []


# GAME CLASS
class Game:
   # static variable
   totalcards = 52
   decknums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, \
               2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

  #  nam_arr = ["H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK", "HA", "C2", "C3", "C4", "C5",
  #             "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK", "CA", \
  #             "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK", "DA", "S2", "S3", "S4", "S5",
  #             "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK", "SA"]

  #  nam_arr = ["\u2665-2", "\u2665-3", "\u2665-4", "\u2665-5", "\u2665-6", "\u2665-7", "\u2665-8", "\u2665-9", "\u2665-10", "\u2665-J", "\u2665-Q", "\u2665-K", "\u2665-A", "\u2663-2", "\u2663-3", "\u2663-4", "\u2663-5",
  #             "\u2663-6", "\u2663-7", "\u2663-8", "\u2663-9", "\u2663-10", "\u2663-J", "\u2663-Q", "\u2663-K", "\u2663-A", \
  #             "\u2666-2", "\u2666-3", "\u2666-4", "\u2666-5", "\u2666-6", "\u2666-7", "\u2666-8", "\u2666-9", "\u2666-10", "\u2666-J", "\u2666-Q", "\u2666-K", "\u2666-A", "\u2660-2", "\u2660-3", "\u2660-4", "\u2660-5",
  #             "\u2660-6", "\u2660-7", "\u2660-8", "\u2660-9", "\u2660-10", "\u2660-J", "\u2660-Q", "\u2660-K", "\u2660-A"]

   h_arr = ["\u2665-2", "\u2665-3", "\u2665-4", "\u2665-5", "\u2665-6", "\u2665-7", "\u2665-8", "\u2665-9", "\u2665-10", "\u2665-J", "\u2665-Q", "\u2665-K", "\u2665-A"]
   c_arr = ["\u2663-2", "\u2663-3", "\u2663-4", "\u2663-5", "\u2663-6", "\u2663-7", "\u2663-8", "\u2663-9", "\u2663-10", "\u2663-J", "\u2663-Q", "\u2663-K", "\u2663-A", ]
   d_arr = ["\u2666-2", "\u2666-3", "\u2666-4", "\u2666-5", "\u2666-6", "\u2666-7", "\u2666-8", "\u2666-9", "\u2666-10", "\u2666-J", "\u2666-Q", "\u2666-K", "\u2666-A"]
   s_arr = ["\u2660-2", "\u2660-3", "\u2660-4", "\u2660-5","\u2660-6", "\u2660-7", "\u2660-8", "\u2660-9", "\u2660-10", "\u2660-J", "\u2660-Q", "\u2660-K", "\u2660-A"]

   h_arr1 = [Fore.RED + x + Style.RESET_ALL for x in h_arr]
   c_arr1 = [Fore.BLACK + x + Style.RESET_ALL for x in c_arr]
   d_arr1 = [Fore.RED + x + Style.RESET_ALL for x in d_arr]
   s_arr1 = [Fore.BLACK + x + Style.RESET_ALL for x in s_arr]

   nam_arr = h_arr1 + c_arr1 + d_arr1 + s_arr1



   suit_list_arr = ["Hearts", "Hearts", "Hearts", "Hearts", "Hearts", "Hearts", "Hearts", "Hearts", "Hearts", "Hearts",
                    "Hearts", "Hearts", "Hearts", \
                    "Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs", "Clubs",
                    "Clubs", "Clubs", \
                    "Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds",
                    "Diamonds", "Diamonds", "Diamonds", "Diamonds", "Diamonds", \
                    "Spades", "Spades", "Spades", "Spades", "Spades", "Spades", "Spades", "Spades", "Spades", "Spades",
                    "Spades", "Spades", "Spades"]

   

   deck = []

   discard = []

   player1 = []
   player2 = []

   # constructor

   def __init__(self, cntplayers):
       # self.deck =  []
       # self.discard = 0
       self.numplayers = cntplayers
       self.players = []

   def startdeck(self):
       for x in range(0, Game.totalcards):
           Game.deck.append(Card(Game.nam_arr[x], Game.decknums[x], Game.suit_list_arr[x]))
       return Game.deck

   def printdeck(self):
       for x in Game.deck:
           print(x.name)
           print(x.value)
           print(x.suit)

   def printdeckval(self):
       for x in Game.deck:
           print(x.value)

   def printsuitval(self):
       for x in Game.deck:
           print(x.name)
           print(x.value)

   def printval(self):
       print("Deck _____________________________________________________")
       time = 0
       for x in Game.deck:
           if (time == (len(Game.deck) - 1)):
               print(x.name, "]")
           elif time == 0:
               print("[", x.name, ",", end='')
           else:
               print(x.name, ", ", end='')
           time = time + 1

           # _---------------------------------------------------------------------------------
       print("Discard _____________________________________________________")
       time = 0
       for x in Game.discard:
           if len(Game.discard) == 1:
               print("[" + Game.discard[0].name + "]")
           else:
               if (time == (len(Game.discard) - 1)):
                   print(x.name, "]")
               elif time == 0:
                   print("[", x.name, ",", end='')
               else:
                   print(x.name, ", ", end='')
               time = time + 1

   def printplay_val(self):

       print("Player1 _____________________________________________________")
       time = 0
       for x in Game.player1:
           if (time == (len(Game.player1) - 1)):
               print(x.name, "]")
           elif time == 0:
               print("[", x.name, ",", end='')
           else:
               print(x.name, ",", end='')
           time = time + 1

           # _---------------------------------------------------------------------------------
       print("Player2 _____________________________________________________")
       time = 0
       for x in Game.player2:
           if (time == (len(Game.player2) - 1)):
               print(x.name, "]")
           elif time == 0:
               print("[", x.name, ",", end='')
           else:
               print(x.name, ",", end='')
           time = time + 1
    
   def print_main(self,x):      
        time = 0
        len_of_discard_deck = len(Game.discard)
        print("Player"+ str(x)+ "'s Turn: _________________________________________________________")

        print("Deck: [?]                      Discard: ["+str(Game.discard[len_of_discard_deck - 1].name)+"]")
        print("  ")

        if x == 1:
          for x in Game.player1:
           if (time == (len(Game.player1) - 1)):
               print(x.name, "]       Player2: [ ? ? ? ]")
           elif time == 0:
               print("Player1: [", x.name, "", end='')
           else:
               print(x.name, "", end='')
           time = time + 1

        if x == 2:
          for x in Game.player2:
           if (time == (len(Game.player2) - 1)):
               print(x.name,"]       Player1: [ ? ? ? ]")
           elif time == 0:
               print("Player2: [", x.name, "", end='')
           else:
               print(x.name, "", end='')
           time = time + 1

        print(" ")
        print(" ")




   def startplayers(self):

       # print(Game.player1)
       # print(Game.player2)
       # print(self.numplayers)
       # player1 = []
       # arr = [10,11,17,18,59,49,37,78,68,69,70]
       # arr = Game.deck

       # print("Hi")
       # Player1 = Player([])
       # Player2 = Player([])
       # player2 = []
       # discar = []
       # discar = Game.discard

       for counter in range(0, 6):
           ran_number = random.randint(0, len(Game.deck) - 1)
           # print(ran_number)
           if (counter % 2 == 0):
               Game.player1.append(Game.deck[ran_number])
               Game.deck.pop(ran_number)
           elif (counter % 2 == 1):
               Game.player2.append(Game.deck[ran_number])
               Game.deck.pop(ran_number)

       ran_number = random.randint(0, len(Game.deck) - 1)
       # print(ran_number)
       Game.discard.append(Game.deck[ran_number])
       Game.deck.pop(ran_number)

   # print("player " + str(Game.player1))
   # print("player 2" + str(Game.player2))
   # print("arr " + str(arr))
   # print("disca " + str(discar))
   def turn_player(self, x):

       # arr = [3,6,9,5,69]

       # dcar = [23,24]
       # player  = [59, 18, 49]
       if x == 1:
           player = Game.player1
       if x == 2:
           player = Game.player2

       # print("discard " + str(dcar))
       # print("player " + str(player))
       # print("arr " + str(Game.deck))

       ran_number = random.randint(0, len(Game.deck) - 1)
       # print("ran_number " +str(ran_number))
       print("Do you want to pick up a card from the deck [1] or the discard pile [2] ")
       input1 = int(input())

       if input1 == 1:

           # print(" card drawn: Do you want to keep " + str(arr[ran_number]) + " [Y]/[N] ")
           # input2= input()
           input2 = "input"
           while (((input2 != "y") and (input2 != 'Y')) and ((input2 != "n") and (input2 != 'N'))):
               print("Card drawn: Do you want to keep " + str(Game.deck[ran_number].name) + " [Y] / [N] ")
               input2 = input()
           if ((input2 == "y") or (input2 == 'Y')):
               print("Which card you want to switch with: " + str(player[0].name) + " [1], " + str(
                   player[1].name) + "  [2]," + str(player[2].name) + " [3]")
               input3 = int(input())
               b = input3 - 1
               c = Game.deck[ran_number]
               Game.discard.append(player[b])
               player.pop(b)
               player.append(Game.deck[ran_number])
               Game.deck.pop(ran_number)
           elif ((input2 == "n") or (input2 == 'N')):
               Game.discard.append(Game.deck[ran_number])
               Game.deck.pop(ran_number)
       elif input1 == 2:
           # print("Discard pile " + str(Game.discard[len(Game.discard)-1]))
           print("Which card you want to switch with: " + str(player[0].name) + " [1], " + str(
               player[1].name) + "  [2]," + str(player[2].name) + " [3]")
           input4 = int(input())
           ap = input4 - 1
           c = player[ap]
           d = Game.discard.pop()
           player.pop(ap)
           Game.discard.append(c)
           player.append(d)
       if x == 1:
           Game.player1 = player
       if x == 2:
           Game.player2 = player

       # print("discard " + str(Game.discard))

   #  print("player " + str(player))
   #  print("arr " + str(arr))

   def artificial_intelligence(self):
    #playerarr = ["H6","D3","H4"]
    player = [6,3,4]
    target_class = "iv"
    least_card = "70"
    points = 0
    play3 = ["Hearts","Diamonds","Hearts"]
    # playerarr = ["H6","H3","H4"]
    # player = [6,3,4]


    playerarr = [Game.player2[0].name,Game.player2[1].name,Game.player2[2].name]

    print(playerarr)

    player = [Game.player2[0].value,Game.player2[1].value,Game.player2[2].value]

    print(player)
    play3 = [Game.player2[0].suit,Game.player2[1].suit,Game.player2[2].suit]
    print(play3)



    points =0
    if ((play3[0] == play3[1]) and (play3[1] == play3[2]) and (play3[0] == play3[2])):
      points = player[0] + player[1]+ player[2]
      print(points)
      target_class = play3[0]

      if (player[0]>player[1]) and player[2]>player[1] :
          least_card = playerarr[1]
      elif (player[1]>player[0]) and player[2]>player[0] :
          least_card = playerarr[0]
      elif (player[0]>player[2]) and player[1]>player[2] :
          least_card = playerarr[2]

    elif ((play3[0] == play3[1]) and(player[0] + player[1] <player[2])):
      points = player[2]
      target_class = play3[2]

      if  play3[0] <play3[1]:
        least_card = playerarr[0]
      elif (play3[0] > play3[1]):
        least_card = playerarr[1]

    elif ((play3[0] == play3[1]) and(player[0] + player[1] > player[2])):
      points = player[0] + player[1]
      target_class = play3[0]
      least_card = playerarr[2]
      #return points

    elif ((play3[0] == play3[2]) and(player[0] + player[2] <player[1])):
      points = player[1]
      target_class = play3[1]

      if  play3[0] <play3[2]:
        least_card = playerarr[0]
      elif (play3[0] > play3[2]):
        least_card = playerarr[2]
    #  return points

    elif ((play3[0] == play3[2]) and(player[0] + player[2] >player[1])):
      points = player[0]  +player[2]
      target_class = play3[0]
      least_card = playerarr[1]
      #return points

    elif ((play3[1] == play3[2]) and(player[1] + player[2] <player[0])):
      points = player[0]
      target_class = play3[0]

      if  play3[1] <play3[2]:
        least_card = playerarr[1]
      elif (play3[2] < play3[1]):
        least_card = playerarr[2]
    # return points

    elif ((play3[1] == play3[2] ) and(player[1] + player[2] >player[0])):
      points = player[1] + player[2]
      target_class = play3[1]
      least_card = playerarr[0]
      #return points

    elif ((play3[0] != play3[1]) and (play3[1] != play3[2]) and (play3[0] !=play3[2])):
      points = max(player[0],player[1],player[2])
      if (player[0]<player[1]) and player[2]<player[1] :
          target_class = play3[1]
      elif (player[1]<player[0]) and player[2]<player[0] :
          target_class = play3[0]
      elif (player[0]<player[2]) and player[1]<player[2] :
          target_class = play3[2]

      if (play3[0]>play3[1]) and play3[2]>play3[1] :
          least_card = playerarr[1]
      elif (play3[1]>play3[0]) and play3[2]>play3[0] :
          least_card = playerarr[0]
      elif (play3[0]>play3[2]) and play3[1]>play3[2] :
        least_card = playerarr[2]
      #return points   1

      #if Game.deck[ran_number].name

    #__________________________
        #___________________________________________________________________________________________________________________________
    player_2 = Game.player2
    ran_number = random.randint(0,len(Game.deck) -1)

    #print("ran_number " +str(ran_number))
    print("Want to pick up card from deck [1] or discard pile [2] ")


    least_card_in_sui = []

    isnottarget = 0



    # print("print playe")
    # print(player_2[0].suit)
    # print(player_2[1].suit)
    # print(player_2[2].suit)


    #for count in range(0,3):
    #  print(player_2[count].suit)


    ttryi =0



    for counter in range(0,3):
      if player_2[counter].suit == target_class:
        least_card_in_sui.append(player_2[counter].value)
        ttryi=ttryi+1
      elif player_2[counter].suit != target_class:
        isnottarget=isnottarget+1


      # print("tt ttryi " +str(ttryi))

      # print("is not target " + str(isnottarget))



    #print(least_card_in_sui)



    #print("min  " + str(min(least_card_in_sui)))



    # print("leaassst car " + str(least_card))



    least_card_suit = min(least_card_in_sui)
    #least_card_suit = "C5"

    input1 = 0





    #target_class = "Hearts"
    #a = 3
    #least_card = "S8"
    #_____________________________________________________________
    if (Game.discard[len(Game.discard)-1].suit == target_class):
      if ((Game.discard[len(Game.discard)-1].value >least_card_suit) and(isnottarget==0)) or (isnottarget>=1):
        input1 = 2
      else:
        input1 = 1
    else:
      input1 = 1

    print(input1)
    #--------------------------------------------------------------

    #input1= int(input())

    if input1== 1:

      #print(" card drawn: Do you want to keep " + str(arr[ran_number]) + " [Y]/[N] ")
      #input2= input()
      input2 = "input"
      while (((input2!= "y") and (input2!= 'Y')) and ((input2!= "n") and (input2!= 'N'))) :
          print("Card drawn: Do you want to keep " + str(Game.deck[ran_number].name) + " [Y] / [N] ")
          #input2= input()
          #______________________________________________________________________________

          if (Game.deck[ran_number].suit == target_class):
              if ((Game.deck[ran_number].value >least_card_suit) and(isnottarget==0)) or (isnottarget>=1):
                input2 = "y"
              else:
                input2 = "n"
          else:
            input2 = "n"
          # if (Game.discard[len(Game.discard)-1].suit == target_class):# and (Game.discard[len(Game.discard)-1].value >least_card_in_sui):
          #   input2 = "y"
          # else:
          #   input2 = "n"
            #____________________________________________________________

          print(input2)
          #input2
      if ((input2 == "y") or (input2== 'Y')):
        print("Which card you want to switch with: " + str(player_2[0].name) +" [1], " + str(player_2[1].name) +"  [2]," + str(player_2[2].name)+" [3]")
        #input3 = int(input())
        input3 = 0
        #________________________________________________________________________
        if player_2[0].name == least_card:
          input3 = 1
        elif player_2[1].name == least_card:
          input3 = 2
        elif player_2[2].name == least_card:
          input3 = 3
        #__________________________________________________________________
        print(input3)
        b = input3 - 1
        c = Game.deck[ran_number]
        Game.discard.append(player_2[b])
        player_2.pop(b)
        player_2.append(Game.deck[ran_number])
        Game.deck.pop(ran_number)
      elif ((input2== "n") or (input2== 'N')):
          Game.discard.append(Game.deck[ran_number])
          Game.deck.pop(ran_number)
    elif input1== 2 :
        #print("Discard pile " + str(Game.discard[len(Game.discard)-1]))
        print("Which card you want to switch with: " + str(player_2[0].name) +" [1], " + str(player_2[1].name) +"  [2]," + str(player_2[2].name)+" [3]")
        #input4 = int(input())
        input4 = 0

        if player_2[0].name == least_card:
          input4 = 1
        elif player_2[1].name == least_card:
          input4 = 2
        elif player_2[2].name == least_card:
          input4 = 3

        print(input4)

        ap = input4 - 1
        c = player_2[ap]
        d = Game.discard.pop()
        player_2.pop(ap)
        Game.discard.append(c)
        player_2.append(d)



    #print(player_2.names)

    #Game.player2 = player
    #_____________________________________________________________________________________________________________



  #   Game.player2[0].name = playerarr[0]
  #   Game.player2[1].name = playerarr[1]
  #   Game.player2[2].name  = playerarr[2]

  #  # Game.player2[0].value = player_2[0].value
  #  # Game.player2[1].value = player_2[1].value
  #   #-----Game.player2[2].value = player_2[2].value

  #   Game.player2[0].suit = play3[0]
  #   Game.player2[1].suit = play3[1]
  #   Game.player2[2].suit = play3[2]

    Game.player2 = player_2


   def getscore(self, x):
       if x == 1:
           player = [Game.player1[0].value, Game.player1[1].value, Game.player1[2].value]
           play3 = [Game.player1[0].suit, Game.player1[1].suit, Game.player1[2].suit]
           # print("player " +str(player))
           # print("play3 " +str(play3))

       if x == 2:
           player = [Game.player2[0].value, Game.player2[1].value, Game.player2[2].value]

           play3 = [Game.player2[0].suit, Game.player2[1].suit, Game.player2[2].suit]
           # te the prints from the other


      # print("printt " + str(Game.player2[0].value))



       # Game.player1[1].value

       # playerarr = ["H6","D3","H4"]
       # player = [6,3,4]
       points = 0
       # play3 = ["Hearts","Diamonds","Hearts"]


      # print(player)
       # playerarr = ["S6","S3","C4"]
       # player = [6,3,4]
       # points = 0
       # player3 = ["Clubs", "Spades","Spades"]
       if ((play3[0] == play3[1]) and (play3[1] == play3[2]) and (play3[0] == play3[2])):
           points = player[0] + player[1] + player[2]
           return points
           print(points)
       elif ((play3[0] == play3[1]) and (player[0] + player[1] < player[2])):
           points = player[2]
           return points
       elif ((play3[0] == play3[1]) and (player[0] + player[1] > player[2])):
           points = player[0] + player[1]
           return points

       elif ((play3[0] == play3[2]) and (player[0] + player[2] < player[1])):
           points = player[1]
           return points
       elif ((play3[0] == play3[2]) and (player[0] + player[2] > player[1])):
           points = player[0] + player[2]
           return points

       elif ((play3[1] == play3[2]) and (player[1] + player[2] < player[0])):
           points = player[0]
           return points
       elif ((play3[1] == play3[2]) and (player[1] + player[2] > player[1])):
           points = player[1] + player[2]
           return points

       elif ((play3[0] != play3[1]) and (play3[1] != play3[2]) and (play3[0] != play3[2])):
           points = max(player[0], player[1], player[2])
           return points

       # print(getscore(player,playerarr, player3))


# ----------
print("Welcome to the game of")
print(Fore.CYAN+  r"""
 ________  ________  ________  ___  ___       ___       ________  ________     
|\   ____\|\   __  \|\   ___ \|\  \|\  \     |\  \     |\   __  \|\   ____\    
\ \  \___|\ \  \|\  \ \  \_|\ \ \  \ \  \    \ \  \    \ \  \|\  \ \  \___|    
 \ \  \    \ \   __  \ \  \ \\ \ \  \ \  \    \ \  \    \ \   __  \ \  \       
  \ \  \____\ \  \ \  \ \  \_\\ \ \  \ \  \____\ \  \____\ \  \ \  \ \  \____  
   \ \_______\ \__\ \__\ \_______\ \__\ \_______\ \_______\ \__\ \__\ \_______\
    \|_______|\|__|\|__|\|_______|\|__|\|_______|\|_______|\|__|\|__|\|_______|
                """+  Style.RESET_ALL)
print("Do you want to play with an AI [1] or a person [2]")

                                                                               
isAi =0
input34 = int(input())
print(" ")
print(" ")

if input34 == 1:
  isAi=1
if input34 ==2:
  isAi =2

S = Game(2)
S.startdeck()
# S.printval()
# S.printdeck()
S.startplayers()
# S.printval()

# S.printval()
# S.startplayers(6)
# print(Game.deck)

x = 4
turns = 0
knock = 0
while (((S.getscore(1) < 31) and (S.getscore(2) < 31)) and knock != 2):
   if (turns % 2 == 0):
       #print("____________________________________Player1__________________________________________")
      #  S.printval()
      #  S.printplay_val()
       S.print_main(1)

       S.turn_player(1)
       S.getscore(1)
       # S.printval()

       if (knock == 1):
           print("Last turn before knock")
           knock = 2
           print(knock)
       elif (knock == 0):
           print("Do you want to knock? [Y] / [N]")
           a = input()

           if ((a == "y") or (a == 'Y')):
               print("Player1 knocked")
               knock = 1
           print(" ")
           print(" ")
           #print("__________________________________________________________________")

       turns = turns + 1

       # elif ((a== "n") or (a== 'N')):
       #     g = 7
       #     break
   elif ((turns % 2 == 1) and isAi==1):
        # print("____________________________________Player2__________________________________________")
        # S.printval()
        # S.printplay_val()
        S.print_main(2)
        # S.printdeck()

        S.artificial_intelligence()
        S.getscore(2)
        # S.printdeck()

        if (knock == 1):
            print("Last turn before knock")
            knock = 2
            print(knock)
        elif (knock == 0):
            print("Do you want to knock? [Y] / [N]")
            #a = input()
            a = "n"

            if ((a == "y") or (a == 'Y')):
                print("Player 1 knocked")
                knock = 1
            print(" ")
            print(" ")
            #print("__________________________________________________________________")

        turns = turns + 1


   elif (turns % 2 == 1) and isAi==2:
      #  print("____________________________________Player2__________________________________________")
      #  S.printval()
      #  S.printplay_val()
       
       S.print_main(2)

       # S.printdeck()
       S.turn_player(2)
       S.getscore(2)
       # S.printdeck()

       if (knock == 1):
           print("Last turn before knock")
           knock = 2
           print(knock)
       elif (knock == 0):
           print("Do you want to knock? [Y] / [N]")
           a = input()
           
           if ((a == "y") or (a == 'Y')):
               print("Player 1 knocked")
               knock = 1
           print(" ")
           print(" ")
           #print("__________________________________________________________________")
       turns = turns + 1

       # elif ((a== "n") or (a== 'N')):
       #     g = 7
       #     break


if (S.getscore(1) > S.getscore(2)):
   print("Player 1")
   print(r"""
         _          __
 _    __(_)__  ___ / /
| |/|/ / / _ \(_-</_/ 
|__,__/_/_//_/___(_)  
  """)                    
elif (S.getscore(1) < S.getscore(2)):
   print("Player 2")
print(r"""            
         _          __
 _    __(_)__  ___ / /
| |/|/ / / _ \(_-</_/ 
|__,__/_/_//_/___(_)  
 """)                     
