class Tamagotchi
    nombre=""
    hambre=0
    animo=0
    energia=0

    def_init_(self,nombre, hambre,animo,energia):
        self.nombre=nombre
        self.hambre=hambre
        self.animo=animo
        self.energia=energia

    def jugar(self):
        self.animo+=1
        self.energia-=1

    def alimentar(self):
        self.animo+=1
        self.hambre-=1     
    
    def dormir(self):
        self.animo+=1
        self.energia-=1 
        print("Tengo suenio")

    def pasar(self):
        self.animo+=1
        self.hambre-=1                      

#Programa Principal
t = Tamagotchi("Tamagochito", 10, 10, 10)
print(t)
t.dormir()
print(t)
t.jugar()
print(t)
t.alimentar()
print(t)
t.pasar()

t.animo
