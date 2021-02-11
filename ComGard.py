'''
Option 2: Community Garden Program 
 ---- Program that Moval residents can register and schedule an ---
 ---- appointment to vist the garden and pick fresh produce. ---
'''

import Resident  #importing module resident
import Prod      #importing module Prod


print('Welcome to the Moreno Valley Community Garden!')     #Greeting message
print('Before getting started some information is required to access the garden.') #Will tell user they need to input some general info

while True:   #while loop incase user inputs a invalid answer somewhere
    try:
        name = input('Please enter your first name:')  #asks for name
        age = input('Age:')   #asks for age
        phone = input('Phone number:')  #asks for phone
        email = input('Email:')  #asks for email
        Resident.check_name(name)   #calling the functions from the Resident module that checks for the following above.
        Resident.check_age(age)
        Resident.check_phone(phone)
        Resident.check_email(email)
        print('\nInformation was stored. Welcome to the Community Garden!')  #If user inputted answers correctly then this will display
        break
    except:
        print('Invalid Info!')  #if not then should display(user will have to restart program)
        break
print('Community garden hours are from: Mon-Fri, 8:00AM-8:00PM, and Sat, 8:00AM-5:00PM')  #WIll display the hours available 

'''Appointment'''  #Appointments

class Appointment():   #class Appointment, which has month,day,year,time in its parameter 
    def __init__(self, month,day,year,time):
        self.month = month
        self.day = day
        self.year = year
        self.time = time
       
    def __str__(self):  #dunder str method  -- 
        return'Your appointment: {}, {}, {}, {}'.format(month,day,year,time)
    
    

class oneappointment(Appointment):  #subclass of appointment
    def __init__(self,month,day,year,time):
        Appointment.__init__(self,month,day,year,time)
        
        
fout = open('apptsum.txt', 'w') #opens a text.file called apptsum - which will display appointment receipt

def show():  #function called show - which holds some prompts for the user
    appointment = []
    print('Now please answer the following and remember to select from the following times listed:') #will ask the user to input a time for appt
    month = input('Enter the month:') #input month(number form usually) or can be abbv e.g: 08 or Aug
    day = input('Enter the day:')  #input day, eg. Mon, Tue, .....
    year = int(input('Year:')) #ask user to input current year
    time = input('Time:')  #Ask the user to input an appropriate time
    a = oneappointment(month,day,year,time)  
    appointment.append(a)     #appends to appoinement 
    print('Appointment has been set')  #will display to the user that appointment has been  created
    
    apptsummary(show,month,day,year,time)  #calls on the next function 
    
def apptsummary(show,month,day,year,time):  #apptsummary on the following chocies that the user picked out for appt.      
    fout.write('-----APPT SUM-----\n')
    fout.write('-----        ------\n')
    fout.write('-----        -------\n')
    
    fout.write('''
*************************
Month: {}
Day: {}
Year: {}
Time: {}
*************************
'''.format(month,day,year,time))
    fout.close() #closes text file
    
show() #calls on the function to display 


dict = {1:('Carrots', 0.00), 2:('Tomatoes', 0.00), 3:('Apples', 0.00), 4:('Potatoes', 0.00), 5:('Avocados', 0.00), 6:('Bell peppers', 0.00), 7:('Lettuce',0.00)} #Dictionary which holds available items and prices

print('\nHere is the current list of vegetables and fruits that you may pick: ') #Will print the dictionary here

for k, v in dict.items():  #for loop that allows the items to be accessed
    print('{}) {}: $ {}'.format(k, v[0], v[1])) #printed and formatted 
    
    
customersum = [] #choices the user makes will be stored here

kchoose = 'Y'  #asks user if they will would to keep choosing 
while kchoose == 'Y': #if yes it will keep appending 
    choice = int(input('\nWhich would you like?:'))
    
    if choice in dict.keys(): #append to the customersum 
        customersum.append((dict[choice][0], dict[choice][1]))      
    else:
        print('Invalid choice') #any invalid number from the dict wil get this 
        
    kchoose = input('To keep selecting please enter (Y for yes, N for no):').upper() #allows for uppercase and even lowercase is user enters y or n 
    
Prod.total(customersum) #total from Prod 


print('\nAs being a customer of community garden, would you like to make any donations to keep garden running for the community?')  #Will ask user if he would like to make any donations
print('Any donations are greatly appreciated!')
usrchoice = int(input('If so, please select what you would like to donate to the garden: 1:Seeds, 2:Soil, 3:Fertilizer, 4:Gardeningtools, 5:VoluntaryLabor, 6:No Donation:')) #asks user to pick from this list

def Seeds():                                   #defintion for each functions in the list
    return "Thank you for the donation!"
def Soil():
    return "Thank you for this donation!"
def Fertilizer():
    return "Thank you for this donation!"
def Gardeningtools():
    return "Thank you for this donation!"
def Volunatarylabor():
    return "Great!, we appreciate it, any help is needed!"
def default():
    return "No worries! Have a good day!"

switcher = {                 
    1: Seeds,
    2: Soil,
    3: Fertilizer,
    4: Gardeningtools,
    5: Volunatarylabor
    } #dictionary - switch 1-5 which will be from the list, 6 will get default 

def switch(donate):     #switch function, will return value from the dictionary 
    return switcher.get(donate, default)()

print(switch(usrchoice))  #prints the user's choice 


print('Thank you for visiting the Community Garden!')  #last text mesasge displayed to the user. 





    


    
