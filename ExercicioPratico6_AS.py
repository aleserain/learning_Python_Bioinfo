>>> 
>>> #Exercicios praticos - 6 - Dicionarios
>>> 
>>> 
>>> pdb = {'1A8M':'471', '1TNR':'283', '2AZ5':'592', '1TNF':'471', '2TNF':'468', '2TUN':'942', '4TSV':'150', '5TSW':'900', '2E7A':'471', '6RMJ':'489'}
>>> 
>>> '2TNF' in pdb
True
>>> pdb['2TNF']
'468'
>>> 
>>> pdb['2E7A']
'471'
>>> 
>>> len(pdb)
10
>>> 
>>> pdb.keys()
dict_keys(['1A8M', '1TNR', '2AZ5', '1TNF', '2TNF', '2TUN', '4TSV', '5TSW', '2E7A', '6RMJ'])
>>> 
>>> pdb.values()
dict_values(['471', '283', '592', '471', '468', '942', '150', '900', '471', '489'])
>>> 
>>> pdb.items()
dict_items([('1A8M', '471'), ('1TNR', '283'), ('2AZ5', '592'), ('1TNF', '471'), ('2TNF', '468'), ('2TUN', '942'), ('4TSV', '150'), ('5TSW', '900'), ('2E7A', '471'), ('6RMJ', '489')])
>>> 
>>> #––––––––––––––––––––––––––––––––#––––––––––––––––––––––––––––––––––#

>>> 
>>> 
>>> #nao da pra indexar dict_keys,  n vai conseguir trabalhar como lista entao precisa atribuir variavel pra isso.
>>> 
>>> pdb_list = pdb.keys()
>>> 
>>> pdb_list
dict_keys(['1A8M', '1TNR', '2AZ5', '1TNF', '2TNF', '2TUN', '4TSV', '5TSW', '2E7A', '6RMJ'])
>>> 
>>> lista = list(pdb.keys())
>>> 
>>> lista
['1A8M', '1TNR', '2AZ5', '1TNF', '2TNF', '2TUN', '4TSV', '5TSW', '2E7A', '6RMJ']
>>> 
>>> #portanto atribuir list(.....) para que ele entenda que aquilo vai ser lista e nao so usar =
>>> 
>>> 
>>> #nas tuplas acontece o mesmo:
>>> 
>>> tuplas = tuple(pdb.keys())
>>> 
>>> tuplas
('1A8M', '1TNR', '2AZ5', '1TNF', '2TNF', '2TUN', '4TSV', '5TSW', '2E7A', '6RMJ')
>>> 
>>> tuplas = tuple(pdb.items())
>>> 
>>> tuplas
(('1A8M', '471'), ('1TNR', '283'), ('2AZ5', '592'), ('1TNF', '471'), ('2TNF', '468'), ('2TUN', '942'), ('4TSV', '150'), ('5TSW', '900'), ('2E7A', '471'), ('6RMJ', '489'))
>>> 
>>> tuplas[0]
('1A8M', '471')
>>> 
>>> lista[0]
'1A8M'
>>> 
>>> #lista foi feito com keys, mas fazer com items pra ficar a posiçao chave:valor
>>> 
>>> 
>>> 
>>> 