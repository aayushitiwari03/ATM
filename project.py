print("Welcome to SBI")
balance=500000
print("insert your card")
card=int(input("select your card 1.debit card 2.credit card:"))
if card=="credit card" or "debit card" :
    print("next")
    language=int(input("select your language 1.english 2.hindi:"))
    if language==1:
        account=int(input("select your account 1.current account 2.saving account:"))
        if account=="1" or "2":
            tranction=int(input("choose your tranction 1.balance enquiry 2.money withdrawl:"))
            if tranction=="1" or "2":
                pin=int(input("enter your pin"))
                if pin==pin:
                    print("your total amount is :",balance)
                    if tranction=="2":
                        print("money withdrawl")
                    else:
                         print("no money")
                else:
                    print("Wrong")
            else:
                 print("please chose valid transtion")
        else: 
            print("invalid account")
    else:
        ("choose another language")
else:
    print("plz check carefully")