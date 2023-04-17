x = 1 

def escopo():
    #global x
    x = 10
    def outra_func():
        print(x, x)
    
    print(x)
    outra_func()
    
escopo()
print(x)