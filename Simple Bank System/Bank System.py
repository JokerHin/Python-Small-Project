def Personal():
    list = []
    data = open('Bank Account.txt', 'r')
    list.append(data.read())
    current = int(list[0])
    profile = open('Profile.txt','r')
    print(profile.read())
    print('Balance : $',current)
def deposite():
    list = []
    data = open('Bank Account.txt', 'r')
    list.append(data.read())
    current = int(list[0])
    print('Balance : $',current)
    Add = int(input('How much u wanna deposite ? : '))
    if Add < 0:
        print('Something error, Please try again')
    elif Add > 0:
        Sum = Add + current
        print('Deposite sucessfully !\n Balance : $',Sum)
        renew = open('Bank Account.txt', 'w')
        renew.write(str(Sum))
def withdraw():
    list = []
    data = open('Bank Account.txt', 'r')
    list.append(data.read())
    current = int(list[0])
    print('Balance : $',current)
    Minus = int(input('How much u wanna withdraw ? : '))
    if Minus < 0:
        print('Something error, Please try again')
    elif Minus > 0 and Minus < current:
        Deduct = current - Minus
        print('Withdraw Sucessfully !\nBalance : $', Deduct)
        renew = open('Bank Account.txt', 'w')
        renew.write(str(Deduct))
    elif Minus > current:
        print('[Not enough balance in your account]')

def main():
    while True:
        print('**********************************')
        print('Welcome to my Bank !')
        print('1. Personal Profile')
        print('2. deposite')
        print('3. withdraw')
        print('4. Exit')
        print('***********************************')
        main = input('Please select your choice :')


        if main == '1':
            Personal()
        elif main == '2':
            deposite()
        elif main == '3':
            withdraw()
        elif main == '4':
            print('Thank you for support us !')
            break
        else:
            print('Something error....Please try again !')

if __name__ == '__main__':
    main()