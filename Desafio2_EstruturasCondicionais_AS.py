>>> #Desafio
>>>
>>>#Exercicio 1
>>>
>>> Seq_A = 'LRSSSQNSSDKPVAHVVANHQVEEQLEWLSQRANALLANGMDLKDNQLVVPADGLYLVYSQVLFKGQGCPDYVLLTHTVSLRSSSDK'
>>> Seq_B = 'KPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSS'
>>> 
>>> Seq_C = 'CPQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCR' 
>>> 
>>> len(Seq_A)
87
>>> len(Seq_B)
79
>>> len(Seq_C)
85
>>> 
>>> if len(Seq_A) > 80:
...     print('A sequencia de A é maior que 80 aa')
... 
A sequencia de A é maior que 80
>>> 
>>> if len(Seq_B) > 80:
...     print('A sequencia de B é maior que 80 aa')
... else:
...     print('A sequencia de B é menor que 80 aa')
... 
A sequencia de B é menor que 80
>>> 
>>> if len(Seq_C) > 80:
...     print('A sequencia de C é maior que 80 aa')
... 
A sequencia de C é maior que 80
>>> 
>>> 
>>> #Exercicio 2
>>>
>>> if (((len(Seq_A) + len(Seq_B) + len(Seq_C))/3) < len(Seq_C)):
...     print('Esta sequencia é maior do que a média das sequencias')                                 ... 
Esta sequencia é maior do que a média das sequencias
>>> 
>>> if (((len(Seq_A) + len(Seq_B) + len(Seq_C))/3) < len(Seq_B)):
...     print('Esta sequencia é maior que a média das sequencias')
... else:
...     print('Esta sequencia é menor do  que a média das sequencias')
... 
Esta sequencia é menor do  que a média das sequencias
>>> 
>>> if (((len(Seq_A) + len(Seq_B) + len(Seq_C))/3) < len(Seq_A)):
...     print('Esta sequencia é maior do que a média das sequencias')
... 
Esta sequencia é maior do que a média das sequencias
>>>
>>> ((len(Seq_A) + len(Seq_B) + len(Seq_C))/3) 
83.66666666666667
>>>
>>>
>>> #Exercicio 3
>>> 
>>> if 'H' in Seq_B and 'P' not in Seq_B:
...     print('Esta sequencia possui histidina e nao possui Prolina')
... 
>>> 
>>> if 'H' in Seq_A and 'P' not in Seq_A:
...     print('Esta sequencia possui histidina e nao possui Prolina')
... 
>>> 
>>> if 'H' in Seq_C and 'P' not in Seq_C:
...     print('Esta sequencia possui histidina e nao possui Prolina')
... 
>>> 
>>> 'H' in Seq_A and 'P' not in Seq_A
False
>>> 'H' in Seq_B and 'P' not in Seq_B
False
>>> 'H' in Seq_C and 'P' not in Seq_C
False
>>> 
>>> #Exercicio 4
>>> 
>>> if len(Seq_A) > len(Seq_B) and len(Seq_A) > len(Seq_C):
...     print('A sequencia A é a maior')
... elif len(Seq_B) > len(Seq_A) and len(Seq_B) > len(Seq_C):
...     print('A sequencia B é a maior')
... elif len(Seq_C) > len(Seq_A) and len(Seq_C) > len(Seq_B):
...     print('A sequencia C é a maior')
... 
A sequencia A é a maior
>>> 
>>> #Exercicio 5
>>> 
>>> tam_A = [len(Seq_A)]
>>> tam_B = [len(Seq_B)]
>>> tam_C = [len(Seq_C)]
>>> 
>>> verif = [(len(Seq_A)), (len(Seq_B)), (len(Seq_C))]
>>> 
>>> verif.sort()
>>> print(verif)
[79, 85, 87]
>>>
>>> if len(Seq_A) > len(Seq_B) > len(Seq_C):
...     print('Seq_A > Seq_B > Seq_C')
... elif len(Seq_B) > len(Seq_C) > len(Seq_A):
...     print('Seq_B > Seq_C > Seq_A')
... elif len(Seq_C) > len(Seq_A) > len(Seq_B):
...     print('Seq_C > Seq_A > Seq_B')
... elif len(Seq_C) > len(Seq_B) > len(Seq_A):
...     print('Seq_C > Seq_B > Seq_A')
... elif len(Seq_A) > len(Seq_C) > len(Seq_B):
...     print('Seq_A > Seq_C > Seq_B')
... elif len(Seq_B) > len(Seq_A) > len(Seq_C):
...     print('Seq_B > Seq_A > Seq_C')
... 
Seq_A > Seq_C > Seq_B
>>> 
>>>
>>>#########################################################



