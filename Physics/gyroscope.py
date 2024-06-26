from vpython import *

mass = 2.0
moi = 10.0 
damping_coeff = 0.1 
gravity = vector(0, -9.8, 0)  

scene = canvas(title = 'Gyroscope Simulation', width = 800, height = 800, center = vector(0, 0, 0))

gyro = cylinder(pos = vector(0, 0, 0), axis = vector(0, -1, 0), length = 1.5, radius = 0.025)
ang_vel = vector(0, 0, 1) 

time_step = 0.01
num_steps = 10000

enclosure = box(pos = vector(0, 0, 0), size = vector(2, 2, 2), color = color.white, opacity = 0.1, wireframe = True)
serrated_disk = ring(pos = gyro.pos + gyro.axis, axis = gyro.axis, radius = 0.15, thickness = 0.02, color = color.white, make_trail = True, retain = 20)
perp_line = cylinder(pos = vector(0, 0, 0), axis = vector(0, 1, 0), radius = 0.006, color = color.white)
arrowhead = cone(pos = vector(0, 1, 0), axis = vector(0, 0.1, 0), radius = 0.05, color = color.yellow)
pivot_sphere = sphere(pos = gyro.pos, radius = 0.05, color = color.red)

scene.forward = vector(0, 0, -1)  
scene.up = vector(0, 1, 0) 

for step in range(num_steps):
    rate(60)

    friction_torque = -damping_coeff * ang_vel

    angle_of_rotation = acos(ang_vel.y / mag(ang_vel))
    gravity_torque = -mass * mag(gravity) * 0.5 * sin(angle_of_rotation) * vector(0, 1, 0)

    total_torque = friction_torque + gravity_torque

    angular_acceleration = total_torque / moi
    ang_vel += angular_acceleration * time_step

    pivot_sphere.pos = gyro.pos
    gyro.rotate(angle = mag(ang_vel) * time_step, axis = norm(ang_vel), origin = vector(0, 0, 0))
    
    serrated_disk.pos = gyro.pos + gyro.axis
    serrated_disk.axis = gyro.axis

scene.waitfor('click')