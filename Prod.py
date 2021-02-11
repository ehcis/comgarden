'''Produce Subtotal'''

fout = open('summary.txt', 'w') #opens a text file, 'summary' which will write the receipt

tax = 0.0000   #tax will be 0, since garden items are free
def total(customersum):  #function that will get the total from subtotal and tax

    subtotal = 0  #will be 0 like tax, since free

    for i in customersum:  #runnning sum for list, again should = 0
        subtotal += (i[1])

    print(customersum)   #will print subtotal = 0
    print('Subtotal: ${:.2f}'.format(subtotal)) 

    tamount = tax*subtotal   #will print tax amount = 0
    print('Tax: \t $ {:.2f}'.format(tamount))

    total = subtotal + tamount
    print('Total: \t ${:.2f}'.format(total)) # total = sub + tax = 0

    summary(customersum, subtotal, total)  #calling on the functon summary
      
def summary(customersum, subtotal, total):  #summary on the following parameters
    fout.write('----ORDER SUMMARY----\n')
    fout.write('Item             Price\n')
    fout.write('----             ======\n')
    
    for i in customersum:    #for loop for the customer's choices
        fout.write('{} $ {}\n'.format(i[0],i[1]))
        
    fout.write('''     
***********************
Subtotal: $ {}
Tax:      $ {:.2f}
Total:    $ {:.2f}
***********************
'''.format(subtotal,tax*100,total))  #Will write user's receipt to the text file
   
    fout.close()  #closes the text file 
    print('Thank you for ordering from the community garden! Your receipt is being printed') #confirms the transaction was successful. 
           
               
            
    
            
    
        
    
            


    
    
    
