import picamera
import time
from pathlib import Path

p = Path('/home') / 'pi' / 'Documents'/ 'repos'/ 'camAirQuality'/ 'data'/ 'raw'/ 'piImages'
p.mkdir(exist_ok=True)

#TODO
# only take a photo if its bright enough, or if not dark, maybe after sunset
# write data to folder if it exists

time_int = int(time.time())

image_name = 'image_'+ str(time_int) +'.jpg'

new_photo = open(p/image_name, 'wb')

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture(new_photo)
    
new_photo.close()