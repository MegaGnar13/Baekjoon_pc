import random

class BaseballGame:
    def __init__(self, seed_num=None):
        random.seed(seed_num)
        while True:
            a= random.randrange(10)
            b= random.randrange(10)
            c= random.randrange(10)
            if a!=b and b!=c and c!=a:
                break
        self.num=[a,b,c]

        return

    def input_check():
        user=input("What is your guess: ")
        user=user.replace(" ","")
        user=user.replace(",","")

        if user.isdigit():
            if len(user)==3:
                if user[0] != user[1] and user[1] != user[2] and user[2]!= user[0]:
                    num =list(user)
                    for i in range(len(num)):
                        num[i]=int(num[i])
                    return num
                else:
                    return None
            else:
                return None
        else:
            return None



    def check_count(self, usr):
        rand=self.num
        user=usr
        cnt_ball=0
        cnt_strike=0

        for i in range(len(user)):
            if user[i] in rand:
                if user[i] == rand[i]:
                    cnt_strike+=1
                else:
                    cnt_ball+=1
        if cnt_strike==3:
            return "3S 0B"
        else:
            return f"{cnt_strike}S {cnt_ball}B"



        pass

    def play (self):
        while True:
            usr = BaseballGame.input_check()
            if not usr:
                print("Your input is not valid.")
                continue
            else :
                result = self.check_count(usr)
            if result == "3S 0B":
                print("You got it!!")
                break
            else:
                print(result)

if __name__ == "__main__":
    new_game = BaseballGame(2)
    new_game.play()
