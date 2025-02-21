guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess_no = int(input("Guess the no.: "))
    if guess_no == 9:
        print("Congratulations, you won.")
        break
    guess_count += 1
else:
    print("Sorry, you lost.")
