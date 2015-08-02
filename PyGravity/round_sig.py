'''
.. module:: RoundSig
   :platform: Unix
   :synopsis: Rounding to sig digits

.. moduleauthor:: Russell Loewe <russloewe@gmail.com>

'''
from math import log10, floor
def round_sig(number, sig=2):
    '''
    Round to significant digits
    '''
    if number == 0:
        return 0
    if number < 0:
        number = -number
        return round(number, sig-int(floor(log10(number)))-1) * (-1)
    return round(number, sig-int(floor(log10(number)))-1)
