import wpilib
from commandbased import CommandBasedRobot

import subsystems
import oi
from commands.autonomous import AutonomousProgram


class Robot(CommandBasedRobot): 
    def robotInit(self):
        subsystems.init()
        self.autonomousProgram = AutonomousProgram()
        oi.init()
    def autonomousInit(self):
        self.autonomousProgram.start()
if __name__ == '__main__':
    wpilib.run(Robot)