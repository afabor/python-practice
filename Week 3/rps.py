from random import choice

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