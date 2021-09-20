from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

move = 7 # white blokje
for movement in range (move):
    robotArm.moveRight();
robotArm.grab()   

move = 1 #white blokje
for movement in range (move):
    robotArm.moveRight();
robotArm.drop()


move = 2 # red blokje 
for movement in range (move):
    robotArm.moveLeft();
robotArm.grab()

move = 1 # red blokje 
for movement in range (move):
    robotArm.moveRight();
robotArm.drop()    
 

move = 2  # blue blokje 
for movement in range (move):
    robotArm.moveLeft();
robotArm.grab()  

move = 1 # blue blokje 
for movement in range (move):
    robotArm.moveRight();
robotArm.drop()    

move = 2  # green blokje 
for movement in range (move):
    robotArm.moveLeft();
robotArm.grab()  

move = 1 # green blokje 
for movement in range (move):
    robotArm.moveRight();
robotArm.drop()    

move = 2  # green blokje 
for movement in range (move):
    robotArm.moveLeft();
robotArm.grab()  

move = 1 # green blokje 
for movement in range (move):
    robotArm.moveRight();
robotArm.drop()    

move = 2  # white blokje 
for movement in range (move):
    robotArm.moveLeft();
robotArm.grab()  

move = 1 # white  blokje 
for movement in range (move):
    robotArm.moveRight();
robotArm.drop()    

move = 2  # blue blokje 
for movement in range (move):
    robotArm.moveLeft();
robotArm.grab()  

move = 1 # blue blokje 
for movement in range (move):
    robotArm.moveRight();
robotArm.drop()  

move = 2  # red blokje 
for movement in range (move):
    robotArm.moveLeft();
robotArm.grab()  

move = 1 # red  blokje 
for movement in range (move):
    robotArm.moveRight();
robotArm.drop()    







# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()