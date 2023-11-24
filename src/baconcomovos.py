"""
1 - Receber um número inteiro
2 - Saber se o número é multiplo de 3 e 5
    Bacon com ovos
3 - Saber se o numero é mutiplo somente de 3
    Bacon
4 - Saber se o numero é multiplo somente de 5
    Ovos
5 - Saber se o número NÃO é multiplo de 3 e 5:
    Passar fome
"""

def bacon_com_ovos(n):
    assert isinstance(n,int), 'n deve ser int'
    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
    if n % 3 == 0:
        return 'Bacon'
    if n % 5 == 0:
        return 'Ovos'
    return 'Passar fome'
