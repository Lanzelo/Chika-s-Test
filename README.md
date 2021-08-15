# Teste-de-Chika
 Programa que executa uma reprodução visual do Teste de Chika em Python
 
Em setembro de 2019, o jovem estudante nigeriano Chika Ofili, de apenas 12 anos, morador do Reino Unido, apresentou em sua escola um trabalho onde demonstrou ter descoberto uma metodologia rápida para testar se um número inteiro é divisível por 7.

O teste reside em:
1º Pega-se o último digito do numero inteiro e o multiplica por 5
2º Em seguida o produto é somado ao restante do numero
3º Se o resultante for divisivel por 7, o numero inteiro original também é divisivel por 7

Exemplos: 

Tome o número 532
53 + 2 x 5 = 63
63 é um múltiplo de 7, então 532 também é divisível po 7)

Ou 987

98 + 7 x 5 = 133
13 + 3 x 5 = 28
28 é um múltiplo de 7, assim como 133 e 987 também são múltiplos de 7

Em programação não é preciso um algoritmo tão completo para identificar um número divisível por 7 ou qualquer outro número.
Qualquer pessoa com conhecimento básico pode resolver isso com um if e o operador Módulo em 3 linhas de código.

Ex: 
n = int(input("Digite um número: "))
if n % 7 == 0:
   print("divisível!")

Assim como qualquer pessoa que não saiba nada de programação com uma calculadora. De modo que a ideia aqui não é criar um programa que faça a verificação, de fato, mas sim:
- um programa que mostre visualmente a execução do algoritmo implementado por Chika Ofili, de modo a facilitar a compreensão e o seu estudo na matemática. 
- utilizar a sua implementação como estudo de lógica de programação em Python

Fontes: 

https://www.correiobraziliense.com.br/app/noticia/mundo/2019/11/19/interna_mundo,807535/menino-de-12-anos-descobre-formula-matematica-que-ajuda-o-estudo-da-di.shtml

https://www.westminsterunder.org.uk/chikas-test/
