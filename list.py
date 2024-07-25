#find the middle element 
numbers=[1,2,3,4,5]
n=len(numbers)
if n%2==0:
    m1=numbers[n//2-1]
    m2=numbers[n//2]
    middle=(m1+m2)/2
    print("the middle element is:",middle)
else:
    m_index=n//2
    middle=numbers[m_index]
    print("")

#2 Print calander
    import calendar
    yy=2024
    mm=7
print(calendar.month(yy,mm))
    
# #Find leap year
year=int(input("enter a year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is aleap year')
else:
        print(f'{year} is not a leap year')

