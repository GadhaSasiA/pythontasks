Choice=(input("enter your choice:"))
if Choice in ('+','-','*','/'):
    num1=float(input("enter a number:"))
    num2=float(input("enter a number:")) 

if Choice=='+':
    print(num1+num2)
elif Choice=='-':
    print(num1-num2)
elif Choice=='*':
    print(num1*num2)
elif Choice=='/':
    print(num1/num2)
else:
    print("invalid number")



