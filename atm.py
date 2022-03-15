datafilename = 'data_atm.csv'

def get_bank_from_file(filename = datafilename):
    """ Return a 'bank' data structure as described 
        at the top of the file, by reading its data from a CSV file """
    bank = []                        # Start with an empty bank.
    datafile = open(filename, 'r')
    first_line = datafile.readline()  # Read & do nothing with first line.
    while True:                      # Loop over remaing lines in file.
        line = datafile.readline()
        if line == '':               # At end of file, readline() returns ''
            return bank              # ... so the bank is filled with accounts.
        else:
            (person, pin, main_account, dollar_account) = line.split(',')
            bank.append( {'person': person,               # Make a new dict
                          'pin': int(pin),           # account, and put
                          'main_account': float(main_account),    # it in the bank.
                          'dollar_account': float(dollar_account) }     # 
                       )

def login(bank):
    """ Prompt the user to login to a bank account. 
        If succesful, return id = index of account in bank list.
        If user types 'QUIT', return 'QUIT'.
    """
    while True:                          # Allow repeated login attempts.
        # print "DEBUG: {}:format(bank)"

        print
        who = input('Please enter your name (or QUIT to exit): ')
        print('')

        if who == 'QUIT':
            print ('Bye.')
            return 'QUIT'

        pin = int(input('Enter your pin? '))
        print('') 

        for id in range(len(bank)):   # search accounts for user,passwd
            account = bank[id]
            if account['person'] == who and account['pin'] == pin:
               return id

        print(" OOPS: name or pin is wrong - try again. ")

def transaction(account):
    """ Prompt user for transactions to apply to given account, which is
        a dictionary with keys ('person', 'pin', 'main_account', 'dollar_account')
        Return the modified account. """
    while True:
        
        # show account status
        print("Account Status: Hello {} , you have Ksh. {:.2f} in main account, {:.2f} dollars in your dollar account.".format(
            account['person'], account['main_account'], account['dollar_account']))
        
        # do one transaction
      
        what = input('\n****Menu****\n 1. Deposit\n 2. Withdraw\n 3. Transfer\n 4. Exit\n************\n :')


        if what[0] == '4':    # end
            return account
        elif what[0] == '2':  # withdraw
            enter_account = input('Choose account (1. Main account, 2. Dollar account) ? ')
            if enter_account == '1':
                which = 'main_account'
            elif enter_account == '2':
                which = 'dollar_account'
            else:
                 print("Enter a valid account.") 
                 break
            
            amount = float(input('  amount (xxx.xx) ? '))
            if amount > account[which]:
                print("Not enough money in account")
            else:
                account[which] = account[which] - amount
                reciept = input('Do you want a reciept(y or n): ')
                print('')
                if reciept == "y":
                    print("********************************")
                    print("    TRANSACTION SUCCESSFULL     ")
                    print(" Account holder: {}".format(account['person']))
                    print(" Main Account: {}".format(account['main_account']))
                    print(" Dollar account balance: {:.2f}".format(account['dollar_account']))
                    print("********************************")
                    print('')
                else:
                    print("Thank you for banking with us!!")
                    print('')
        elif what[0] == '1':  # deposit
            enter_account = input('Choose account (1. Main account, 2. Dollar account) ? ')
            if enter_account == '1':
                which = 'main_account'
            elif enter_account == '2':
                which = 'dollar_account'
            else:
                 print("Enter a valid account.") 
                 break
            amount = float(input('  amount (xxx.xx) ? '))
            account[which] = account[which] + amount

        elif what[0] == '3':  # transfer
            which = input(' 1 (main account to dollar account) or 2 (dollar account to main account) ? ')
            amount = float(input('  amount (xxx.xx) ? '))
            if which == '1':
                account['main_account'] = account['main_account'] - amount
                account['dollar_account'] = account['dollar_account'] + (amount/114)
                
            if which == '2':
                account['main_account'] = account['main_account'] + (amount*114)
                account['dollar_account'] = account['dollar_account'] - amount

def main():
    print("-- ATM BY TEAM JULIET --")
    bank = get_bank_from_file()
    while True:
        id = login(bank)
        if id == 'QUIT':
            return
        else:
            bank[id] = transaction( bank[id] )

if __name__ == '__main__':
    main()