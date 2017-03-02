import wpilib
from wpilib.command.subsystem import Subsystem

from commands.followjoystick import FollowJoystick
import robotmap

class drivetrain:
  def __init__(self)
     super().__init__()
    self.motor0 = wpilib.Spark(robotMap.DRIVE0_PORT)
    self.motor1 = wpilib.Spark(robotMap.DRIVE1_PORT)
    self.motor2 = wpilib.Spark(robotMap.DRIVE2_PORT)
    self.motor3 = wpilib.Spark(robotMap.DRIVE3_PORT)
