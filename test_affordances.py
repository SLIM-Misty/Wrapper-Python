import mistyPy

robot  = mistyPy.Robot("10.10.0.7")
robot.changeLED(200,200,0)
robot.changeImage("e_EcstacyStarryEyed.jpg")



#Test Battery: 
result = robot.battery()
# Test Notes: returns chargePercent but no value.




#robot.printImageList()
print("result: {}".format(result))
print("Script done.")

def test_head():
    # Test head movement
    for i in range(-5,6):
        robot.moveHead(0,i,0) 
        robot.moveHead(0,0,i)
        robot.moveHead(i,0,0)



def test_led(max_color_val, step=step):
    # Test LED:
    step = 3
    for i in range(256,step=step ): # Red
        robot.changeLED(i,0,0)

    for i in range(256,step=step): # Green
        robot.changeLED(0,i,0)

    for i in range(256, step=step): #Blue
        robot.changeLED(0,0,i)

    for i in range(256,step=step ): # 
        robot.changeLED(i,i,0)

    for i in range(256,step=step): # 
        robot.changeLED(0,i,i)

    for i in range(256, step=step): #Blue
        robot.changeLED(i,0,i)

    for i in range(256, step=step): #Blue
        robot.changeLED(i,i,i)