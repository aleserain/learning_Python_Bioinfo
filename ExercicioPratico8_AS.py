>>> #Exercicios Praticos 8 - Estruturas condicionais 
>>> 
>>> #Exercicio 1
>>> 
>>> #variavel de tamanho de sequencia biologica = x
>>> #aceita se tamanho = ou > 50
>>> #Portanto:
>>> 
>>> x=50
>>> 
>>> y=60
>>> z=10
>>> 
>>> if y==x or y>x:
...     print('Aceita para analise')
... elif y<x:
...     print('Nao aceita para analise')
... 
Aceita para analise
>>> 
>>> if z==x or z>x:
...     print('Aceita para analise')
... elif z<x:
...     print('Nao aceita para analise')
... 
Nao aceita para analise
>>> 
>>> 
>>> 
>>> 
>>> #Exercicio 2
>>> 
>>> #peptideo =2 >2 mas <50 aminoacidos
>>> #peptideo = p
>>> 
>>> p=30
>>> 
>>> if p==2 or p>2 and p<50:
...     print('p é um aminoacido')
... 
p é um aminoacido
>>> 
>>> p=52
>>> 
>>> if p==2 or p>2 and p<50:
...     print('p é um aminoacido')
... elif p>50 or p<2:
...     print('p nao é um aminoacido')
... 
p nao é um aminoacido
>>> 
>>>#poderia usar p>= para maior ou igual
>>>#poderia escrever a frase print('p nao é um aminoacido: tamanho', len(seq))
>>>#ao inves de simplesmente p, poderia usar len(seq) 
>>>
>>> #Exercicio 3
>>> 
>>> #2 aminoacidos = dipeptideo
>>> #3 aminoacidos = tripeptideo
>>> #4 ou mais aminoacidos até 50 = polipeptideo
>>> 
>>> a=2
>>> if a == 2:
...     print('Este é um dipeptideo')
... elif a == 3:
...     print('Este é um tripeptideo')
... elif a == 4 or a > 4 and a < 50:
...     print('Este é um polipeptideo')
... 
Este é um dipeptideo
>>> 
>>> b=3
>>> if b == 2:
...     print('Este é um dipeptideo')
... elif b == 3:
...     print('Este é um tripeptideo')
... elif b == 4 or b > 4 and b < 50:
...     print('Este é um polipeptideo')
... 
Este é um tripeptideo
>>> 
>>> c=10
>>> if c == 2:
...     print('Este é um dipeptideo')
... elif c == 3:
...     print('Este é um tripeptideo')
... elif c == 4 or c > 4 and c < 50:
...     print('Este é um polipeptideo')
... 
Este é um polipeptideo
>>> 
>>> d=52
>>> if d == 2:
...     print('Este é um dipeptideo')
... elif d == 3:
...     print('Este é um tripeptideo')
... elif d == 4 or d > 4 and d < 50:
...     print('Este é um polipeptideo')
... elif d > 50:
...     print('Este nao é um polipeptideo')
... 
Este nao é um polipeptideo
>>> 
>>>#poderia colocar else no final sendo 'nao é um peptideo'
>>>
>>>#Exercicio 4 e 5
>>>
>>> Hidrofobico = ['I', 'V', 'L', 'M', 'C', 'A', 'T', 'F', 'Y', 'W', 'H', 'K']
>>> Pequeno = ['P', 'A', 'G', 'C', 'S', 'T', 'D', 'N', 'V']
>>> Polar = ['C', 'S', 'T', 'N', 'D', 'Q', 'Y', 'W', 'H', 'K', 'R', 'E']
>>> Carregado = ['D', 'E', 'R', 'K', 'H']
>>> Aromatico = ['F', 'Y', 'W', 'H']
>>> Minusculo = ['A', 'C', 'G', 'S']
>>> Alifatico = ['I', 'L', 'V']
>>> Hidroxila = ['T', 'S']
>>> Acido = ['N', 'Q']
>>> Enxofre = ['C', 'M']
>>> 
>>> aa = 'E'
>>> 
>>> if aa in Hidrofobico:
...     print('Este aminoacido é hidrofobico')
... 
>>> if aa in Pequeno:
...     print('Este aminoacido é pequeno')
... 
>>> if aa in Polar:
...     print('Este aminoacido é polar')
... else:
...     print('Este aminoacido é apolar')
... 
Este aminoacido é polar
>>> 
>>> if aa in Carregado:
...     print('Este aminoacido é Carregado')
... else:
...     print('Este aminoacido é Neutro')
... 
Este aminoacido é Carregado
>>> 
>>> if aa in Aromatico:
...     print('Este aminoacido é Aromatico')
... 
>>> if aa in Aromatico:
...     print('Este aminoacido é Minusculo')
... 
>>> if aa in Alifatico:
...     print('Este aminoacido é Alifatico')
... 
>>> if aa in Hidroxila:
...     print('Este aminoacido tem hidroxila')
... 
>>> if aa in Hidroxila:
...     print('Este aminoacido tem grupo acido')
... 
>>> if aa in Enxofre:
...     print('Este aminoacido tem enxofre')
... 
>>>
>>>#Poderia fazer os exercicios separado, em que testa todos primeiros com if sequecialmente e o segundo com if (not aa in polar) or (not aa in carregado):
>>> 
>>> #Exercicio 6
>>> 
>>> Nucleotideos = ['A', 'G', 'C', 'T']
>>> Nucl_purinicos = ['A', 'G']
>>> Nucl_primidinicos = ['C', 'T']
>>> 
>>> n = 'B'
>>> 
>>> if n in Nucleotideos:
...     print('Este é um nucleotideo')
... elif n in Nucl_purinicos:
...     print('Este é um nucleotideo da classe das pourinas')
... elif n in Nucl_primidinicos:
...     print('Este é um nucleotideo da classe das primidinas')
... else:
...     print('Este nao é um nucleotideo')
... 
Este nao é um nucleotideo
>>> 
>>> n = 'A'
>>> 
>>> if n in Nucleotideos:
...     print('Este é um nucleotideo')
... elif n in Nucl_purinicos:
...     print('Este é um nucleotideo da classe das purinas')
... elif n in Nucl_primidinicos:
...     print('Este é um nucleotideo da classe das primidinas')
... else:
...     print('Este nao é um nucleotideo')
... 
Este é um nucleotideo
>>> 
>>> if n in Nucl_purinicos:
...     print('Este é um nucleotideo da classe das purinas')
... elif n in Nucl_primidinicos:
...     print('Este é um nucleotideo da classe das primidinas')
... else:
...     print('Este nao é um nucleotideo')
... 
Este é um nucleotideo da classe das purinas
>>>
>>>#poderia usar um if pra nucleotideo e depois dentro desse if, colocar um if e elif pra testar qual e ao final um else pra ver se é invalido.
>>> 
>>> if n in Nucleotideos:
...     print('Este é um nucleotideo')
...     if n in Nucl_purinicos:
...             print('Este é um nucleotideo da classe das purinas')
...     elif n in Nucl_primidinicos:
...             print('Este é um nucleotideo da classe das primidinas')
... else:
...     print('Este nao é um nucleotideo')
... 
Este é um nucleotideo
Este é um nucleotideo da classe das purinas
>>> 
>>>
>>>###############################################################
