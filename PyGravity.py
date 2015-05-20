from libs import Vector, Particle, Physics

A = Particle(Vector(0,10.00,0), Vector(0,0,0), 1)
B = Particle(Vector(2.00,0,0), Vector(0,0,0), 100000000000)
C = Particle(Vector(-2.00,0,0), Vector(0,0,0), 100000000000)
D = Particle(Vector(4.00,0,0), Vector(0,0,0), 100000000000)

base = Physics()

base.add_obj(A)
base.add_obj(B)
base.add_obj(C)
#base.add_obj(D)

for item in base.objects:
    print item.P.show

f = base.sum_Fg_one_particle(base.objects[0])
for i in range(500):
    base.apply_gravitational_acceleration(base.objects[0])
    base.objects[0].move()
    print 'A: ', base.objects[0].P.y
    #print "force: ", f.show
    #print "volecity: ", base.objects[0].V.show


for item in base.objects:
    print item.P.show
