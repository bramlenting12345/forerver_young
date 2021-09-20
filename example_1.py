from RobotArm import RobotArm

robotArm = RobotArm('exercise 1')

# Jouw python instructies zet je vanaf hier:
time = 1
for movement in range (time):
    robotArm.moveRight();
robotArm.grab()

time = 1 
for movements in range (time):
    robotArm.moveLeft();
robotArm.drop()    








# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()