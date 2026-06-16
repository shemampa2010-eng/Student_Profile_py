club_membership = {
    (101, "Alice"),
    (102, "Bob"),
    (103, "Charlie")
}
userid = int(input("Your ID please : "))
for user_id, name in club_membership :
   
    if userid == user_id:
        print ("---Acces Acceptee---")
        break


