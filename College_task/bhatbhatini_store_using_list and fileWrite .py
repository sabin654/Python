
#creating empty list to store values
name=[]
address=[]
email=[]
itemname=[]
itemprice=[]
itemqty=[]
total=[]
netTotal=[]
disc=[]

def initialDisplay():
    print('''     SUNWAY BHATBHATINI STORE 
   \t KATHMANDU, NEPAL\n
   \t\t\t\t Date: 2022-12-22
    ''')
    
    
   
# #fuction for input and information
def initialInformation():
    n=int(input("Enter the number of customers: "))
    #first for loop for different customers
    for i in range(n):
        #input for details
        name.append(input(f"Enter the name of customer [{i+1}]: "))
        address.append(input(f"Enter the address of customer [{i+1}]: "))
        email.append(input(f"Enter the email of customer [{i+1}]: "))
        itemno=int(input(f"Enter the number of items of customer : "))
        
        for j in range(itemno):
            totalPrice=0
            itemname.append(input(f"enter the name of item[{j+1}]: "))
            itemprice=int(input(f"Enter the price of item [{j+1}]: "))
            itemqty=int(input(f"Enter the quantity of item [{j+1}]: "))
            totalPrice=totalPrice+itemprice*itemqty
            
            total.append(totalPrice)
            calculation(total)  
      
       
        
    Action=int(input("Enter 1 to print the bill: \nEnter 2 to Create the bill in text file: \nEnter 3 to both print and create bill : "))
    if Action==1:
        displayInformation(name,address,email,itemname,total,disc,netTotal)
    elif Action==2:
        writeInformation(name,address,email,itemname,total,disc,netTotal)
    elif Action==3:
        displayInformation(name,address,email,itemname,total,disc,netTotal)
        writeInformation(name,address,email,itemname,total,disc,netTotal)
    else:
        print("Invalid Input") 
        
                                                                                                                                                                                                                                                                                                                                                                                                    
def calculation(total):
    for i in range(len(total)):
        totalPrice=total[i]
        discount=0
        if totalPrice<=5000:
            discount = totalPrice*0.05
        elif totalPrice<=7000:
            discount=(5000*0.05)+(totalPrice-5000)*0.08
        elif totalPrice<=10000:
            discount=(5000*0.05)+(2000*0.08)+(totalPrice-7000)*0.10
        else:
            discount=(5000*0.05)+(2000*0.08)+(3000*0.10)+(totalPrice-10000)*0.15
        # net amount after discount
        
        netAmount=totalPrice-discount
        netTotal.append(netAmount)
        disc.append(discount)
        return netAmount,discount
    
#function for writing the information in text file
def writeInformation(name,address,email,itemname,total,disc,netTotal):
    for j in range(len(name)):
        f= open("C:\python\sabin.txt","w", encoding="utf-8")
        for i in range(1):
            f.write(f"Customer Name: {name[j]}\n")
            f.write(f"Customer Address: {address[j]}\n")
            f.write(f"Customer Email: {email[j]}\n")
            f.write(f"Item Name: {itemname[j]}\n")
            f.write(f"Total Price: {total[j]}\n")
            f.write(f"Discount: {disc[j]}\n")
            f.write(f"Net Amount: {netTotal[j]}\n")
        f.close()

# #function for displaying the information
def displayInformation(name,address,email,itemname,total,disc,netTotal):
 for i in range(len(name)):
    print(f"Customer Name: {name[i]}")
    print(f"Customer Address: {address[i]}")
    print(f"Customer Email: {email[i]}")
    print(f"Item Name : {itemname[i]}")
    print(f"Total Price: {total[i]}")
    print(f"Discount: {disc[i]}")
    print(f"Net Amount: {netTotal[i]}")

# #function call
initialDisplay()
initialInformation()

