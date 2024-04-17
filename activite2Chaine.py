def extraireCHaine(chainCara):
    mot1=chainCara.split()
    pyth=mot1[0]
    app=mot1[-1]
    phrase=mot1[3:6]
    inverse = chainCara[::-1]
    return pyth,app,phrase,inverse
chaine1="Python est un langage de progarmmation puissant et facile à apprendre"
result= extraireCHaine(chaine1)
print (f"1er mot:{result}")
