def valid(password):
    if len(password)<8:
        print("invalid pwd")
        return False
    for i in password:
        if i==" ":
            print("invalid pwd")    
            return False
    special_characters = "@#$%&*"
    uflag=False
    lflag=False 
    digflag=False
    scflag=False

    for i in password:
        if i.isupper():
            uflag=True

    for i in password:        
        if i.islower():
            lflag=True
        
    for i in password:        
        if i.isdigit():
            digflag=True
        
    for i in password:
        if i in special_characters:
            scflag=True
        
    if uflag==True and lflag==True and digflag==True and scflag==True:
        print("valid pwd")
        return True
    else:
        print("invalid pwd")
        return False
               
valid("bdugnj7Asdn&*")
valid("bdugnj7sdn&*")#no cap letter
valid("bdugAnj7 sdn&*")#space in pwd
valid("bdugAnj7sdn")#no special char    
valid("ASDFNGHKKJEJRN7&*")#  no small letter
valid("bdugAnj7sdnSD")# no special char
valid("bduAgnjsdn&*")# no digit
valid("bd7sdn&*")# less than 8 char
valid("bdugAGBN7sdn&*")
valid("bdugAGBN798989sdn&*")


        
        
        
