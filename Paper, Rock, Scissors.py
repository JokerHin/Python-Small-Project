#'Rock', 'Paper', 'Scissors'
import random
mylist = ['Rock', 'Paper', 'Scissors']
user = input('Please select Rock, Paper or Scissors: ')
bot = random.choice(mylist)
print(bot)
if user == 'Rock' and bot == 'Rock':
    print('tie, try again')
if user == 'Rock' and bot == 'Scissors':
    print('You win')
if user == 'Rock' and bot == 'Paper':
    print('You lose')
if user == 'Paper' and bot == 'Paper':
    print('tie, try again!')
if user == 'Paper' and bot == 'Scissors':
    print('You lose')
if user == 'Paper' and bot == 'Rock':
    print('You Win')
if user == 'Scissors' and bot == 'Scissors':
    print('tie, try again')
if user == 'Scissors' and bot == 'Rock':
    print('You lose')
if user == 'Scissors' and bot == 'Paper':
    print('You win')
if user not in mylist:
    print('Something error, please try again!')





