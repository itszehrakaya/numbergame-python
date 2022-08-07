from itertools import permutations
import random
import datetime as dt
import time
ti = int(time.time())
x = dt.datetime.now()
print(x.strftime("%d %b %Y %A %H:%M"))
print("to give up and learn the secret code, please type any string")



def bulls_cows():
    try:
        while True:
            x = int(input("how many digits do you want to play, please type a number among 3️⃣, 4️⃣, 5️⃣: "))

            if x not in range(3, 6):
                print("wrong")
            else:
                break
        perm = permutations(range(0, 10), x)
        Perm_list = [i for i in list(perm)]
        without_0 = [i for i in Perm_list if i[0] != 0]
        Sec_list = random.choice(without_0)





        step = 1
        while True:

            Player_2_guess = input(" guess :")



            guess_list = [int(i) for i in str(Player_2_guess)]
            are_digists_same = [1 for i in guess_list if (guess_list.count(i) > 1)]
            if guess_list[0] == 0:
                print("first digit mustn't be 0️⃣")

            elif len(are_digists_same) != 0:
                print("digits must be different from each other")

            elif len(Sec_list) != len(guess_list):
                print("your guess must contain {} digits.".format(len(Sec_list)))

            else:

                n_digit, bulls = 0 , 0


                bc_intersection_list = [n_digit + 1 for i in guess_list for a in Sec_list if (i == a)]

                while n_digit < len(guess_list):

                    if Sec_list[n_digit] == guess_list[n_digit]:
                        bulls += 1
                    bulls
                    n_digit += 1

                cows = sum(bc_intersection_list) - bulls

                print("{}. {}: {} ️💚 {} 💔  ".format(step, Player_2_guess, bulls, cows))
                step += 1

                if bulls == len(Sec_list):

                    print("congrats 🥳️")
                    ts = int(time.time())
                    y = dt.datetime.now()
                    print(y.strftime("%d %b %Y %A %H:%M"))
                    print("Digits:",x, "Time (sec):",ts - ti,"Attempts:", step - 1, sep = "\n")

                    break


    except ValueError:

        print("hataa")


bulls_cows()




