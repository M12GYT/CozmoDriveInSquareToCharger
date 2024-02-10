import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Hello World").wait_for_completed()
    
def cozmo_program(robot: cozmo.robot.Robot):
    # Turn 90 degrees to the left.
    # Note: To turn to the right, just use a negative number.
    robot.turn_in_place(degrees(90)).wait_for_completed()    



def cozmo_program(robot: cozmo.robot.Robot):
    robot.drive_straight(distance_mm(330), speed_mmps(99)).wait_for_completed()
    robot.say_text("Hello coderdojo People").wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.drive_straight(distance_mm(160), speed_mmps(99)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.drive_straight(distance_mm(160), speed_mmps(99)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.drive_straight(distance_mm(158), speed_mmps(99)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.drive_straight(distance_mm(-180), speed_mmps(99)).wait_for_completed()
    robot.play_anim(name="anim_gotosleep_getin_01").wait_for_completed()
    robot.play_anim(name="anim_gotosleep_sleeploop_01").wait_for_completed()   
    
cozmo.run_program(cozmo_program)
  