print('hello world')

# # FUNCTIONS 

def bootcamp_welcome(bootcamp_subject):
    print(f'Welcome to the {bootcamp_subject} Bootcamp!')

bootcamp_welcome('Data Analytics')
bootcamp_welcome('Cyber Security')

def cash_machine(acc_num, sort_code, amount):
    print(f'Withdrawing £{amount} \nAccount Number: {acc_num}\nSort Code: {sort_code}')

cash_machine(amount= 500, acc_num= 507044, sort_code=403003)


def birthday_message(name, age):
    print(f'Happy Birthday {name} I hear you are {age} today!')

def drinks_order(size, type):
    print(f'Your ordered a {type} in a size {size}')

birthday_message('Samuel', 26)
drinks_order(size='L', type='Pina Colada')

order_count = 0
def take_order(topping):
    global order_count
    print(f'Pizza with {topping}')
    order_count +=1

take_order('pepperoni')
print(order_count)
take_order('cheese')
print(order_count)

acc_balance = float(4000)
correct_pin = int(1234)
def check_pin(pin):
    global correct_pin
    int(input('Please enter your pin:'))
    if pin != correct_pin:
        print('incorrect pin')
        return False
    else: 
        print('correct pin')
        return True

def withdraw_cash(amount):
    global acc_balance
    float(input('How Much Would You Like To Withdraw?:'))
    if amount > acc_balance:
        acc_balance -= amount
        print(f'Your new balance is £{amount}')
    else: 
        print('insufficient funds')
        


    