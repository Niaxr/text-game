choice = 0
FALSE = 0
level = 0

Deal=input("Welcome to Game Hub")

#-------------START OF WHILE LOOP-------------
while choice == FALSE:

    game=int(input("What level of difficulty would u like to play at? 1, 2 or 3?"))
    
    if game == 3:
        #level=int(input("This is the hardest level are you sure?"))
        choice = input("This is the hardest level... are you sure? (TRUE / FALSE)")
      
    elif game == 2:
        #print("Medium? Good choice")
        choice = input("This is the normal difficulty... are you sure? (TRUE / FALSE)")
    
    elif game == 1:
        #level=int(input("The easiest level? Are you sure?"))
        choice = input("This is the easiest level... are you sure? (TRUE / FALSE)")
     
    else:
        print("Sorry thats not possible try again")
        
    if choice == "true":
        
        print("Lets get started!")
    
        break
       
    else:

      print("Guess u couldnt handle the heat huh :P")  
                
#-------------END OF WHILE LOOP-------------
