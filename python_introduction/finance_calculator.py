##Finance calculator
monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

#calculate monthly savings
monthly_savings = float(monthly_income - total_monthly_expenses)


#Calculate future value of savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print('Your monthly savings are $',monthly_savings)
print('Your projected savings after one year, with interest is: $',projected_savings)
