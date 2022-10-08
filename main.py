# adding = 4 + 3
# print(adding)

# subtraction = 8 - 9
# print(subtraction)

# multiplication = 4 * 32
# print(multiplication)

# division = 50 / 5
# print(division)

# squared = 5**2
# print(squared)

# modulo = 15 % 4
# print(modulo)

# divisor = 15 // 2
# print(divisor)

# Fix My Code

# multiplication
# multiplication = 3.4 * 6.8
# print(multiplication)

# division
# division = 2467 / 4673
# print(division)

#raise 10 to the power of 2

# squared = 10**2
# print(squared)

# print the remainder when 343 is divided by 4

# remainder = 343 % 4
# print(remainder)

# print("343 // 100")

# myBill = float(input("What was the bill?: "))
# numberOfPeople = int(input("How many people?: "))
# answer = round(myBill / numberOfPeople, 4)
# print("You all owe", answer)

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent?" ))


bill_with_tip = tip / 100 * myBill + myBill
bill_per_person = bill_with_tip / numberOfPeople
final_amount = round(bill_per_person, 2)


print("You all owe", final_amount)