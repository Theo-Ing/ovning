CURRENT_YEAR = 2020

def years_since_start(a):
    last_digits = int(a[2:])
    if CURRENT_YEAR-(1900+last_digits)>100:
        return CURRENT_YEAR-(2000+last_digits)
    else:
        return CURRENT_YEAR-(1900+last_digits)


print(years_since_start("F-97"))

#Input "F-XX"