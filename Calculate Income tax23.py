# practice how apply logic in it

# How to calculate the income after deducting tax on yearly income

# Conditions are:
# below 3 lac - NO Tax
# Between 3 - 6 lac - 5% Tax
# Between 6 - 9 lac - 10% Tax
# Between 9 - 12 lac - 15% Tax
# Between 12 - 15 lac - 20% Tax
# above  15 lac - 30% Tax

# tax_percentage_1 = 5            # Between 3 - 6 lac - 5% Tax
# tax_percentage_2 = 10           # Between 6 - 9 lac - 10% Tax
# tax_percentage_3 = 15           # Between 9 - 12 lac - 15% Tax
# tax_percentage_4 = 20           # Between 12 - 15 lac - 20% Tax
# tax_percentage_5 = 30           # above  15 lac - 30% Tax
#
# # income = int(input('Enter your income: '))
# # if 900000 <= income <= 1200000
# #     Income_after_deduction = income - income * tax_percentage_1 / 100
#
# income = int(input('Enter your income: '))
# if 0 < income < 300000:
#     print('There will be no Tax')
#     Total_income_after_deduction = income
#
# elif income <= 600000:                                  # if_income = 5,00,000
#     print(f'There will be {tax_percentage_1}% tax')     # 5% tax
#     total_tax = income * tax_percentage_1 / 100         #total_tax = 5,00,000 * 5% / 100
#     Income_after_deduction = income - total_tax         # income = 5,00,00 - 25,000 = 4,75,000
#
# elif income <= 900000:                                # if_income = 5,00,000
#     print(f'There will be {tax_percentage_2}%tax')     # 5% tax
#     total_tax = income * tax_percentage_1 / 100       #total_tax = 5,00,000 * 5% / 100
#     Income_after_deduction = income - total_tax       # income
#
# elif income <= 1200000:
#     print(f'There will be {tax_percentage_3}% tax')
#     total_tax = income * tax_percentage_1 / 100
#     Income_after_deduction = income - total_tax
#
# elif income <= 1500000:
#     print(f'There will be {tax_percentage_4}% tax')
#     total_tax = income * tax_percentage_1 / 100
#     Income_after_deduction = income - total_tax
#
# elif income >= 1500000:
#     print(f'There will be {tax_percentage_5}% tax')
#     total_tax = income * tax_percentage_1 / 100
#     Income_after_deduction = income - total_tax
#
# else:
#     print('Find a job')

# Final after checking

# below 3 lac - No tax
tax_percentage_1 = 5       # between 3 - 6 lac - 5% tax
tax_percentage_2 = 10      # between 6 - 9 lac - 10% tax
tax_percentage_3 = 15     # between 9 - 12 lac - 15% tax
tax_percentage_4 = 20      # between 12 - 15 lac - 20% tax
tax_percentage_5 = 30     # above 15 lac - 15%-30%


# income = int(input('Enter your income'))

# if 900000 <= income >= 1200000:
# Income_after_deduction = Income - Income = tax_percentage_3 / 100
# print(Income_after_deduction)
# Income_afer_deduction_other_way = income * (1 - tax_percentage_3 / 100)
# print(Income_afer_deduction_other_way)


income = int(input('Enter your income: '))
Income_after_deduction = 0
# for varaible in [1,2,]:
#     print(varaible)

if 0 < income < 300000:
    print('There will be no tax')
    Income_after_deduction = income

elif income <= 600000:
    print(f'There will be {tax_percentage_1}% tax')
    Income_after_deduction = income - income * tax_percentage_1 / 100

elif income <= 900000:
    print(f'There will be {tax_percentage_2}% tax')
    Income_after_deduction = income - income * tax_percentage_2 / 100

elif income <= 1200000:
    print(f'There will be {tax_percentage_3}% tax')
    Income_after_deduction = income - income * tax_percentage_3 / 100

elif income <= 1500000:
    print(f'There will be {tax_percentage_4}% tax')
    Income_after_deduction = income - income * tax_percentage_4 / 100

elif income >= 1500000:
    print(f'There will be {tax_percentage_5}% tax')
    Income_after_deduction = income - income * tax_percentage_5 / 100

else:
    print('Find a job')

print('Income After  Deduction: ', Income_after_deduction)

for variable in [1, 2, 3, 4]:
    print('My tax is deducted')