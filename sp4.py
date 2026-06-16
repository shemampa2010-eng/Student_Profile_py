setset = set()
while True :
    op = input ("Do you want to add 5 student names ? ")
    if op == "Yes":
        for i in range (1 , 6):
            sun= input("Eleve: ")
            setset.add (sun)
        print(setset)
    else :
        break
    
