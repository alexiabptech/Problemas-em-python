import math  

def area_pentagono(lado):
    converte_p_radiano =  math.radians(36)
    #x = (lado/2) / (a)

    x = math.tan(converte_p_radiano) 

    a = (lado/2) / x

    area_total = ((lado * a)/2) * 5
    
    return area_total