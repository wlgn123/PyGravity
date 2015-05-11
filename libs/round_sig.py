from math import log10, floor
def round_sig(x, sig=2):
    if x == 0:
        return 0
    else:
        return round(x, sig-int(floor(log10(x)))-1)
