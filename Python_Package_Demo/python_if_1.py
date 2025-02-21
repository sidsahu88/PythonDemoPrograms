house_price = 1000000
has_good_credit = True


if has_good_credit:
    downpayment = house_price*10/100
else:
    downpayment = house_price*20/100

print(f"Downpayment: ${downpayment}")


has_high_income = True
has_criminal_record = True

if has_high_income and has_good_credit and not has_criminal_record:
    print("Eligible for loan.")
else:
    print("Not eligible for loan.")


name = "Sid"
name_len = len(name)

if name_len < 3:
    print("Name cannot be less than 3 characters.")
elif name_len > 50:
    print("Name cannot be more than 50 Characters.")
else:
    print(f"Hi {name}!")
