import random

def guess_number(seed_num=None):
    """Generate a random and tell user whether their guessed number is correct"""
    """ seed_num으로 seed값을 고정 후 진행 """
    random.seed(seed_num)
    a = random.randrange(100)
    print(a)
    while True:
        b=int(input('Enter your guess: '))
        if a==b:
            print('You got it!')
            break
        elif a>b:
            print('Too small!')
        else:
            print('Too big!')


if __name__ == '__main__':
    guess_number()
