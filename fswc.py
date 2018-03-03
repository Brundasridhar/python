#import libraries
import time 
import os 

while True: # do forever
          
    import time
        a=1
        b=1
        while (a<5):
            os.system('fswebcam -r 1280X720 -S 3 --jpeg 100 -- no banner --swapchannels RB --save/home/cs2017a113/1.jpg') # uses Fswebcam to take picture
            time.sleep(10) # this line creates a 15 second delay before repeating the loop
            print("hello time",str(b))
            a=a+1
            b=b+1

