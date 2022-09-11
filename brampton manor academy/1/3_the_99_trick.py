
print(' We are going to play a game.', '\n',
      'I want you to pick a number then do a series of calculations.', '\n',
      'I bet I know what the result of those calculations will be!')

answer = int(input('This will be the answer. Select a number between 10-49: '))
player_number = int(input('Pick any number between 50-99: '))

factor = 99 - answer
result = factor + answer
result = (result - 100) + 1
final_result = player_number - result

if final_result == answer:
    print(f'I said the answer was {answer} and the calculation result is {final_result}')
else:
    print('error, try again')


