# exercicios try except

# # # 21: Conversor de Temperatura Celsius a farenheit
# # try:
# #     celsius =  int(input("Please enter: Celsius grades"))
# #     farenheit = (celsius * 9/5) + 32

# # except ValueError:
# #     print(f" Please enter a number dont be able to read string formats")

# # else:
# #     print(f" The celsius grades {celsius} ºC in farenheit is {farenheit} ºF")



# 22: Verificador de Palíndromo








# 23: Calculadora Simples
# 24: Clasificador de Números


# 25: Conversión de Tipo com Validação
try:
    entrada_lista = input("Insere numeros seguidos de uma virgula:n1,n2,....")
    numeros_str =entrada_lista.split(",")
    numeros_int = []
    for n in numeros_str:
        numeros_int.append(int(n.strip()))
    print(f" lista de inteiros {numeros_int}")



except ValueError :
    print(" Na hora de inserir foi inserido alguma carater invalido ")

