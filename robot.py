import wpilib

import subsystems
import oi
#from commands.autonomous import AutonomousProgram


class Robot(wpilib.IterativeRobot): 
   
    def robotInit(self):
        self.drivetrain = subsytems.Drivetrain()
        self.oi = OI()
        self.autonomousCommand = commands.Auto()
        
    def autonomousInit(self):
        try:
            self.autonomousProgram.start()
        except NameError:
            print("Autonomous command not set")
        
    def teleopInit(self):
        try:
            self.autonomousProgram.cancel()
        except NameError:
            print("Autonomous command not set")
            
if __name__ == '__main__':
    wpilib.run(Robot)
