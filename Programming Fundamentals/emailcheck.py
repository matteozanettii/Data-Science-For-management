valid = False
while not valid:
  
 email=input("Insert email: ")
 repeat=input("Reinsert the email: ")
 boo1=(email.count("@")) == 1
 boo2=email.endswith(".it") or email.endswith(".com")
 boo3= (email == repeat)
 final=boo1 and boo2 and boo3
 
 if final:
     valid=True
     print("OK!")
     
 else:
     print("Wrong email or email repeated, try again!")
