contact={}
def display_contact():
  print("Name\t\t\contact number")
  for key in contact:
    print("{}\t\t{}".format(key,contact.get(key)))
while True:
  choice=int(input("1.add contact\n 2.search contact\n 3.display contact\n 4.update contact\n 5.delete contact\n 6.exit\n"))
  if choice==1:
    name=input("enter the name:")
    phone=input("enter mobile number:")
    email=input("enter the email:")
    address=input("enter the address:")
    contact[name]=phone
  elif choice==2:
    search_name=input("enter the CONTACT NAME:")
    if search_name in contact:
      print(search_name,"contact is",contact[search_name])
    else:
      print("contact not found")
  elif choice==3:
    if not contact:
      print("empty contact book")
    else:
      display_contact()
  elif choice==4:
    update_contact=input("enter the conatct name:")
    if update_contact in contact:
      phone=input("enter mobile number:")
      contact[update_contact]=phone
      print("contact updated")
      display_contact()
    else:
      print("contact not found in contact book")
  elif choice==5:
    del_contact=input("enter the contact name to be deleted:")
    if del_contact in contact:
      confirm=input("are you sure you want to delete the contact:")
      if confirm=="yes":
        contact.pop(del_contact)
      display_contact()  
    else:
      print("contact not found")
  else:
    break