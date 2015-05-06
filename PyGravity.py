from libs import Vector

a = Vector(1,2,1)
b = Vector(1,1,0)
print " Partical A at ", a.show
print " Partical B at ", b.show


for i in range(50000):
    str_a = a.show
    str_b = b.show
    a = a.add(b)    
    print str_a, '+', str_b, '=', a.show

