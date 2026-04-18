# ============================================================
# EXERCÍCIO 4 - Sobrescrita de Método (Method Overriding)
# Conceito: A classe filha redefine um método da classe pai
#           para adaptar seu comportamento
# ============================================================

# Classe PAI — forma genérica sem dimensões reais
class Forma:
    def area(self):
        # Retorna 0 como valor padrão (sem forma específica)
        return 0


# Classe FILHA — sobrescreve o método area() com lógica real
class Retangulo(Forma):
    # A assinatura muda: agora recebe largura e altura
    def area(self, largura, altura):
        return altura * largura  # Cálculo real da área


# --- Testando as classes ---

forma1 = Forma()
print(forma1.area(), "CM²")       # Saída: 0 CM²

retangulo1 = Retangulo()
print(retangulo1.area(5, 5), "CM²")  # Saída: 25 CM²
