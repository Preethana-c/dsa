'''def string_repeat(s):
    count={}
    for i in s:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for key,value in count.items():
        if value<2:
            return key
            break
        
print(string_repeat("importance of ibm coding interviews in recruitmentpafbgvwsud"))'''

def string_repeat(s):
    count={}
    for i in s.split():
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for key,value in count.items():
        if value<2:
            return key
            break
print(string_repeat("when i saw a cat the cat saw a rat the rat ran away when i"))    

