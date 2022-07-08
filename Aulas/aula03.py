# DECLARAÇAO DE VALOR DA VARIAVEL
x=1 #int 
x="variavel" #string
x=2.5 #float
x=False #bool

n1=5;n2=2;x=complex(n1,n2)
#print(x.real)
#print(x.imag)
x=["LOL", "GTA", "POW", "MARIO KART", 1, 15.58, True] #LIST / ARRAY
#print("valor: "+x[0])
x=("LOL", "GTA", "POW", "MARIO KART", 1, 15.58, True) #Tupla
x=range(0, 100) #List de 0 a 100
#print("valor: "+srt(x[0]))
x={ #Dic
    "Aula":"Variaveis em Python",
    "Tipo": "incializaçao em Python", 
}
#print("valor: "+x["Tipo"])
x={5,4,6,7,7,5,8,9,4} #Set
x=frozenset({5,4,8,7,7,5,3,4,2}) 
print("valor: " +str(x))
print("tipo: "+str(type(x)))
