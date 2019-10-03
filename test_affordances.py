import mistyPy

robot  = mistyPy.Robot("10.10.0.7")
robot.changeLED(200,200,0)
robot.changeImage("e_EcstacyStarryEyed.jpg")

def test_head():
    print("Testing Head.")
    # Test head movement
    for i in range(40,-40):
        robot.moveHead(0,i,0) 
        robot.moveHead(0,0,i)
        robot.moveHead(i,0,0)


def test_led(max_color_val, step=10):
    # Test LED:
    print("led test 1")
    for i in range(256): # Red
        robot.changeLED(i,0,0)

    print("led test 2")
    for i in range(256): # Green
        robot.changeLED(0,i,0)

    print("led test 3")   
    for i in range(256): #Blue
        robot.changeLED(0,0,i)

    print("led test 4")
    for i in range(256): # yellow
        robot.changeLED(i,i,0)

    print("led test 5")
    for i in range(256): #  blue
        robot.changeLED(0,i,i)

    print("led test 6")
    for i in range(256): #Pink
        robot.changeLED(i,0,i)

    print("led test 7")
    for i in range(256): #Blue
        robot.changeLED(i,i,i)


# test_head()
# test_led(256,5)

# robot.printImageList()
# robot.driveTime(50,0,2000)


# image_name = "result"
# robot.changeImage(image_name,timeout=5)
print("audio_populated")
robot.populateAudio()
robot.printAudioList()

# for audio_file in audio_list():
#     robot.playAudio(audio_file)
# robot.battery()
# left_track_speed = 10
# right_track_speed = 10
# robot.driveTrack(left_track_speed, right_track_speed)
# message="Message sent to backpack"
# robot.sendBackpack(message)
robot.populateImages()

# robot.populateLearnedFaces()
robot.printImageList()
# robot.getImageList()
# robot.printAudioList()
# robot.getAudioList()
# robot.printSubscriptionList()
# robot.startFaceRecognition()
# robot.stopFaceRecognition()
# robot.printLearnedFaces()

# robot.clearLearnedFaces()
name = "bob"
# robot.learnFace(name)
faces = robot.getLearnedFaces()
# for face in faces:
print(faces)

print("Script done.")