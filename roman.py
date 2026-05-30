def romantoint(str):
    str1=str[::-1]
    print(str1)
    num=0
    for i in str1:
        num+=i
        if i=="I":
            ieq=1
        elif i=="V":
            ieq=5   
        elif i=="X":
            ieq=10  
        elif i=="L":
            ieq=50  
        elif i=="C":
            ieq=100
        elif i=="D":
            ieq=500
        elif i=="M":
            ieq=1000
        
        if i>i+1:
            
        elif i==i+1:
            
        else:
            num+=ieq
romantoint("MCMXCIV")
#VICXMCM