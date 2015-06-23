from math import log10, floor
def round_sig(x, sig=2):
    if x == 0:
        return 0
    if x < 0:
        x = -x
        return round(x, sig-int(floor(log10(x)))-1) * (-1)
    
    return round(x, sig-int(floor(log10(x)))-1)
