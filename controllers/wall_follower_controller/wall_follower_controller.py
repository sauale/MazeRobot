"""wall_follower_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


def run_robot(robot):


    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getDevice('motorname')
    #  ds = robot.getDevice('dsname')
    #  ds.enable(timestep)
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    
    
    left_motor = robot.getMotor('left wheel motor')
    right_motor = robot.getMotor('right wheel motor')
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    
    prox_sensors = []
    for ind in range(8):
        sensor_name = 'ps' + str(ind)
        prox_sensors.append(robot.getDistanceSensor(sensor_name))
        prox_sensors[ind].enable(timestep)
    
    
    while robot.step(timestep) != -1:
        
        for ind in range(8):
            print("ind : {}, val:{}".format(ind,prox_sensors[ind].getValue()))
        
        left_wall = prox_sensors[5].getValue() >80
        front_wall = prox_sensors[7].getValue() >80
        
        left_speed = max_speed
        right_speed = max_speed
        
        if front_wall:
            left_speed = max_speed
            right_speed = -max_speed 
        else:
            
            if left_wall:
                left_speed = max_speed
                right_speed = max_speed
            else:
                left_speed = max_speed/4
                right_speed = max_speed
                
            
                
            
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)       
   
    
    # Enter here exit cleanup code.

if __name__ == "__main__":
    
    my_robot = Robot()
    run_robot(my_robot)
    
