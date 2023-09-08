#def puissance(a,b):
#   if a < 0 and b == 0:
#      return -1
#   else:
#      return a ** b
      
def puissance(a, b):
    if not type(var) is int:
        raise TypeError("Only integers are allowed")

    if b == 0:
        if a < 0:
            res = -1
        else 
            res = 1
     
    if b < 0:
        if a == 0:
            return 0
        a = 1 / a  
        b = -b  
    
    resultat = 1
    
    for _ in range(b):
        res *= a

    return res
