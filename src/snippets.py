from vex import *

# https://api.vex.com/v5/home/python/


controller_1 = Controller(PRIMARY)

# Robot configuration code
# Add, remove, or copy Motors as needed
# Be sure to change any ports as necessary
claw_motor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
arm_motor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)

left_motor1 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)  # RATIO_6_1 = blue cartridge;
left_motor2 = Motor(Ports.PORT11, GearSetting.RATIO_6_1, False) # use 18_1 for green and 
right_motor1 = Motor(Ports.PORT10, GearSetting.RATIO_6_1, True) # 36_1 for red
right_motor2 = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)


# Drivetrain configuration
inertialSens = Inertial(Ports.PORT15)
lft_motor_group = MotorGroup(left_motor1, left_motor2)
rgt_motor_group = MotorGroup(right_motor1, right_motor2)
drive_train = SmartDrive(lft_motor_group, rgt_motor_group, inertialSens)



##### ARCADE DRIVE #####
# if you changed or added any motors above, update this code accordingly
lft_motor_group.set_velocity((controller_1.axis3.position() + controller_1.axis1.position()), PERCENT)
rgt_motor_group.set_velocity((controller_1.axis3.position() - controller_1.axis1.position()), PERCENT)
lft_motor_group.spin(FORWARD)
rgt_motor_group.spin(FORWARD)



##### Optical Sensor #####
optical_sensor = Optical(Ports.PORT10)

# returns True if sensor sees anythine EXCEPT opponent alliance color
# returns False if sensor sees opponent alliance color
# opponent color must be passed in as a paremeter in format Color.<color_name> (see documentation)
def color_sort(opponent_color):
  if not optical_sensor.color() == opponent_color:
    return True
  else:
    return False

# to use above, call the function in your button.pressing() block:
# for instance, to spin an intake one direction for your team color 
# and the opposite direction for opponent's color
if controller1.buttonA.pressing():
  if color_sort(Color.RED):
    selected_motor.spin(FORWARD)
  else:
    selected_motor.spin(REVERSE)

