def cf(C1):
    C2=(C1 * 9/5) + 32
    history.append(("C: "+str(C1)," F: "+str(C2)))
    return C2
def fc(F1):
    F2=(F1 - 32) * (5/9)
    history.append(("F: "+str(F1)," C: "+str(F2)))
    return F2

history=[]
while(1):
    choice=int(input('Enter\n1 for C to F\n2 for F to C\n3 to review the previous inputs and outputs\n4 to exit'))
    if choice==1:
        C=float(input('Enter temperature in celsius'))
        print("Temperature in fahrenheit is :",cf(C))
    elif choice==2:
        F=float(input('Enter temperature in fahrenheit'))
        print("Temperature in celsius is :",fc(F))
    elif choice==3:
        print("History is ",history)
    elif choice==4:
        break
    else:
        print("Invalid Input")
