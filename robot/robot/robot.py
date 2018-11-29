#!/usr/bin/env python3
'''
    This is a demo program showing how to use Mecanum control with the
    RobotDrive class.
'''

import wpilib
import commandbased
import ctre
#main robot

class MyRobot(commandbased.CommandBasedRobot):
    def robotInit(self):
        self.motors={}
        self.motors['leftMotor']=ctre.WPI_TalonSRX(0)
        self.motors['rightMotor']=ctre.WPI_TalonSRX(1)
    def testInit(self):
        print("TESTING TESTING 123")
        while self.isTest():       
            print("VROOM VROOM I'M MOVING FAST")
            self.motors['leftMotor'].set(0.06)
            self.motors['rightMotor'].set(0.05)
        print("I am now moving at a reasonable speed")
#code to help run the robot

#import sys       
def exit(retval):
    pass
#    sys.exit(retval)

if __name__ == '__main__':
    try:
        print(wpilib._impl.main.exit)
    except:
        wpilib._impl.main.exit = exit
    wpilib.run(MyRobot,physics_enabled=True)