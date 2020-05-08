from math import sqrt

def hypotenuse(a,b):
    c_to_the_2 = a**2 + b**2
    print(c_to_the_2**.5)

    
    return c_to_the_2**.5


# cf is curection factor
# sl is sugar leval in mg/dl
def blood_sugar_currection(cf,sl):
    resalt = 0
    if sl < 100:
        resalt = (sl - 100)/cf
    else:
        resalt = (sl - 100)/cf
    print(resalt)
    return resalt

hypotenuse(3,4)

blood_sugar_currection(40,300)