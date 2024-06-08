def calcular_area_paredes(comprimento, largura, altura):
    # Calcula a área das quatro paredes
    area_paredes = 2 * altura * (comprimento + largura)
    return area_paredes

def calcular_area_teto(comprimento, largura):
    # Calcula a área do teto
    area_teto = comprimento * largura
    return area_teto

def calcular_litros_tinta(area, cobertura_por_litro=10):
    # Calcula a quantidade de litros de tinta necessária
    litros_tinta = area / cobertura_por_litro
    return litros_tinta

def main():
    print("Bem-vindo ao calculador de tinta!")
    
    # Solicita as dimensões do cômodo
    comprimento = float(input("Informe o comprimento do cômodo em metros: "))
    largura = float(input("Informe a largura do cômodo em metros: "))
    altura = float(input("Informe a altura do cômodo em metros: "))
    
    # Calcula a área das paredes
    area_paredes = calcular_area_paredes(comprimento, largura, altura)
    
    # Pergunta se o teto será pintado
    pintar_teto = input("Deseja pintar o teto? (sim/não): ").strip().lower()
    
    # Calcula a área do teto, se necessário
    area_teto = 0
    if pintar_teto == 'sim':
        area_teto = calcular_area_teto(comprimento, largura)
    
    # Área total a ser pintada
    area_total = area_paredes + area_teto
    
    # Calcula a quantidade de tinta necessária
    litros_tinta = calcular_litros_tinta(area_total)
    
    print(f"\nA área total a ser pintada é de {area_total:.2f} metros quadrados.")
    print(f"Você precisará de aproximadamente {litros_tinta:.2f} litros de tinta.")
    
if __name__ == "__main__":
    main()
