# Sabin Bhandari
initialdisplay='''WELCOME TO SUNWAY CHARACTER CHECK SYSTEM
 \tMAITIDEVI,KATHMANDU'''
print(initialdisplay) 
print("\t")

String = input("Enter the String: ")
print("\t")

lowercase= 0
uppercase=0
digit=0
special_ch=0

for character in String:
    if character.islower():
         lowercase=lowercase+1
         
    elif character.isupper():
        uppercase=uppercase+1
        
    elif character.isdigit():
        digit=digit+1
        
    else:
        special_ch=special_ch+1
        
print("Lower case: ",lowercase)
print("Upper Case: ",uppercase)
print("Digit: ",digit)
print("Special Character: ",special_ch)

print("\t")

initialdisplay='''Thank You for the visit!'''
print(initialdisplay) 