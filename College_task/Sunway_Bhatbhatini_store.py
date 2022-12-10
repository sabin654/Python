def initialDisplay():
    print('''     SUNWAY BHATBHATINI STORE 
   \t KATHMANDU, NEPAL\n
   \t\t\t\t Date: 2022-12-22
    ''')

def cust_info():
    Num = int(input("Enter Number Of Customer : " ))
    print("\t")
    
    for i in range(Num):
        Name = input(f"Enter Customer Name [{i+1}]: ")
        Address= input(f"Address [{i+1}] : ")
        Email= input(f"Email [{i+1}] : ")
        Phone= int(input(f"Contact No [{i+1}] : "))
        Itemno= int(input(f"Items [{i+1}] : "))
    

        for j in range(Itemno):
             total_price=0
             item_name=input(f"Item Name [{j+1}]: ")
             item_price=int(input(f"Item Price [{j+1}]: $")) 
             item_qty=int(input(f"Quantity of Items [{j+1}]: "))
             total_price= total_price+item_price*item_qty
             print("_________________________________________")

        
       
        netAmt,discount=calculation(total_price)
        initialDisplay() 
        
        display(Name,Address,Email,Phone,item_name,total_price,discount,netAmt)
        

    
    
def calculation (total_price):
    discount =0
    if total_price <=5000:
        discount= total_price*0.05
    elif total_price>5000 and total_price<=7000:
        discount= (5000*0.05) + (total_price-5000)*0.08
    elif total_price>7000 and total_price<=10000:
        discount=(5000*0.05)+ (2000*0.08) + (total_price-7000)*0.10
    else:
        discount= (5000*0.05)+ (2000*0.08) + (3000*0.10)+(total_price-10000)*0.15
    netAmt= total_price- discount
    return netAmt,discount

def display(Name, Address,Email,Phone,item_name,total_price,discount,netAmt):
    print(f"Customer Name: {Name}")
    print(f"Customer Address: {Address}")
    print(f"Customer Email: {Email}")
    print(f"Contact No: {Phone}")
    print(f"Item: {item_name}")
    print(".............................................")
    print(f"Total Price: ${total_price}")
    print(f"Discount: ${discount}")
    print(f"Net Amount: ${netAmt}")
    print(".............................................")


initialDisplay() 
cust_info()

 



    
    
    
    

