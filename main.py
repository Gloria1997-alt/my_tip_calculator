
print("welcome to the Gloria's tip calculator")
bill = float(input("what is the total bill? $"))

tip = int(input("what percentage tip would you like to give? 10, 12 or 15?"))
people = int(input("how many people should split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"each person will pay ${final_amount}")

print(total_bill)

bill_with_tip = tip / 100 * bill +bill
print(bill_with_tip)