weight = int(input("Weight: "))
type = input("(L)bs or (K)gs: ")

if type == 'L' or type == 'l':
    print(f"You are {weight/2.2} kgs.")
elif type.upper() == 'K':
    print(f"You are {weight*2.2} pounds.")
else:
    print("Enter valid weight type.")
