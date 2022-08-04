>>> #Desafio 1 - Operadores
>>> 
>>> 
>>> #Primeiro passo: calcular todas médias das coordenadas
>>> #Sendo g1 o primeiro residuo de glicina e g2 o segundo.
>>> 
>>> mxg1 = (108.304 + 108.477 + 109.907 + 110.821)/4
>>> mxg1
109.37725
>>> 
>>> myg1 = (100.827 + 100.389 + 100.555 + 100.799)/4
>>> myg1
100.64250000000001
>>> 
>>> mzg1 = (67.992 + 69.362 + 69.817 + 69.027)/4
>>> mzg1
69.0495
>>> 
>>> mxg2 = (107.670 + 108.477 + 109.513 + 110.667)/4
>>> mxg2
109.08175
>>> 
>>> myg2 = (101.359 + 100.389 + 101.011 + 100.572)/4
>>> myg2
100.83275
>>> 
>>> mzg2 = (70.074 + 69.362 + 68.450 + 68.425)/4
>>> mzg2
69.07775
>>> 
>>> #Segundo passo: calcular o desvio, começando pela somatoria e potencia
>>> 
>>> RMSD1 = ((mxg1 - mxg2)**2 + (myg1 - myg2)**2 + (mzg1 - mzg2)**2)
>>> RMSD1
0.1243133749999993
>>> 
>>> #Terceiro passo: calcular o restante da formula
>>> 
>>> 
>>> RMSD = ((RMSD1/4)**1/2)
>>> RMSD
0.015539171874999912
>>> 
>>> #Formula completa:
>>> 
>>> RMSD = ((((mxg1 - mxg2)**2 + (myg1 - myg2)**2 + (mzg1 - mzg2)**2)/4)**1/2)
>>> RMSD
0.015539171874999912
>>> 
>>> 
>>> 
>>> #Exercicio 2
>>> 
>>> SeqA = 'ATGATCTCGTAATTAACCGGAATTTTGGGCC'
>>> 
>>> SeqB = 'GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA'
>>> 
>>> len(SeqA)
31
>>> SeqA.count('G')
7
>>> SeqA.count('C')
6
>>> ConteudoGC_SeqA = ((7+6)/31)*100
>>> ConteudoGC_SeqA
41.935483870967744
>>> 
>>> ConteudoGC_SeqB = (((SeqB.count('G')) + (SeqB.count('C')))/((len(SeqB)))*100)
>>> ConteudoGC_SeqB
44.44444444444444
>>> 
>>> ###############THE END####################


#Correçao formula exercicio 1 - deveria fazer a diferença de cada atomo primeiro, entre N do x glicina 1 e 2, entre N do y glicina 1 e 2, N do z da glicina 1 e 2 e assim com os outros.

>>> 
>>> 
>>> #Primeiro ver as diferenças entre cada atomo
>>> 
>>> atomoN = ((108.304 - 107.670)**2 + (100.827 - 101.359)**2 + (67.992 - 70.074)**2)
>>> atomoN
5.019703999999971
>>> 
>>> atomoCA = ((108.477 - 108.477)**2 + (100.389 - 100.389)**2 + (69.362 - 69.362)**2)
>>> atomoCA
0.0
>>> atomoC = ((109.907 - 109.513)**2 + (100.555 - 101.011)**2 + (69.817 - 68.450)**2)
>>> atomoC
2.231860999999956
>>> 
>>> atomoO = ((110.821 - 110.667)**2 + (100.799 - 100.572)**2 + (69.027 - 68.425)**2)
>>> atomoO
0.4376490000000053
>>> 
>>> RMSD = (((atomoN + atomoCA + atomoC + atomoO)/4)**(1/2))
>>> RMSD
1.3864716008631346
>>> 
