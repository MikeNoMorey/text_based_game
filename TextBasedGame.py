#Zombie Apocolypse Game Script // Mike Morey // 09/18/21
print('Would you like to play the Zombie Apocolypse mini game???')
user_input = input('yes / no: ')

import sys
import time

#Choice to play game
if user_input == 'yes':
    game_ongoing = True

#Rooms & Items 
    rooms = { 
        'Entryway': {'south': 'Living Room', 'east': 'Dining Room', 'west': 'Garage'},
        'Garage': {'south':'Bedroom', 'east':'Entryway'},
        'Dining Room': {'south':'Kitchen', 'west': 'Entryway'},
        'Living Room': {'south':'Basement','east': 'Kitchen', 'north': 'Entryway'},
        'Kitchen': {'west':'Living Room','north':'Dining Room'},
        'Bathroom': {'north':'Bedroom'},
        'Bedroom': {'north': 'Garage', 'south': 'Bathroom'},
        'Basement': {'north': 'Living Room'}
    }

#Welcome Screen Info
    print('')
    print('-- Welcome to the ZOMBIE APOCOLYPSE game! --')
    print('-- Protect your home by collecting all 6 required items! --')
    print('-- OR BE OVER RUN BY THE ZOMBIE HOARD!!! --')
    print('')
    print('TIP: AVOID THE BASEMENT UNTIL YOUR INVENTORY IS FULL!')

#Starting Room & Inventory
    current_room = 'Entryway'
    player_move = ''
    current_inventory = []
    
#Player Commands & Inventory Functions
    def main():
        print('')
        print('-'*50)
        print('** Inventory: {}'.format(current_inventory))
        print('** Controls: north // south // east // west // exit // attack')
        print('** Inventory Controls: grab \'item name\'')
        print()
        print('You are in the {}\n'.format(current_room))
        print('-'*50)

        #Object Discovery, Functionality, & Appending to Player's Inventory

        #Basement Elite Zombie Commands
        if 'Basement' == current_room:
            print('*' * 32)
            print('*** OH NO ITS A ZOMBIE ELITE ***')
            print('*' * 32, '\n')
            if len(current_inventory) == 6:
                print('Are you just going to let the Zombies take over the house!')
                print('You have all the tools now use them!')
                user_inputs = input('\n Enter your next move: ')
                if user_inputs == 'attack':
                    print('\n ***Congrats you beat the game and saved your home!***')
                    print('Hopefully now you can enjoy the rest of this apocolpyse in peace...')
                    sys.exit(0)
                else:
                    print('Invalid entry, try again...')
            else:
                print('You forgot to bring the correct items with you!')
                print('The zombie elite ate you!')
                print('Game over')
                time.sleep(5)
                sys.exit(0)

        #Garage Item Commands
        elif 'Garage' == current_room and 'hammer & nails' not in current_inventory:
            print('You found the \'hammer & nails\'\n')
            garage = True
            while garage == True:
                player_action = input('What would you like to do: ')
                if player_action == 'grab hammer & nails':
                    print('\n ***You got it champ!*** ')
                    current_inventory.append('hammer & nails')
                    main()
                    garage = False
                else:
                    print('Invalid entry, try again...')
                    garage = True

        #Bedroom Item Commands
        elif 'Bedroom' == current_room and 'shield' not in current_inventory:
            print('Great, you found the \'shield\'!!!\n')
            bedroom = True
            while bedroom == True:
                player_action = input('What would you like to do: ')
                if player_action == 'grab shield':
                    print('\n ***Yes sir, you got it!*** ')
                    current_inventory.append('shield')
                    main()
                    bedroom = False
                else:
                    print('Invalid Entry, try again...')
                    bedroom = True

        #Bathroom Item Commands
        elif 'Bathroom' == current_room and 'toothpick' not in current_inventory:
            print('Nice you found a \'toothpick\'!!! Questionable... but I like it.\n')
            bathroom = True
            while bathroom == True:
                player_action = input('What would you like to do: ')
                if player_action == 'grab toothpick':
                    print('\n ***Grabbed toothpick*** ')
                    current_inventory.append('toothpick')
                    main()
                    bathroom = False
                else:
                    print('Invalid entry, try again...')
                    bathroom = True

        #Living Room Item Commands
        elif 'Living Room' == current_room and 'sword' not in current_inventory:
            print('Wonderful you found the \'sword\'!!!\n')
            livingroom = True
            while livingroom ==True:
                player_action = input('What would you like to do: ')
                if player_action == 'grab sword':
                    print('\n ***You now wield a sword, WOOHOO!*** ')
                    current_inventory.append('sword')
                    main()
                    livingroom = False
                else:
                    print('Invalid entry, try again...')
                    livingroom = True

        #Dining Room Item Commands
        elif 'Dining Room' == current_room and 'wood barricades' not in current_inventory: 
            print('Great, you found \'wood barricades\' to protect the house!\n')
            diningroom = True
            while diningroom == True:
                player_action = input('What would you like to do: ')
                if player_action == 'grab wood barricades':
                    print('\n ***Great you got the barricades, now we are getting somewhere!*** ')
                    current_inventory.append('wood barricades')
                    main()
                    diningroom = False
                else:
                    print('Invalid entry, try again...')
                    diningroom = True

        #Kitchen Item Commands
        elif 'Kitchen' == current_room and 'snack' not in current_inventory:
            print('OMG a \'snack\'!!!')
            print('EAT UP!\n')
            kitchen = True
            while kitchen == True:
                player_action = input('We are waiting, eat up before the zombies eat you!: ')
                if player_action == 'grab snack':
                    print('\nNOM NOM NOM.. YUMMY')
                    print('\nBetter save some for later!')
                    print('Now that your nice and full let\'s keep moving, there is work to do.')
                    current_inventory.append('snack')
                    main()
                    kitchen = False
                else:
                    print('Invalid entry, try again...')
                    kitchen = True

#Player Movement & Mapping Between Rooms
    while current_room != 'exit' and SystemExit != True:
        main()
        player_move = input('Enter your move: ')

        if player_move in rooms[current_room]:
            current_room = rooms[current_room][player_move]

            #Final Room Message to Player
            if 'Basement' == current_room:
                print('Are you sure your ready to enter? | Enter yes / no: ')
                response = input()

                if response == 'yes':
                    current_room = 'Basement'
                elif response == 'no':
                    current_room = 'Living Room'
                else:
                    print('-- INVALID INPUT --')
                    print('-- Sending you back to the previous room. --')
                    current_room = 'Living Room'

#In-Game Exit Command
        elif player_move == 'exit':
            current_room != rooms[current_room]
            current_room = 'exit'
            game_ongoing = False
            print('Leaving game!')
            
        else:
            print('-- INVALID INPUT --')

#Exit Game / Denial to play
elif user_input == 'no':
    print('Okay, another time then!')

else:
    game_ongoing = False
    print('Exiting game.')