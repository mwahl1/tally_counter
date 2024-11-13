# hopefully this works out to be a working tip calculator, i know it probably is easier in other langs but i like python the best



# Tip calculator in Python

# Get the total bill amount from the user
bill_amount = float(input('How much was the bill, including the tax? '))
print(f'The bill comes out to ${bill_amount:.2f} before tip.')

# Get the tip percentage from the user
tip_percent = float(input('What % would you like to tip? '))

# Calculate the tip amount
tip_total = bill_amount * (tip_percent / 100)

# Calculate the total amount with tip
total_with_tip = bill_amount + tip_total

print(f'The tip amount is: ${tip_total:.2f}')
print(f'The total for the whole bill is: ${total_with_tip:.2f}')

# find out how many people are splittng the bill
ppl_split = int(input('How many people are splitting the bill?'))

# this is the total per person

total_person = total_with_tip / ppl_split

# calc the total per person

bill_split = print(f'The total is: ${total_person:.2f} ')


