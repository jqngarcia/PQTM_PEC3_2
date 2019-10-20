class Dog:
    especie = 'caniche'

    def __init__(self, name, age):
        self.name = name
        self.age = age


bambi = Dog("Bambi", 5)
mikey = Dog("Rufus", 6)
Wanda = Dog("Wanda", 2)
Lola = Dog("Lola", 3)
Canela = Dog("Canela", 7)

print("{} tiene {} y {} tiene {}". format(bambi.name, bambi.age, mikey.name, mikey.age, Wanda.name, Wanda.age, Lola.name, Lola.age, Canela.name, Canela.age))
print("{} tiene {} y {} tiene {}". format(Wanda.name, Wanda.age, Lola.name, Lola.age))
print("{} tiene {}". format(Canela.name, Canela.age))


if bambi.especie == "caniche":
    print("{0} en un {1}!".format(bambi.name, bambi.especie))

def get_biggest_number (*lista):
    
    max=0
    for i in lista:
        if i>max:
            max=i
    return (max)

print ("El perro mayor tiene", get_biggest_number(bambi.age, mikey.age, Wanda.age, Lola.age, Canela.age), "años")

#print ("El numero mayor es:", get_biggest_number(1,2,3,4,6,7,99,88,999))

