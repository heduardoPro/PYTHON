# VAriavel livre + nonlocal
def fora():

    a = 1
    
    def dentro():
        print(locals())
        return a
    return dentro

