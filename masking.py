def masking(password, n):
    if n * 2 >= len(password):
        print("invalid input")
        return "".join(password)
    
    for i in range(n, len(password) - n):
        password[i] = "*"
    
    return "".join(password)

print(masking(list("hello"), 1))


    
