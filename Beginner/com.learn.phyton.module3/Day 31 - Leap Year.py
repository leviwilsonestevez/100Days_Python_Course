year=int(input("Which year to you want to check?\n"))
checking_1 = year % 4
checking_2 = year % 100
checking_3 = year % 400
by_4=(checking_1 == 0)
by_100=(checking_2==0)
by_400=(checking_3==0)
if by_4:
    if by_100:
        if by_400:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is a not leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is a not leap year")
