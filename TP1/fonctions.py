def puissance(a, b):
    
    if b < 0:
        raise ValueError("L'exposant b doit être positif ou nul")
    
    if b == 0:
        return 1
    
    resultat = 1
    for _ in range(b):
        resultat *= a
    
    return resultat


