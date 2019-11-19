import numpy
import matplotlib.pyplot

def veerkracht():
    num_steps = 1000
    tijdsinterval = 0.1
    friction = 0.002
    s = -0.1 #stugheid van veer


    t = numpy.zeros(num_steps + 1)
    x = numpy.zeros(num_steps + 1)
    v = numpy.zeros(num_steps + 1)

    x[0] = 5


    for step in range(num_steps):
        t[step + 1] = t[step] + tijdsinterval
        v[step + 1] = v[step] + s * x[step] - friction * v[step]
        x[step + 1] = x[step] + v[step + 1] * tijdsinterval


    axes_height = matplotlib.pyplot.subplot(211)
    matplotlib.pyplot.plot(t, x)
    axes_velocity = matplotlib.pyplot.subplot(212)
    matplotlib.pyplot.plot(t, v)
    axes_height.set_ylabel('Height in m')
    axes_velocity.set_ylabel('Velocity in m/s')
    axes_velocity.set_xlabel('Time in s')
    matplotlib.pyplot.show()



veerkracht()
