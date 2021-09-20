from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:
time = 10
robotArm.grab()
for movement in range (time):
    
    robotArm.moveRight(); 

robotArm.drop()
 

time = 2
for movements in range (time):
    robotArm.moveLeft(); 
robotArm.grab()

time = 2
for movements in range (time):
    robotArm.moveRight();
robotArm.drop()    

time = 5
for movements in range (time):
    robotArm.moveLeft();
robotArm.grab()    

time = 5
for movements in range (time):
    robotArm.moveRight();
robotArm.drop()    

    
    
    


    











# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()