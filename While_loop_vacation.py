money_needed= float(input())
money_available=float(input())

counter=0
spending_counter=0
save_money=money_available

while money_needed>money_available and spending_counter<5 :

    use_money = input()
    amount = float(input())

    if use_money=='save':
        money_available=money_available+amount
        counter=counter+1+spending_counter
        spending_counter=0
        if money_available>=money_needed:
            print(f'You saved the money for {counter} days.')
            ##print(spending_counter)
            break
    elif use_money=='spend':
        money_available=money_available-amount
        spending_counter = spending_counter + 1
        if money_available<0:
            money_available=0
        ##spending_counter=spending_counter+1
        if spending_counter==5:
            print(f'''You can't save the money.''')
            print(spending_counter)
            break










