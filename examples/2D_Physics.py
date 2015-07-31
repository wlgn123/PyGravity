import matplotlib.pyplot as plt
import PyGravity

base = PyGravity.PyGravity()    # start by making base instance
base.read_file('example_data.csv')
base.set_time_interval(100)

ax = []
ay = []
bx = []
by = []
cx = []
cy = []
dx = []
dy = []

for i in range(200000):
        if i % 200 == 0:
                #some print statements to watch while the simulator runs
                print i
                print base.particle_list[0].P

                #plot all the postions
                ax.append(base.particle_list[0].P[0])
                ay.append(base.particle_list[0].P[1])
                bx.append(base.particle_list[1].P[0])
                by.append(base.particle_list[1].P[1])
                cx.append(base.particle_list[2].P[0])
                cy.append(base.particle_list[2].P[1])
                dx.append(base.particle_list[3].P[0])
                dy.append(base.particle_list[3].P[1])

                #Stop when a particle starts escaping the system
                if PyGravity.Physics.escaping(base.particle_list) != []:
                        print PyGravity.Physics.escaping(base.particle_list)
                        break

        base.step_all()

print 'Time: ', (base.currant_time), 'mins'
plt.scatter(ax, ay, s=10, c='b', alpha=0.5)
plt.scatter(bx, by, s=10, c='r', alpha=0.5)
plt.scatter(cx, cy, s=10, c='g', alpha=0.5)
plt.scatter(dx, dy, s=10, c='y', alpha=0.5)
plt.show()
