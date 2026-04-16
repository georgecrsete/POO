class Forma:
    def area(self):
        return 0
class Retangulo(Forma):
    def area(self, largura, altura):
        return altura * largura 


forma1 = Forma()
print(forma1.area(),"CM²")
retangulo1 = Retangulo()
print(retangulo1.area(5,5),"CM²")