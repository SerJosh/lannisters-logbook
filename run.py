#Building an experimental Budgeting tool
#income - expenses = margin


print("Welcome to the Budget Estimator \n")
income = float(input("Enter your monthly post-tax income: "))
additional = float(input("Enter any additional income you expect this month: "))

total_income = income + additional 
print("your total income this month will be: " + str(total_income)+ "\n")
print("Now lets get some expenses...soz \n")

def gather_expenses():
    housing = float(input("Enter your monthly housing expense: "))
    utilities = float(input("Enter your monthly utilities total expense: "))
    food = float(input("Enter your monthly food expense: "))
    misc = float(input("Enter any additional expense: "))
    total_exepenses = housing + utilities + food + misc
    return total_exepenses

expense_total = gather_expenses()
print("your total expenses this month will be: " + str(expense_total)+ "\n")
margin = total_income - expense_total
if margin >= 0:
    print("Your total surplus this coming month will be: " + str(margin) + "\n")
else:
    print("You will come up " + str(margin) + " short \n")

print("thanks for using the monthly budget tool")

