
#Electricity Bill 
unit =int (input("Nnter the unit : "))
bill = 0

if unit<=100:
    bill = unit*1.5
    
elif unit>100 and unit<=200:
    bill = (100*1.5) + (unit-100)*2.5
elif unit>200 and unit<=300:
    bill = 100*1.5+100*2.5 + (unit-200)*4
elif unit>300 and unit<=350:
    bill =100*1.5+100*2.5 +100*4 +(unit-300)*5
else:
    bill = (100*1.5+100*2.5 +100*4+100*5)+ (unit-350)+2500
  

print("Unit consumed ", unit)
print(f"Total bill : ",bill)