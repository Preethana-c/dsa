def email_valid(email):
    print("email:", email)
    if len(email)>254:
        print("invalid email")
        return False
    if "@" not in email or "." not in email:
        print("invalid email")
        return False
    local, domain = email.split("@", 1)
    if len(local)>64:
        print("invalid email")
        return False
    for i in email:
        if i==" ":
            print("invalid email")
            return False
    
    for i in email:
        if i.isupper():
            print("invalid email")
            return False
    if email.count("@")>1:
        print("invalid email")
        return False
    if local[0]=="." or local[-1]==".":
        print("invalid email")
        return False
    if domain[0]=="-" or domain[-1]=="-":
        print("invalid email")
        return False
    if domain[0]=="." or domain[-1]==".":
        print("invalid email")
        return False
    
    for i in range(len(local)-1):
        if local[i]=="." and local[i+1]==".":
            print("invalid email")
            return False
    for i in range(len(domain)-1):
        if domain[i]=="." and  domain[i+1]==".":
            print("invalid email")
            return False   
    for i in domain:
        if i.isalpha() or i.isdigit() or i=="-" or i==".":
            continue
        else:
            print("invalid email")
            return False
    if  "." not in domain:
        print("invalid email")
        return False
    mail, ext = domain.split(".", 1)
    if len(mail)<1:
        print("invalid email")
        return False
    if len(ext)<2:
        print("invalid email")
        return False

    print("valid email")
    return True
    
email_valid("pree.c@gmail.com")
email_valid("pree.c@gmail")# no dot in domain
email_valid("pree.c@.com")# dot at start of domain
email_valid("pree.c@com.")# dot at end of domain
email_valid("pree..@gmail.com")# consecutive dots in local
email_valid("pree.c@gmail..com")# consecutive dots in domain
email_valid("pree.c@gmail.c")# less than 2 char in extension
email_valid(".pree.c@gmail.com")# dot at start of local
email_valid("pree.c.@gmail.com")# dot at end of local
email_valid("pree.c@-gmail.com")# hyphen at start of domain
email_valid("pree.c@gmail-.com")# hyphen at end of domain
email_valid("pree .xxx@gmail.com")# space in local
email_valid("pree.c@xxx .com")# space in domain
email_valid("123test@gmail.com")# valid email with digits
email_valid("test@ ,com")

    