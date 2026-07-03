#BONUS IDEAS USED----
#-----BOTH PLAYERS PICK UP 1 CARD-------------------------
#-----WINNER BY A COMBINATION OF SUIT AND VALUE-----------
#-----PLAYERS PICK UP MULTIPLE CARDS----------------------
#-----JOKER CARD IN THE GAMEPLAY--------------------------
#-----INNOVATIVE WAYS TO DEAL CARDS-----------------------
#-----INCORPORATE RANDOMNESS IN DEALING CARDS-------------


import random

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A']        
suits = ['C', 'D', 'H', 'S']       
weights = [0, 10,20, 30]

deck_of_cards = []; 

def Determine_winner(card_p, card_c):
    if card_p!= 'ZZ' and card_c != 'ZZ':
        if cards.index(card_p[1])>cards.index(card_c[1]):
             return 1
    
        elif cards.index(card_p[1])<cards.index(card_c[1]):
            return 2
        else:
            return 0
    else:
        if card_p== 'ZZ' and card_c != 'ZZ':
            return 1
        elif  card_p!= 'ZZ' and card_c == 'ZZ':
            return 2
        else: 
            return 0 


for kk in range(len(suits)):
    for jj in range(len(cards)):
        deck_of_cards.append(suits[kk]+cards[jj])


print('Unshuffled Deck:')
for kk in range(len(deck_of_cards)):
    print(deck_of_cards[kk], end = ' ')
print()
    
random.shuffle(deck_of_cards) 

print('Shuffled Deck:')
for kk in range(len(deck_of_cards)):
    print(deck_of_cards[kk], end = ' ')




done = False
while not done:
    pc_toss = random.choices(deck_of_cards[0:26:1],k=2)
    cc_toss = random.choices(deck_of_cards[26::1],k=2)
    print(cc_toss, pc_toss)
    
    
    
    if (pc_toss[0][0] == pc_toss[1][0]) and (cc_toss[0][0]==cc_toss[1][0]):
       if suits.index(pc_toss[0][0]) > suits.index(cc_toss[0][0]):
        print('Player won')
        done = True
   
       if suits.index(pc_toss[0][0]) < suits.index(cc_toss[0][0]):
         print('Computer won')
         done = True    
    
    elif (pc_toss[0][0] != pc_toss[1][0]) and (cc_toss[0][0]==cc_toss[1][0]):
        print('Computer Won')
        done = True
    elif (pc_toss[0][0] == pc_toss[1][0]) and (cc_toss[0][0]!=cc_toss[1][0]):
        print('Player Won')
        done = True


input()
deck_of_cards.append('ZZ')
deck_of_cards.append('ZZ')
random.shuffle(deck_of_cards)






player_cards = deck_of_cards[0:27:1]
comput_cards = deck_of_cards[27::1]


player_cards = []
table_cards = []
computer_cards = []
n_cd = 1
n_deals = len(deck_of_cards)/(2*n_cd)

for kk in range(int(n_deals)):
    list1 = (deck_of_cards[kk*n_cd*2:kk*n_cd*2+n_cd:1])
    list2 = (deck_of_cards[kk*n_cd*2+n_cd:(kk+1)*n_cd*2:1])
    coin_toss = random.randint(0,1)
    if coin_toss == 0:
        player_cards.extend(list1)
        computer_cards.extend(list2)
    else:
        player_cards.extend(list2)
            computer_cards.extend(list1)
    
    
    
    
    
move_complete = False
game_complete = False
moves_played = 0

while not(game_complete):
  
  move_complete = False
  
  if len(player_cards)<1 or len(computer_cards)<1:
    move_complete = True
    game_complete = True
  
  while not(move_complete):
    if len(player_cards)<1 or len(comput_cards)<1:
      move_complete = True
      break
    card_p = player_cards.pop(0)
    card_c = comput_cards.pop(0)
    print()
    print('Player Card is ...', card_p)
    print('Computer Card is ...', card_c)
    

    table_cards.append(card_p)
    table_cards.append(card_c)
    winner =  Determine_winner(card_p, card_c)
    
    if winner==1:
      print('Player Wins ... ')
      input()
      player_cards.extend(table_cards)
      table_cards.clear()
      move_complete = True
      moves_played = moves_played + 1
    elif winner== 2:
      print('Computer Wins ... ')
      input()
      comput_cards.extend(table_cards)
      table_cards.clear()
      move_complete = True
      moves_played = moves_played + 1
    else:
 
      print("War begins")
      input()
      if len(player_cards)<4 or len(comput_cards)<4:
        move_complete = True
           
      else:
           
        table_cards.extend(player_cards[0:3])
        table_cards.extend(comput_cards[0:3])

                        
        del player_cards[0:3]
        del comput_cards[0:3]
    if moves_played == 100:
      game_complete = True
    print("Player Cards:", len(player_cards), "Computer Cards:", len(comput_cards), "Table Cards:", len(table_cards))    


print()
print()

 
if len(player_cards) > len(comput_cards):
    print('PLAYER is the winner')
elif len(player_cards) < len(comput_cards):
    print('COMPUTER is the winner')
else:
    print('GAME drawn!')