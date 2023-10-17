from beautifultable import BeautifulTable
from colorama import Fore, Back, Style
# Import textwrap to wrap long text for a better visual
import textwrap

# COLOR TAGS

reset_all = Style.RESET_ALL           # Reset to normal
d_color = Fore.LIGHTYELLOW_EX         # Data color
q_color = Style.BRIGHT + Fore.GREEN   # Question color
h_color = Style.BRIGHT + Fore.BLUE    # Header and Image color 

def welcome_message():
    '''
    Display the logo, image and welcome message
    '''
    print(Style.BRIGHT + Fore.BLUE +''' ▄█          ▄████████    ▄████████    ▄████████ ▄██   ▄      ▄████████         
███         ███    ███   ███    ███   ███    ███ ███   ██▄   ███    ███         
███         ███    ███   ███    ███   ███    ███ ███▄▄▄███   ███    █▀          
███         ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███   ███                
███       ▀███████████ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀▀▀   ▄██   ███ ▀███████████         
███         ███    ███ ▀███████████ ▀███████████ ███   ███          ███         
███▌    ▄   ███    ███   ███    ███   ███    ███ ███   ███    ▄█    ███         
█████▄▄██   ███    █▀    ███    ███   ███    ███  ▀█████▀   ▄████████▀          
▀                                                        
 ▄█        ▄██████▄     ▄██████▄  ▀█████████▄   ▄██████▄   ▄██████▄     ▄█   ▄█▄
███       ███    ███   ███    ███   ███    ███ ███    ███ ███    ███   ███ ▄███▀
███       ███    ███   ███    █▀    ███    ███ ███    ███ ███    ███   ███▐██▀  
███       ███    ███  ▄███         ▄███▄▄▄██▀  ███    ███ ███    ███  ▄█████▀   
███       ███    ███ ▀▀███ ████▄  ▀▀███▀▀▀██▄  ███    ███ ███    ███ ▀▀█████▄   
███       ███    ███   ███    ███   ███    ██▄ ███    ███ ███    ███   ███▐██▄  
███▌    ▄ ███    ███   ███    ███   ███    ███ ███    ███ ███    ███   ███ ▀███▄
█████▄▄██  ▀██████▀    ████████▀  ▄█████████▀   ▀██████▀   ▀██████▀    ███   ▀█▀
▀                                                                      ▀        \n''')

    print('''   ____________________________________________________
  |____________________________________________________|
  | __     __   ____   ___ ||  ____    ____     _  __  |
  ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |
  ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |
  ||  |##||  | | || | |JRO|||-|  | |==|+|+||-|-|~||__| |
  ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|
  ||_______________________||__________________________|
  | _____________________  ||      __   __  _  __    _ |
  ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|
  || | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / |
  ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
  |____________________ /\~()/()~//\ __________________|
  | __   __    _  _     \_  (_ .  _/ _    ___     _____|
  ||~~|_|..|__| || |_ _   \ //\\ /  |=|__|~|~|___| | | |
  ||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|
  ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
  |_________________ _/    \/\/\/    \_ _______________|
  | _____   _   __  |/      \../      \|  __   __   ___|
  ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
  ||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||
  ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||
  |_________ __________\___\____/___/___________ ______|
  |__    _  /    ________     ______           /| _ _ _|
  |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|
  | \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|
__|  \/\|/   /(____|/ //                    /  /||~|~|~|__
  |___\_/   /________//   ________         /  / ||_|_|_|
  |___ /   (|________/   |\_______\       /  /| |______|
      /                  \|________)     /  / | |\n''')

    print(reset_all +'Welcome to Larrys LogBook!\n')
    print(textwrap.fill('Hi! Im Larry, your personal budgeting tool! '
                        'I may not be as fancy as those AI thingy majigs you kids use nowadays '
                        'but I get my job done just fine :). Im here to help you with your personal budgeting '
                        'projections, be it for the month, a couple of days for a holiday or '
                        'even the whole year if you up to it. Just give me all the information I need and '
                        'Il do all the magic for you in my trusty logbook, revealing some more insight into your '
                        'budget rather than just how many pennys you have left over ;).', 80))
    print()
    print(textwrap.fill('So the information that my logbook needs to work with are your financial assets, '
                        'incomes, expenses and the timeframe in which you want to budget for. There is additional '
                        'information which is completely optional for you to provide me with but wouldnt it be fun '
                        'to just go all out and discover you financial budgeting story!? '
                        'None the less try out the LogBook and lets see where it takes us.', 80))
    print(Style.BRIGHT + Fore.BLUE +'''\n      __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\ 
   //                 |                 \\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
                    `---`\n''')
print(welcome_message())
print(reset_all + textwrap.fill('Ok... So first I am going to ask a few questions before we go on to '
                    'the actual incomes and expenditures, just some information that might '
                    'be useful to me in regards to your budgeting so hear me out :).', 80))
print()

table4 = BeautifulTable()
table4.columns.header = ["", ""]

name = str(input(q_color + "What is your name?: "))
table4.rows.append([ "NAME", d_color + name])
print(reset_all + f"Hello {name} :).")

month_or_day = (input(q_color + "\nWould you like to budget for a given month(y/n): "))
if month_or_day == "y":
    month = (input("Please give me the number of the month eg: 1 is January and so on: "))
    if month == "1":
        chosen_month = "January"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "2":
        chosen_month = "Febuary"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "3":
        chosen_month = "March"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "4":
        chosen_month = "April"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "5":
        chosen_month = "May"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "6":
        chosen_month = "June"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "7":
        chosen_month = "July"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "8":
        chosen_month = "August"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "9":
        chosen_month = "September"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "10":
        chosen_month = "October"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "11":
        chosen_month = "November"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "12":
        chosen_month = "December"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
if month_or_day == "n":
    days = (input("Then how many days do you want to budget for?: "))
    table4.rows.append(["Days", d_color + days, ])

currency = (input("\nWhat currency would you like to use?($ or (need to find the others): "))
table4.rows.append(["CURRENCY", d_color + currency])

goal_question =  (input("\nDo you want to set a budget goal? ie: a desired amount you want after all expenses(y/n): "))
if goal_question == "y":
    goal = (input("Enter the amount of your goal: "))
    table4.rows.append(["Goal", d_color + goal ])

print(reset_all + "\nSo these are the details you have given to me so far...\n")
print(table4)
(input("\nAre you happy with the details or would you like to start over?(y/n): "))


table3 = BeautifulTable()
table3.columns.header = ["asset", "amount"]
add_asset = []

print(textwrap.fill('Now lets get cracking with the financial assets :). '
                        'By financial assets I mean money that you already have on you that you are willing '
                        'to use in your budget, so if its a pension, a deeply imbedded life savings account '
                        'or anything of that sort, maybe just leave that out ;). What I mean is money in your current '
                        'account, or an amount in it you are willing to give in your budget, same goes with revolut '
                        'or other institutions like that. Cash on hand may be another one you want to put in here '
                        'In the end its all up to you to decide what you want in here, but try leave nothing out '
                        'which may constitute as a financial asset as the more detail you put in only helps you more.', 80))

def asset_calculate():
    '''
   Takes in data of the financial assets plugged in
    '''
    
    asset = (input(q_color + "\nEnter The name of your financial asset: "))
    amount = float(input("Enter the amount of that financial asset: "))
    table3.rows.append([asset, amount])
    add_asset.append(amount)

    print(table3)
    continue1 = (input("Do you want to add another financial asset? y/n: "))
    if continue1 =="y":
        asset_calculate()
        print(table3)
    if continue1 == "n":
        print("Ok... so on to the incomes")  

print(asset_calculate())



table = BeautifulTable()
table.columns.header = ["income", "amount"]
add = []

def income_calculate():
    income = (input("Enter The name of your income: "))
    amount = float(input("Enter your amount of that income: "))
    table.rows.append([income, amount])
    add.append(amount)

    
    print(table)
    continue1 = (input("Do you want to add another income? y/n: "))
    if continue1 =="y":
        income_calculate()
        print(table)
    if continue1 == "n":
        print("ok")  

print(income_calculate())


table2 = BeautifulTable()
table2.columns.header = ["expense", "amount"]
minus = []

def expense_calculate():
    expense = (input("Enter The name of your expense: "))
    amount_exp = float(input("Enter your amount of that expense: "))
    table2.rows.append([expense, amount_exp])
    minus.append(amount_exp)


    print(table2)
    continue1 = (input("Do you want to add another expense? y/n: "))
    if continue1 =="y":
        expense_calculate()
        print(table2)
    if continue1 == "n":
        print("ok") 

print(expense_calculate()) 

inco_total = sum(add)
expe_total = sum(minus)
asset_total = sum(add_asset)

surplus = asset_total + inco_total - expe_total

print(table3)
print()
print(table)
print()
print(table2)
print()
print(" Your financial assets are " + str(asset_total))
print(" Your total income is " + str(inco_total))
print(" Your total expense is " + str(expe_total))
print("your gross amount will be " + str(surplus))






# WARNING!!! EXPEREMENTAL AREA!!!!

#Building an experimental Budgeting tool
#income - expenses = margin

# print("Welcome to the Budget Estimator \n")
# income = float(input("Enter your monthly post-tax income: "))
# additional = float(input("Enter any additional income you expect this month: "))

# total_income = income + additional 
# print("your total income this month will be: " + str(total_income)+ "\n")
# print("Now lets get some expenses...soz \n")

# def gather_expenses():
#     housing = float(input("Enter your monthly housing expense: "))
#     utilities = float(input("Enter your monthly utilities total expense: "))
#     food = float(input("Enter your monthly food expense: "))
#     misc = float(input("Enter any additional expense: "))
#     total_exepenses = housing + utilities + food + misc
#     return total_exepenses

# expense_total = gather_expenses()
# print("your total expenses this month will be: " + str(expense_total)+ "\n")
# margin = total_income - expense_total
# if margin >= 0:
#     print("Your total surplus this coming month will be: " + str(margin) + "\n")
# else:
#     print("You will come up " + str(margin) + " short \n")

# print("thanks for using the monthly budget tool")


# BEAUTIFUL TABLE

# from beautifultable import BeautifulTable
# table = BeautifulTable()
# table.rows.append(["Jacob", "boy"])
# table.rows.append(["Isabella", "girl"])
# table.rows.append(["Ethan", "boy"])
# table.rows.append(["Sophia", "girl"])
# table.rows.append(["Michael", "boy"])
# table.rows.header = ["S1", "S2", "S3", "S4", "S5"]
# table.columns.header = ["name", "gender"]
# print(table)

# print( _   _      _ _        __        __         _     _ _ 
# | | | | ___| | | ___   \ \      / /__  _ __| | __| | |
# | |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
# |  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
# |_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_(_))

# Start of Project (original content as of 15/10/2023)

# from beautifultable import BeautifulTable
# import textwrap

# def welcome_message():
#     print(''' _                          _       _                   
# | |     __ _  _ __   _ __  (_) ___ | |_  ___  _ __  ___ 
# | |    / _` || '_ \ | '_ \ | |/ __|| __|/ _ \| '__|/ __|
# | |___| (_| || | | || | | || |\__ \| |_|  __/| |   \__ \
# |_____|\__,_||_| |_||_|_|_||_||___/ \__|\___||_|   |___/

# | |     ___    __ _ | __ )   ___    ___  | | __         
# | |    / _ \  / _` ||  _ \  / _ \  / _ \ | |/ /         
# | |___| (_) || (_| || |_) || (_) || (_) ||   <          
# |_____|\___/  \__, ||____/  \___/  \___/ |_|\_\ \n''')

#     print('Welcome to the Lannisters LogBook!\n')
#     print(textwrap.fill('Use the Lannisters LogBook to help you budget your monthly '
#                         'finances like a Lannister. Taking in your incomes and expenses, '
#                         'the LogBook will reveal not only your margin but some more insightful '
#                         'information about your budget for the month.', 80))
#     print()
#     print(textwrap.fill('Plug in the number of your financial assets, '
#                         'incomes and expenses for a given month; decalring as many '
#                         'of each income, asset, expense you wish so that the logbook '
#                         'can doo all the calculations for you and giving you insight  '
#                         'into your projected monthly financial story.', 80))
#     print()
# print(welcome_message())

# name = (input("Please Enter your name: "))
# month = (input("Please Enter the month: "))

# print('you name is ' + str(name) + ' and the month is ' + str(month))

# table3 = BeautifulTable()

# # table.rows.append(["Isabella", "girl"])
# # table.rows.append(["Ethan", "boy"])
# # table.rows.append(["Sophia", "girl"])
# # table.rows.append(["Michael", "boy"])
# # table.rows.header = ["S1", "S2", "S3", "S4", "S5"]
# table3.columns.header = ["asset", "amount"]
# add_asset = []

# def asset_calculate():
#     asset = (input("Enter The name of your financial asset: "))
#     amount = float(input("Enter your amount of that financial asset: "))
#     table3.rows.append([asset, amount])
#     add_asset.append(amount)

    
#     print(table3)
#     continue1 = (input("Do you want to add another financial asset? y/n: "))
#     if continue1 =="y":
#         asset_calculate()
#         # income = (input("Enter The name of your income: "))
#         # amount = float(input("Enter your amount of that income: "))
#         # table.rows.append([income, amount])
#         print(table3)
#     if continue1 == "n":
#         print("ok")  

# print(asset_calculate())



# table = BeautifulTable()

# # table.rows.append(["Isabella", "girl"])
# # table.rows.append(["Ethan", "boy"])
# # table.rows.append(["Sophia", "girl"])
# # table.rows.append(["Michael", "boy"])
# # table.rows.header = ["S1", "S2", "S3", "S4", "S5"]
# table.columns.header = ["income", "amount"]
# add = []

# def income_calculate():
#     income = (input("Enter The name of your income: "))
#     amount = float(input("Enter your amount of that income: "))
#     table.rows.append([income, amount])
#     add.append(amount)

    
#     print(table)
#     continue1 = (input("Do you want to add another income? y/n: "))
#     if continue1 =="y":
#         income_calculate()
#         # income = (input("Enter The name of your income: "))
#         # amount = float(input("Enter your amount of that income: "))
#         # table.rows.append([income, amount])
#         print(table)
#     if continue1 == "n":
#         print("ok")  

# print(income_calculate())


# table2 = BeautifulTable()

# # table.rows.append(["Isabella", "girl"])
# # table.rows.append(["Ethan", "boy"])
# # table.rows.append(["Sophia", "girl"])
# # table.rows.append(["Michael", "boy"])
# # table.rows.header = ["S1", "S2", "S3", "S4", "S5"]
# table2.columns.header = ["expense", "amount"]
# minus = []

# def expense_calculate():
#     expense = (input("Enter The name of your expense: "))
#     amount_exp = float(input("Enter your amount of that expense: "))
#     table2.rows.append([expense, amount_exp])
#     minus.append(amount_exp)


#     print(table2)
#     continue1 = (input("Do you want to add another expense? y/n: "))
#     if continue1 =="y":
#         expense_calculate()
#         # income = (input("Enter The name of your income: "))
#         # amount = float(input("Enter your amount of that income: "))
#         # table.rows.append([income, amount])
#         print(table2)
#     if continue1 == "n":
#         print("ok") 

# print(expense_calculate()) 

# inco_total = sum(add)
# expe_total = sum(minus)
# asset_total = sum(add_asset)

# surplus = asset_total + inco_total - expe_total

# print(table3)
# print()
# print(table)
# print()
# print(table2)
# print()
# print(" Your financial assets are " + str(asset_total))
# print(" Your total income is " + str(inco_total))
# print(" Your total expense is " + str(expe_total))
# print("your gross amount will be " + str(surplus))