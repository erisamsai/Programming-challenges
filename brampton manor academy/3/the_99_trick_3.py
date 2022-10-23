print(" We are going to play a game.",
      '\n', "I want you to pick a number then do a series of calculations.",
      '\n', "I bet I know what the result of those calculations will be!", '\n')


def your_part():
    answer = int(input(" This will be the answer. Select a number between 10-49: "))
    return answer


def friend_part():
    friend_number = int(input(' Pick any number between 50-99: '))
    return friend_number


def calculation(answer, friend_number):
    factor = 99 - answer
    result = factor + friend_number
    result = (result - 100) + 1
    final_result = friend_number - result
    return final_result


def end_game(answer, final_result):
    if final_result == answer:
         print(f' I said the answer was {answer} and the calculation result is {final_result}.')
    else:
        print('error, try again')



if __name__ == "__main__":
    answer = your_part()
    friend_number = friend_part()
    final_result = calculation(answer, friend_number)
    end_game(answer, final_result)
