#This is an example of the "Not a chicken" simplified gesture.

#THIS GESTURE WILL NOT WORK FOR YOU UNLESS YOUR SERVO SERVICES MATCH THE SAME NAMES AS MINE! That or your change the names of my setup to match yours. :9 

###############################################################################
sleep(2) #2second buffer so that the gesture starts 2 seconds after you execute it. Can be removed. 

RightArmBicep.moveTo(150)
RightArmRotate.moveTo(90)
RightArmShoulder.moveTo(95)
RightArmOmoplate.moveTo(15)
sleep(0.5)
mouth.audioFile.play('C:\MRL\CustomMovement\Audio\ThatIsNOTaChicken.mp3')  #This line will pull an error if you don't have a matching soundfile "ThatIsNOTaChicken.mp3" in a folder you have it directed it to.
sleep(0.7)

RightHandThumb.moveTo(180)
RightHandIndex.moveTo(0)
RightHandMiddle.moveTo(180)
RightHandRing.moveTo(180)
RightHandPinky.moveTo(180)
RightHandWrist.moveTo(180)
sleep(1.9)

RightArmBicep.moveTo(70)
RightArmShoulder.moveTo(75)
sleep(0.5)

RightArmBicep.moveTo(130)
sleep(1.8)

########END OF NOT A CHICKEN / RETURN TO REST / RESET SPEEDS#############
RightArmBicep.moveTo(5)
RightArmRotate.moveTo(90)
RightArmShoulder.moveTo(30)
RightArmOmoplate.moveTo(5)
RightHandWrist.moveTo(180)
RightHandThumb.moveTo(0)
RightHandIndex.moveTo(0)
RightHandMiddle.moveTo(0)
RightHandRing.moveTo(0)
RightHandPinky.moveTo(0)
