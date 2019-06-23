import mysql.connector
try:

   conn=mysql.connector.connect(host="localhost",user="root",passwd="sachin",database="banking")
   cur=conn.cursor()
   sql_select="SELECT * from account_data"

   def createAccount():
     # Generating a account ID automatically via auto_gen()
      account_no=str(auto_gen())
      name=str(input("Enter your name : "))
      email=str(input("Enter your email : "))
      pin=str(input("Choose a 4 digit pincode : "))
      phone=str(input("Enter your phone number : "))
      gender=str(input(" M for Male \n F for Female\n O for others: "))
      address=str(input("Enter your address : "))
      country = str(input("Enter your country : "))
      state = str(input("Enter your state : "))
      city = str(input("Enter your city : "))
      amount=str(input("Enter amount : "))

      sql = "INSERT into account_data values ('"+account_no+"','"+pin+"','"+name+"','"+email+"','"+phone+"','"+gender+"','"+address+"','"+country+"','"+state+"','"+city+"','"+amount+"')"
      cur.execute(sql)
      conn.commit()
      print(" Account has been created ")

   def auto_gen():
     var='SBI'
     cur.execute(sql_select)
     x=101
     n=len(list(cur))
     if n >0:
       x=x+n
     else:
       pass
     return var+str(x)

   def withdraw():
     ac=str(input("Enter Your account number : "))
     pincode=str(input("\nEnter your pin : "))
     sql="SELECT ac_no from account_data WHERE ac_no='"+ac+"' and pin ='"+pincode+"'"
     cur.execute(sql)
     rs=cur.fetchone()

     if rs[0] == ac:
       withdraw_amount=int(input("Enter amount to be withdrawn : "))
       sql2="SELECT current_amt from account_data WHERE ac_no ='"+ac+"'"
       cur.execute(sql2)
       amount=cur.fetchone()

       if amount[0] > withdraw_amount:
         var=str(amount[0]-withdraw_amount)
         sql3="UPDATE account_data SET current_amt='"+var+"' WHERE ac_no='"+ac+"'"
         cur.execute(sql3)
         conn.commit()
         print(" Please collect your money : ")

       else:
         print("\nInsufficient Balance! ")
       
     else:
       print("Wrong account number or password.\n Please enter the correct account number and password.")


   def deposit():
     ac  = str(input("Enter Your account number : "))
     sql = "SELECT ac_no from account_data WHERE ac_no='"+ac+"'"
     cur.execute(sql)
     rs = cur.fetchone()

     if rs[0] == ac:
       deposit=int(input("\nEnter the amount you want to deposit : "))
       sql2="SELECT current_amt from account_data WHERE ac_no='"+ac+"'"
       cur.execute(sql2)
       amount=cur.fetchone()
       var=str(amount[0]+deposit)
       sql3="UPDATE account_data SET current_amt='"+var+"' WHERE ac_no='"+ac+"'"
       cur.execute(sql3)
       conn.commit()
       print("Your amount is deposited! ")
       
     else:
        print("Wrong account number. \nPlease enter the correct account number you want to deposit into.")


   def tranFund():
     ac=str(input("Enter Your account number : "))
     pincode=str(input("\nEnter your pin : "))
     sql="SELECT ac_no from account_data WHERE ac_no='"+ac+"' and pin ='"+pincode+"'"
     cur.execute(sql)
     rs=cur.fetchone()

     if rs[0] == ac:
       receiver=str(input("Enter the account number of recipent : "))
       sql2="SELECT ac_no from account_data WHERE ac_no='"+receiver+"'"
       cur.execute(sql2)
       rs2=cur.fetchone()

       if rs2[0]==receiver:
         amount=int(input("Enter the amount you want to transfer : "))
         sql3="SELECT current_amt from account_data WHERE ac_no in ('"+ac+"','"+receiver+"')"
         cur.execute(sql3)
         current=cur.fetchall()

         if current[0][0] > amount:
           var1=str(current[0][0] - amount)
           var2=str(current[1][0] + amount)
           sql4="UPDATE account_data SET current_amt='"+var1+"' WHERE ac_no='"+ac+"'"
           cur.execute(sql4)
           sql5="UPDATE account_data SET current_amt='"+var2+"' WHERE ac_no='"+receiver+"'"
           cur.execute(sql5)
           conn.commit()
           print("\nFunds has been transfered.\n")
         else:
           print("Insufficient Funds \n Transfer Failed!\n ")
       else:
         print("Wrong account number recipent \n Please enter correctly. \n")
     else:
       print("Wrong account number or password.\n Please enter the correct account number and password.\n")

   def changePin():
     ac=str(input("Enter Your account number : "))
     pincode=str(input("\nEnter your pin : "))
     sql="SELECT pin from account_data WHERE ac_no='"+ac+"'"
     cur.execute(sql)
     rs=cur.fetchone()
     if rs[0] == pincode:
       new=str(input("Enter new Pincode : "))
       new_rep=str(input("Enter again : "))
       if new==new_rep:
         sql2="UPDATE account_data SET pin='"+new+"' WHERE ac_no='"+ac+"'"
         cur.execute(sql2)
         conn.commit()
         print("Password Successfully Changed. \n")
       else:
         print("Password don't Matches! \n")
     else:
       print("Wrong pincode entered! \n Try again with correct Pin.\n")

   def balance():
     ac=str(input("\nEnter Your account number : "))
     pincode=str(input("\nEnter your pin : "))
     sql="SELECT current_amt from account_data WHERE ac_no='"+ac+"' and pin='"+pincode+"'"
     cur.execute(sql)
     rs=cur.fetchone()
     print("Your current balance is : Rs.",rs[0])
     print()

   a=True
   while a :
     print(" Press 1 to Create Account : ")
     print(" Press 2 to Withdraw : ")
     print(" Press 3 to Deposit : ")
     print(" Press 4 to Transfer Money : ")
     print(" Press 5 to Change Pin : ")
     print(" Press 6 to Balance Enquiry : ")
     print(" Press 7 to Exit : ")
     
     choice=int(input(" Enter Choice: "))

     if choice == 1 :
       createAccount()
     if choice == 2 :
       withdraw()
     if choice == 3 :
       deposit()
     if choice == 4 :
       tranFund()
     if choice == 5:
       changePin()
     if choice == 6:
       balance()
     if choice == 7:
       print("Thanks for using our service. ")
       conn.close()
       a=False
except Exception as err:
   print("Something went wrong : ",str(err),"\nRestarting application.")
