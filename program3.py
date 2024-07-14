guj=int(input("enter your mark of gujarati:"))
account=int(input("enter your mark of account:"))
eng=int(input("enter your mark of english:"))
eco=int(input("enter your mark of eco:"))
spcc=int(input("enter your mark of spcc:"))
total=guj+account+eng+eco+spcc;
print("total mark is",total)
avg=total/5;
print("avereg is:",avg)
if (avg>=80 and avg<=100):
    print("A Gread")
elif (avg>=70 and avg<80):
    print("B Gread")
elif (avg>=60 and avg<70):
    print("C Gread")
elif (avg>=50 and avg<60):
    print("D Gread")
elif (avg>=40 and avg<50):
    print("E Gread")
else:
    print("fail")