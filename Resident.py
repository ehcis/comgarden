'''Resident Basic Info Check(Register Info)'''
'''
Used to check if user inputs any invalid errors,
will make user restart program. 
'''

import re  #needed for re.search()



def check_name(name):        #checks if user inputted a correct name 
    if name.isalpha():       #isalpha() checks if characters in text are letters
        print('You entered:',name) #if true, will display this
    else:
        print('Invalid name') #if not, will display this
             
def check_age(age):          #checks if user inputted a correct age
    if age.isdigit():        #checks if the characters in string are digits  
        print('You entered:',age) #if true, will display this 
    else:
        print('Invalid age') # if characters have letters than this will display
    
def check_phone(phone):     #checks if user inputted a correct phone number
    if phone.isdigit():     #similar to to check_age, will do the same here for phone numbers
        print('You entered:',phone)
    else:
        input('Invalid phone number')
  
   
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'   
def check_email(email):                  #checks for a valid user email
    if (re.search(regex,email)):    #re.search() - will return any use of symbols from regez. eg. '@', '.'   
        print('You entered:',email)
    else:
        print('Invalid email')
