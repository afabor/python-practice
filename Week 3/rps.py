from random import choice

# class Player():
#     def __init__(self):
#         self.move = None

#     def player_move(move):
#         if move == 1:
#             return 'Rock'
#         elif move == 2:
#             return 'Paper'
#         elif move == 3:
#             return 'Scissors'
#         else:
#             return 'Invalid Input'
        
#     def comp_move():
#         comp_choice = random.randint(1,3)

#         if comp_choice == 1:
#             return 'Rock'
#         elif comp_choice == 2:
#             return 'Paper'
#         elif comp_choice == 3:
#             return 'Scissors'
        
   
        
#     print(player_move(4))
#     print(comp_move())
user_options = ['Rock', 'Paper', 'Scissors']
 
human_choice = input('What do you choose? "Rock", "Paper" or "Scissors"?\n')
 
computer_choice = choice(user_options)
 
print(f'Computer chose {computer_choice}')
 
 
if human_choice == 'Rock' and computer_choice == 'Scissors':
    print('You win!!')
elif computer_choice == 'Rock' and human_choice == 'Scissors':
    print('You lose!')
elif human_choice == 'Paper' and computer_choice == 'Rock':
    print('You win!')
elif computer_choice == 'Paper' and human_choice == 'Rock':
    print('You lose!')
elif human_choice == 'Scissors' and computer_choice == 'Paper':
    print(' You win!')
elif computer_choice == 'Scissors' and human_choice == 'Paper':
    print('You lose!')    
elif human_choice == computer_choice:
    print('It\'s a draw!')
else:
    print('You typed an invalid choice.')