Last login: Mon Jul 25 14:19:51 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
Set:~ alessandraserain$ python3
Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> #Exercicios praticos 5 - Conjuntos
>>> 
>>> #Exercicio 1
>>> 
>>> f1 = {1.9, 1.8, 5.7, 1.6, 5.8, 1.7, 9.6, 5.9, 9.5, 6.5, 6.2, 1.1, 4.4, 3.5, 2.9, 4.7, 4.6, 5.2, 5.3}
>>> 
>>> f2 = {4.7, 3.6, 6.2, 7.1, 7, 5.6, 5.7, 3.4, 3.3, 2.1, 3.8, 3.9, 5, 5.1, 1.9, 9.5, 1.0, 1.3, 5.4}
>>> 
>>> f3 = {2.2, 3.3, 5.1, 3, 3.7, 9.1, 8.8, 8.5, 2, 4.1, 6.1, 4.9, 1.1, 0.5, 0.8, 3.2, 6.9, 9.3, 9.5}
>>> 
>>> f1.difference(f2)
{1.7, 1.6, 1.8, 4.4, 5.9, 5.8, 6.5, 5.3, 9.6, 5.2, 3.5, 4.6, 1.1, 2.9}
>>> 
>>> f1.difference(f3)
{1.7, 1.6, 1.8, 1.9, 5.8, 5.7, 5.9, 6.5, 9.6, 6.2, 4.4, 5.3, 5.2, 2.9, 3.5, 4.6, 4.7}
>>> 
>>> f2.difference(f3)
{1.9, 2.1, 3.6, 4.7, 5.6, 6.2, 7, 7.1, 5.7, 3.4, 3.8, 5, 5.4, 1.0, 3.9, 1.3}
>>> 
>>> 
>>> f1.intersection(f2)
{1.9, 4.7, 5.7, 6.2, 9.5}
>>> 
>>> f1.intersection(f3)
{1.1, 9.5}
>>> 
>>> f2.intersection(f3)
{9.5, 3.3, 5.1}
>>> 
>>> f4 = f1.union(f2)
>>> f5 = f4.union(f3)
>>> 
>>> f5
{0.5, 1.7, 1.9, 1.8, 1.6, 5.8, 5.7, 5.9, 6.5, 9.6, 9.5, 6.2, 4.4, 5.3, 5.2, 7, 3.5, 3, 2, 4.6, 4.1, 4.9, 5.6, 5, 5.1, 5.4, 1.0, 6.1, 6.9, 7.1, 1.1, 8.8, 8.5, 2.1, 9.1, 9.3, 3.6, 2.2, 3.3, 3.8, 3.7, 3.2, 0.8, 4.7, 1.3, 2.9, 3.4, 3.9}
>>> 

#Ou poderia fazer método update: f1.update(f2, f3)



>>> len(f5)
48
>>> 
>>> len(f1)
19
>>> len(f2)
19
>>> len(f3)
19
>>> 
>>> 
>>> #Exercicio 2
>>> 
>>> A = {3, 6, 9, 12, 15, 18, 21, 24, 28, 27}
>>> B = {2, 6, 8, 10, 14, 16, 18, 20, 22, 24}
>>> C = {2, 6, 10, 18, 20}
>>> D = {1, 30, 5, 11, 17, 16, 22, 26}
>>> 
>>> A.intersection(B)
{24, 18, 6}
>>> 
>>> A.difference(B)
{3, 9, 12, 15, 21, 27, 28}
>>> 
>>> A.isdisjoint(D)
True
>>> B.isdisjoint(D)
False
>>> 
>>> C.issubset(A)
False
>>> C.issubset(B)
True
>>> 
>>> 
>>> E = {18, 23, 25, 63}
>>> 
>>> D.union(E)
{1, 5, 11, 16, 17, 18, 22, 23, 25, 26, 30, 63}

#novamente: ou D.update([18, 23, 65, 63])
>>> 
>>> ##########################################################################