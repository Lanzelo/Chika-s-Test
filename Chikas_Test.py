print("Teste de Chika")
numero = input("Digite um número: ")

'''

Input entra como string
Aproveito isso para fazer a leitura do ultimo digito do numero digitado,
assim como da parte restante

Simultaneamente converto essas leituras em inteiros para iniciar o
algoritmo de verificação do Teste de Chika

'''

ultimo_dig = int(numero[-1:])  
restante = int(numero[:-1])
print(f"O último digito é {ultimo_dig} e o restante é {restante}")

while True:
    produto = ultimo_dig * 5
    montante = restante + produto
    print(f"{ultimo_dig} x 5 = {produto}")
    print(f"{restante} + {produto} = {montante}")
    if (len(str(montante)) > 2) or montante >= 84: #84 tem 2 digitos mas, junto com 91 e 98, é um multiplo de 7 não facilmente identificável, por isso o reduzo também  
        ultimo_dig = int(str(montante)[-1:])
        restante = int(str(montante)[:-1])
    else:
        break

# agora var montante assume o papel da var numero, em seguida apenas a leio com string para agilizar 
# utilizo 'While True' + 'If/Else' + 'Break' para simular um 'Do While'

if montante % 7 == 0:
    print(f"{montante} é múltiplo de 7, então {numero} é divisível por 7!")
else:
    print(f"{montante} NÃO é múltiplo de 7, então {numero} NÃO é divisível por 7!!")
