import random
def main():
    guess1 = 0
    guess2 = 0
    guess12 = 0
    guess22 = 0
    guess13 = 0
    guess23 = 0
    print ("Welcome to the Guessing Game!")
    print ("")
    print ("1. Easy(10), 2. Medium(20), 3. Hard(100)")
    levelnumber = input("Choose what level you would like to play:")
    print ("")
#EASY (10,10)
    if levelnumber == 1:
        print ("ROUND ONE")
        x1 = random.randrange(1, 11,1)
        x2 = random.randrange (1,11,1)
        while guess1 < 10:
            guess1 = guess1 + 1
            number11 = input ("Player One - Enter a number between 1-10:")
            if number11 < x1:
                print ("The number you choose was too low.")
            if number11 > x1:
                print ("The number you choose was too high.")
            if number11 == x1:
                break
        if guess1 == 10:
            print ("Sorry you did not guess the right number.")
        if guess1 < 10:
            print ("Yay you choose the correct number!")
        print ("")
        while guess2 < 10:
            guess2 = guess2 + 1
            number12 = input("Player Two - Enter a number between 1-10:")
            if number12 < x2:
                print ("The number you choose was too low.")
            if number12 > x2:
                print ("The number you choose was too high.")
            if number12 == x2:
                break
        if guess2 == 10:
            print ("Sorry you did not guess the right number.")
        if guess2 < 10:
            print ("Yay you choose the correct number!")
        print ("")
        if guess1 == guess2:
            print ("Tie For Round One!")
        if guess1 < guess2:
            print ("Player One Wins Round One!")
        if guess1 > guess2:
            print ("Player Two Wins Round One!")
        print ("")
        print ("ROUND TWO")
        x1 = random.randrange(1, 11, 1)
        x2 = random.randrange(1, 11, 1)
        while guess12 < 10:
            guess12 = guess12 + 1
            number11 = input("Player One - Enter a number between 1-10:")
            if number11 < x1:
                print ("The number you choose was too low.")
            if number11 > x1:
                print ("The number you choose was too high.")
            if number11 == x1:
                break
        if guess12 == 10:
            print ("Sorry you did not guess the right number.")
        if guess12 < 10:
            print ("Yay you choose the correct number!")
        print ("")
        while guess22 < 10:
            guess22 = guess22 + 1
            number12 = input("Player Two - Enter a number between 1-10:")
            if number12 < x2:
                print ("The number you choose was too low.")
            if number12 > x2:
                print ("The number you choose was too high.")
            if number12 == x2:
                break
        if guess22 == 10:
            print ("Sorry you did not guess the right number.")
        if guess22 < 10:
            print ("Yay you choose the correct number!")
        print ("")
        if guess12 == guess22:
            print ("Tie For Round Two!")
        if guess12 < guess22:
            print ("Player One Wins Round Two!")
        if guess12 > guess22:
            print ("Player Two Wins Round Two!")
        print ("")
        print ("ROUND THREE")
        x1 = random.randrange(1, 11, 1)
        x2 = random.randrange(1, 11, 1)
        while guess13 < 10:
            guess13 = guess13 + 1
            number11 = input("Player One - Enter a number between 1-10:")
            if number11 < x1:
                print ("The number you choose was too low.")
            if number11 > x1:
                print ("The number you choose was too high.")
            if number11 == x1:
                break
        if guess13 == 10:
            print ("Sorry you did not guess the right number.")
        if guess13 < 10:
            print ("Yay you choose the correct number!")
        print ("")
        while guess23 < 10:
            guess23 = guess23 + 1
            number12 = input("Player Two - Enter a number between 1-10:")
            if number12 < x2:
                print ("The number you choose was too low.")
            if number12 > x2:
                print ("The number you choose was too high.")
            if number12 == x2:
                break
        if guess23 == 10:
            print ("Sorry you did not guess the right number.")
        if guess23 < 10:
            print ("Yay you choose the correct number!")
        print ("")
        if guess13 == guess23:
            print ("Tie For Round Three!")
        if guess13 < guess23:
            print ("Player One Wins Round Three!")
        if guess13 > guess23:
            print ("Player Two Wins Round Three!")
        #WINNERS OF THE LEVEL
        print ("")
        #First part of the tree chart
        if guess1 < guess2: #1
            if guess12 < guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2: #2
            if guess12 < guess13:
                if guess22 > guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2: #3
            if guess12 > guess13:
                if guess22 == guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2: #4
            if guess12 > guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2: #5
            if guess12 > guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 < guess2: #6
            if guess12 > guess13:
                if guess22 == guess23:
                    print ("TIE!")
        if guess1 < guess2: #7
            if guess12 == guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2: #8
            if guess12 == guess13:
                if guess22 > guess23:
                    print ("TIE!")
        if guess1 < guess2: #9
            if guess12 == guess13:
                if guess22 == guess23:
                    print ("PLAYER ONE WINS!")
        #Second part of the tree chart
        if guess1 > guess2: #1
            if guess12 < guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 > guess2: #2
            if guess12 < guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2: #3
            if guess12 < guess13:
                if guess22 == guess23:
                    print ("TIE!")
        if guess1 > guess2: #4
            if guess12 > guess13:
                if guess22 < guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2: #5
            if guess12 > guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2: #6
            if guess12 > guess13:
                if guess22 == guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2: #7
            if guess12 == guess13:
                if guess22 < guess23:
                    print ("TIE!")
        if guess1 > guess2: #8
            if guess12 == guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2: #9
            if guess12 == guess13:
                if guess22 == guess23:
                    print ("PLAYER TWO WINS!")
        #Third part of the tree chart
        if guess1 == guess2: #1
            if guess12 < guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 == guess2: #2
            if guess12 < guess13:
                if guess22 > guess23:
                    print ("TIE!")
        if guess1 == guess2: #3
            if guess12 < guess13:
                if guess22 == guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 == guess2: #4
            if guess12 > guess13:
                if guess22 < guess23:
                    print ("TIE!")
        if guess1 == guess2: #5
            if guess12 > guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 == guess2: #6
            if guess12 > guess13:
                if guess22 == guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 == guess2: #7
            if guess12 == guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 == guess2: #8
            if guess12 == guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 == guess2: #9
            if guess12 == guess13:
                if guess22 == guess23:
                    print ("TIE!")
# MEDIUM (20,15)
    if levelnumber == 2:
        print ("ROUND ONE")
        x3 = random.randrange(1, 21,1)
        x4 = random.randrange (1,21,1)
        while guess1 < 15:
            guess1 = guess1 + 1
            number21 = input ("Player One - Enter a number between 1-20:")
            if number21 < x3:
                print ("The number you choose was too low.")
            if number21 > x3:
                print ("The number you choose was too high.")
            if number21 == x3:
                break
        if guess1 == 15:
            print ("Sorry you did not guess the right number.")
        if guess1 < 15:
            print ("Yay you choose the correct number!")
        print ("")
        while guess2 < 15:
            guess2 = guess2 + 1
            number22 = input("Player Two - Enter a number between 1-20:")
            if number22 < x4:
                print ("The number you choose was too low.")
            if number22 > x4:
                print ("The number you choose was too high.")
            if number22 == x4:
                break
        if guess2 == 15:
            print ("Sorry you did not guess the right number.")
        if guess2 < 15:
            print ("Yay you choose the correct number!")
        print ("")
        if guess1 == guess2:
            print ("Tie For Round One!")
        if guess1 < guess2:
            print ("Player One Wins Round One!")
        if guess1 > guess2:
            print ("Player Two Wins Round One!")
        print ("")
        print ("ROUND TWO")
        x3 = random.randrange(1, 21, 1)
        x4 = random.randrange(1, 21, 1)
        while guess12 < 15:
            guess12 = guess12 + 1
            number21 = input("Player One - Enter a number between 1-20:")
            if number21 < x3:
                print ("The number you choose was too low.")
            if number21 > x3:
                print ("The number you choose was too high.")
            if number21 == x3:
                break
        if guess12 == 15:
            print ("Sorry you did not guess the right number.")
        if guess12 < 15:
            print ("Yay you choose the correct number!")
        print ("")
        while guess22 < 15:
            guess22 = guess22 + 1
            number22 = input("Player Two - Enter a number between 1-20:")
            if number22 < x4:
                print ("The number you choose was too low.")
            if number22 > x4:
                print ("The number you choose was too high.")
            if number22 == x4:
                break
        if guess22 == 15:
            print ("Sorry you did not guess the right number.")
        if guess22 < 15:
            print ("Yay you choose the correct number!")
        print ("")
        if guess12 == guess22:
            print ("Tie For Round Two!")
        if guess12 < guess22:
            print ("Player One Wins Round Two!")
        if guess12 > guess22:
            print ("Player Two Wins Round Two!")
        print ("")
        print ("ROUND THREE")
        x3 = random.randrange(1, 21, 1)
        x4 = random.randrange(1, 21, 1)
        while guess1 < 15:
            guess13 = guess13 + 1
            number21 = input("Player One - Enter a number between 1-20:")
            if number21 < x3:
                print ("The number you choose was too low.")
            if number21 > x3:
                print ("The number you choose was too high.")
            if number21 == x3:
                break
        if guess13 == 15:
            print ("Sorry you did not guess the right number.")
        if guess13 < 15:
            print ("Yay you choose the correct number!")
        print ("")
        while guess23 < 15:
            guess23 = guess23 + 1
            number22 = input("Player Two - Enter a number between 1-20:")
            if number22 < x4:
                print ("The number you choose was too low.")
            if number22 > x4:
                print ("The number you choose was too high.")
            if number22 == x4:
                break
        if guess23 == 15:
            print ("Sorry you did not guess the right number.")
        if guess23 < 15:
            print ("Yay you choose the correct number!")
        print ("")
        if guess13 == guess23:
            print ("Tie For Round Three!")
        if guess13 < guess23:
            print ("Player One Wins Round Three!")
        if guess13 > guess23:
            print ("Player Two Wins Round Three!")
        # WINNERS OF THE LEVEL
        print ("")
        #First part of the tree chart
        if guess1 < guess2: #1
            if guess12 < guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2: #2
            if guess12 < guess13:
                if guess22 > guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2: #3
            if guess12 > guess13:
                if guess22 == guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2: #4
            if guess12 > guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2: #5
            if guess12 > guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 < guess2: #6
            if guess12 > guess13:
                if guess22 == guess23:
                    print ("TIE!")
        if guess1 < guess2: #7
            if guess12 == guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2: #8
            if guess12 == guess13:
                if guess22 > guess23:
                    print ("TIE!")
        if guess1 < guess2: #9
            if guess12 == guess13:
                if guess22 == guess23:
                    print ("PLAYER ONE WINS!")
        #Second part of the tree chart
        if guess1 > guess2: #1
            if guess12 < guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 > guess2: #2
            if guess12 < guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2: #3
            if guess12 < guess13:
                if guess22 == guess23:
                    print ("TIE!")
        if guess1 > guess2: #4
            if guess12 > guess13:
                if guess22 < guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2: #5
            if guess12 > guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2: #6
            if guess12 > guess13:
                if guess22 == guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2: #7
            if guess12 == guess13:
                if guess22 < guess23:
                    print ("TIE!")
        if guess1 > guess2: #8
            if guess12 == guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2: #9
            if guess12 == guess13:
                if guess22 == guess23:
                    print ("PLAYER TWO WINS!")
        #Third part of the tree chart
        if guess1 == guess2:#1
            if guess12 < guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 == guess2: #2
            if guess12 < guess13:
                if guess22 > guess23:
                    print ("TIE!")
        if guess1 == guess2: #3
            if guess12 < guess13:
                if guess22 == guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 == guess2: #4
            if guess12 > guess13:
                if guess22 < guess23:
                    print ("TIE!")
        if guess1 == guess2: #5
            if guess12 > guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 == guess2: #6
            if guess12 > guess13:
                if guess22 == guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 == guess2: #7
            if guess12 == guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 == guess2: #8
            if guess12 == guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 == guess2: #9
            if guess12 == guess13:
                if guess22 == guess23:
                    print ("TIE!")
# HARD (100,30)
    if levelnumber == 3:
        print ("ROUND ONE")
        x5 = random.randrange(1, 101, 1)
        x6 = random.randrange(1,101,1)
        while guess1 < 30:
            guess1 = guess1 + 1
            number31 = input("Player One - Enter a number between 1-100:")
            if number31 < x5:
                print ("The number you choose was too low.")
            if number31 > x5:
                    print ("The number you choose was too high.")
            if number31 == x5:
                break
        if guess1 == 30:
            print ("Sorry you did not guess the correct number.")
        if guess1 < 30:
            print ("Yay you choose the correct number!")
        print ("")
        while guess2 <30:
            guess2 = guess2 + 1
            number32 = input("Player Two - Enter a number between 1-100:")
            if number32 < x6:
                print ("The number you choose was too low.")
            if number32 > x6:
                print ("The number you choose was too high.")
            if number32 == x6:
                break
        if guess2 == 30:
            print ("Sorry you did not guess the right number.")
        if guess2 < 30:
            print ("Yay you choose the correct number!")
        print ("")
        if guess1 == guess2:
            print ("Tie For Round One!")
        if guess1 < guess2:
            print ("Player One Wins Round One!")
        if guess1 > guess2:
            print ("Player Two Wins Round One!")
        print ("")
        print ("ROUND TWO")
        x5 = random.randrange(1, 101, 1)
        x6 = random.randrange(1, 101, 1)
        while guess12 < 30:
            guess12 = guess12 + 1
            number31 = input("Player One - Enter a number between 1-100:")
            if number31 < x5:
                print ("The number you choose was too low.")
            if number31 > x5:
                print ("The number you choose was too high.")
            if number31 == x5:
                break
        if guess12 == 30:
            print ("Sorry you did not guess the correct number.")
        if guess12 < 30:
            print ("Yay you choose the correct number!")
        print ("")
        while guess22 < 30:
            guess22 = guess22 + 1
            number32 = input("Player Two - Enter a number between 1-100:")
            if number32 < x6:
                print ("The number you choose was too low.")
            if number32 > x6:
                print ("The number you choose was too high.")
            if number32 == x6:
                break
        if guess22 == 30:
            print ("Sorry you did not guess the right number.")
        if guess22 < 30:
            print ("Yay you choose the correct number!")
        print ("")
        if guess12 == guess22:
            print ("Tie For Round Two!")
        if guess12 < guess22:
            print ("Player One Wins Round Two!")
        if guess12 > guess22:
            print ("Player Two Wins Round Two!")
        print ("")
        print ("ROUND THREE")
        x5 = random.randrange(1, 101, 1)
        x6 = random.randrange(1, 101, 1)
        while guess13 < 30:
            guess13 = guess13 + 1
            number31 = input("Player One - Enter a number between 1-100:")
            if number31 < x5:
                print ("The number you choose was too low.")
            if number31 > x5:
                print ("The number you choose was too high.")
            if number31 == x5:
                break
        if guess13 == 30:
            print ("Sorry you did not guess the correct number.")
        if guess13 < 30:
            print ("Yay you choose the correct number!")
        print ("")
        while guess23 < 30:
            guess23 = guess23 + 1
            number32 = input("Player Two - Enter a number between 1-100:")
            if number32 < x6:
                print ("The number you choose was too low.")
            if number32 > x6:
                print ("The number you choose was too high.")
            if number32 == x6:
                break
        if guess23 == 30:
            print ("Sorry you did not guess the right number.")
        if guess23 < 30:
            print ("Yay you choose the correct number!")
        print ("")
        if guess13 == guess23:
            print ("Tie For Round Three!")
        if guess13 < guess23:
            print ("Player One Wins Round Three!")
        if guess13 > guess23:
            print ("Player Two Wins Round Three!")
        # WINNERS OF THE LEVEL
        print ("")
        # First part of the tree chart
        if guess1 < guess2:  # 1
            if guess12 < guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2:  # 2
            if guess12 < guess13:
                if guess22 > guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2:  # 3
            if guess12 > guess13:
                if guess22 == guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2:  # 4
            if guess12 > guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2:  # 5
            if guess12 > guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 < guess2:  # 6
            if guess12 > guess13:
                if guess22 == guess23:
                    print ("TIE!")
        if guess1 < guess2:  # 7
            if guess12 == guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 < guess2:  # 8
            if guess12 == guess13:
                if guess22 > guess23:
                    print ("TIE!")
        if guess1 < guess2:  # 9
            if guess12 == guess13:
                if guess22 == guess23:
                    print ("PLAYER ONE WINS!")
        # Second part of the tree chart
        if guess1 > guess2:  # 1
            if guess12 < guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 > guess2:  # 2
            if guess12 < guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2:  # 3
            if guess12 < guess13:
                if guess22 == guess23:
                    print ("TIE!")
        if guess1 > guess2:  # 4
            if guess12 > guess13:
                if guess22 < guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2:  # 5
            if guess12 > guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2:  # 6
            if guess12 > guess13:
                if guess22 == guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2:  # 7
            if guess12 == guess13:
                if guess22 < guess23:
                    print ("TIE!")
        if guess1 > guess2:  # 8
            if guess12 == guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 > guess2:  # 9
            if guess12 == guess13:
                if guess22 == guess23:
                    print ("PLAYER TWO WINS!")
        # Third part of the tree chart
        if guess1 == guess2:  # 1
            if guess12 < guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 == guess2:  # 2
            if guess12 < guess13:
                if guess22 > guess23:
                    print ("TIE!")
        if guess1 == guess2:  # 3
            if guess12 < guess13:
                if guess22 == guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 == guess2:  # 4
            if guess12 > guess13:
                if guess22 < guess23:
                    print ("TIE!")
        if guess1 == guess2:  # 5
            if guess12 > guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 == guess2:  # 6
            if guess12 > guess13:
                if guess22 == guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 == guess2:  # 7
            if guess12 == guess13:
                if guess22 < guess23:
                    print ("PLAYER ONE WINS!")
        if guess1 == guess2:  # 8
            if guess12 == guess13:
                if guess22 > guess23:
                    print ("PLAYER TWO WINS!")
        if guess1 == guess2:  # 9
            if guess12 == guess13:
                if guess22 == guess23:
                    print ("TIE!")

    print ("")
    print ("The game has ended. Would you like to play again? 1.Yes, 2.No")
    again = input("Please enter your choice:")
    if again == 1:
        main()
    else:
        print ("")
        print ("Thanks for playing!")
main()
