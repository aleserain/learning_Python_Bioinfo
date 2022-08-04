Alessandra Serain

#Exercicio 1

>>> seq = 'VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'
>>> seq
'VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'
>>> 
>>> len(seq)
157
>>> 
>>> seq.count('LL')
4
>>> 
>>> seq.count('LLL')
0
>>> 
>>> seq.find('GG')
120
>>> seq.find('RR')
30
>>> 
>>> seq[1:100]
'RSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSP'
>>> seq[0:99]
'VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKS'
>>> seq[0:100] #correto porque nao conta o 100 e o zero é contado 

>>> seq.replace('SSSR', 'AAAA')
'VRAAAATPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'
>>> seq.replace('SSSR', 'A')
'VRATPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'
>>> 
>>> seq = seq.replace('SSSR', 'AAAA')
>>> seq
'VRAAAATPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'
>>> seq.split('AAAA')
['VR', 'TPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL']
>>> 
>>> #Obs.: se eu emitir o comando somente com um A, ele poderia cortar em outros locais com somente um A e nao nos que foram substituidos. Poderia tambem usar uma letra diferente destas para nao gerar erro.
>>> 
>>> 
>>> 

#Exercicio 2

>>> seq = "As proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos. Existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. A esses aminoácidos, foram atribuídas abreviações de 3 letras e símbolos de 1 letra. As abreviações de 3 letras são bastante evidentes consistindo nas três primeiras letras do se nome."
>>> 
>>> seq
'As proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos. Existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. A esses aminoácidos, foram atribuídas abreviações de 3 letras e símbolos de 1 letra. As abreviações de 3 letras são bastante evidentes consistindo nas três primeiras letras do se nome.'
>>> 
>>> seq.upper()
'AS PROTEÍNAS SÃO CADEIAS POLIPEPTÍDICAS FORMADAS PELA LIGAÇÃO PEPTÍDICA ENTRE RESÍDUOS DE AMINOÁCIDOS. EXISTEM 20 TIPOS DE AMINOÁCIDOS COMUMENTE ENCONTRADOS NOS SERES VIVOS. A ESSES AMINOÁCIDOS, FORAM ATRIBUÍDAS ABREVIAÇÕES DE 3 LETRAS E SÍMBOLOS DE 1 LETRA. AS ABREVIAÇÕES DE 3 LETRAS SÃO BASTANTE EVIDENTES CONSISTINDO NAS TRÊS PRIMEIRAS LETRAS DO SE NOME.'
>>> 
>>> seq.lower()
'as proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos. existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. a esses aminoácidos, foram atribuídas abreviações de 3 letras e símbolos de 1 letra. as abreviações de 3 letras são bastante evidentes consistindo nas três primeiras letras do se nome.'
>>> 
>>> seq.title()
'As ProteíNas SãO Cadeias PolipeptíDicas Formadas Pela LigaçÃO PeptíDica Entre ResíDuos De AminoáCidos. Existem 20 Tipos De AminoáCidos Comumente Encontrados Nos Seres Vivos. A Esses AminoáCidos, Foram AtribuíDas AbreviaçÕEs De 3 Letras E SíMbolos De 1 Letra. As AbreviaçÕEs De 3 Letras SãO Bastante Evidentes Consistindo Nas TrêS Primeiras Letras Do Se Nome.'
>>> 
>>> #vejo que tem um erro que se repete apos cada letra com acento. Como manter a palavra toda em minusculo?
>>> 
>>> seq.title().swapcase()
'aS pROTEÍnAS sÃo cADEIAS pOLIPEPTÍdICAS fORMADAS pELA lIGAÇão pEPTÍdICA eNTRE rESÍdUOS dE aMINOÁcIDOS. eXISTEM 20 tIPOS dE aMINOÁcIDOS cOMUMENTE eNCONTRADOS nOS sERES vIVOS. a eSSES aMINOÁcIDOS, fORAM aTRIBUÍdAS aBREVIAÇõeS dE 3 lETRAS e sÍmBOLOS dE 1 lETRA. aS aBREVIAÇõeS dE 3 lETRAS sÃo bASTANTE eVIDENTES cONSISTINDO nAS tRÊs pRIMEIRAS lETRAS dO sE nOME.'
>>> seq.title().swapcase().swapcase()
'As ProteíNas SãO Cadeias PolipeptíDicas Formadas Pela LigaçÃO PeptíDica Entre ResíDuos De AminoáCidos. Existem 20 Tipos De AminoáCidos Comumente Encontrados Nos Seres Vivos. A Esses AminoáCidos, Foram AtribuíDas AbreviaçÕEs De 3 Letras E SíMbolos De 1 Letra. As AbreviaçÕEs De 3 Letras SãO Bastante Evidentes Consistindo Nas TrêS Primeiras Letras Do Se Nome.'
>>> 

#Exercicio 3

>>> insulin_signal = 'MALWMRLLPLLALLALWGPDPAAA'
>>> 
>>> len(insulin_signal)
24
>>> 
>>> insulin_signal.split('LLALLALWG')
['MALWMRLLP', 'PDPAAA']
>>> >>> ''.join(insulin_signal.split('LLALLALWG'))
'MALWMRLLPPDPAAA'
>>> 
>>> insulin_signal = ''.join(insulin_signal.split('LLALLALWG'))
>>> insulin_signal
'MALWMRLLPPDPAAA'
>>> insulin_signal.replace('DPAAA', 'LLALL')
'MALWMRLLPPLLALL'
>>> 

#Exercicio 4

>>> 
>>> seq = 'GATGGAACTTGACGTAAACCTATATT'
>>>> seq.replace('T', 'U')
'GAUGGAACUUGACGUAAACCUAUAUU'
>>> 
>>> #the end
>>> 
>>> 

>> 
