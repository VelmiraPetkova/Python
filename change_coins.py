change=float(input())
change_coins=change*100
counter=0

while round(change_coins)>0:
    if change_coins>=200:
        counter=counter+1
        change_coins=change_coins-200
    elif change_coins>=100:
        counter=counter+1
        change_coins=change_coins-100
    elif change_coins>=50:
        counter=counter+1
        change_coins=change_coins-50
    elif change_coins>=20:
        counter=counter+1
        change_coins=change_coins-20
    elif change_coins>=10:
        counter=counter+1
        change_coins=change_coins-10
    elif change_coins>=5:
        counter=counter+1
        change_coins=change_coins-5
    elif change_coins>=2:
        counter=counter+1
        change_coins=change_coins-2
    elif change_coins>=1:
        counter=counter+1
        change_coins=change_coins-1

print(counter)
