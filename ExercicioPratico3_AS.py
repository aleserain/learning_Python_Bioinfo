Alessandra Serain

#Exercicio 1 - a
>>> t = ('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y')
>>> len(t)
20
>>> t
('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y')


>>> 'S' in t
True
>>> t.count('S')
1
>>> t.index('S')
15
>>> 

>>> second_tupla = ('P', 'G', 'N', 'Y', 'V', 'W')
>>> 
>>> t + second_tupla
('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'P', 'G', 'N', 'Y', 'V', 'W')
>>> 
>>> t.count('G')
1
>>> 

>>> third_t = t + second_tupla
>>> third_t
('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'P', 'G', 'N', 'Y', 'V', 'W')
>>> t.count('G')
1
>>> 
>>> t.count('N')
1
>>> third_t.count('N')
2
>>> third_t.count('C')
1
>>> t.count('C')
1
>>> t.index('N')
11
>>> third_t.index('N')
11

>>> t[-5:]
('S', 'T', 'V', 'W', 'Y')
>>> third_t[-5:]
('G', 'N', 'Y', 'V', 'W')
>>> 
>>> 
>>> ################################################