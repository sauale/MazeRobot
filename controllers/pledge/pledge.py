"""pledge_controller"""


from controller import Robot


def run_robot(robot):


    # gaunamas world laiko žingnis
    timestep = int(robot.getBasicTimeStep())
    
    # nustatomas motoru max greitis
    max_speed = 6.28
    
    counter =0 
    
    forward = False
    #inicializuojami motorai, nustatomi ju pradiniai greiciai
    left_motor = robot.getMotor('left wheel motor')
    right_motor = robot.getMotor('right wheel motor')
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    print(timestep)
    
     
    #inicializuojami  8 infraraudonųjų spindulių sensoriai 
    prox_sensors = []
    
    for ind in range(8):
        sensor_name = 'ps' + str(ind)
        prox_sensors.append(robot.getDistanceSensor(sensor_name))
        prox_sensors[ind].enable(timestep)
    
    
    while robot.step(1750) != -1:
    
    
        #Spausdinamos iš sensorių gaunamos reikšmės
        for ind in range(8):
            print("sensor : {}, value:{}".format(ind,prox_sensors[ind].getValue()))
        
        
        #tikrinama ar roboto kairėje yra siena
        left_sensor = prox_sensors[5].getValue() >80
        
        right_sensor = prox_sensors[2].getValue() >80
        
        #tikrinama ar roboto priekyje yra siena
        front_sensor = prox_sensors[7].getValue() >80
        front2_sensor = prox_sensors[6].getValue() >80
        
        
        back_sensor = prox_sensors[4].getValue() >80
        
        left_speed = max_speed
        right_speed = max_speed
        
        
        
        if forward:
            forward =False
        else:
            if front_sensor:
                left_speed = max_speed
                right_speed = -max_speed
                counter=counter+1
            elif left_sensor:
                left_speed = max_speed
                right_speed = max_speed
            elif counter>0 and forward!=True:
                left_speed = -max_speed
                right_speed =max_speed
                counter=counter-1
                forward = True 
        
                  
                
        #nustatomi motorų greičiai 
        print(counter)   
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)       
   
    
    # Enter here exit cleanup code.

if __name__ == "__main__":
     
    # sukuriamas Robot objektas
    my_robot = Robot()  
    # paleidžiamas robotas
    run_robot(my_robot)  
    