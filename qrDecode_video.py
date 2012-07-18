"""
This is an example code taken from
http://sourceforge.net/apps/mediawiki/zbar/index.php?title=HOWTO:_Scan_video_using_the_Processor

This code uses the laptop camera to capture the video and give real-time decoding of the image. The response time is quite fast.

Refer to the webpage below for details on image quality
http://sourceforge.net/apps/mediawiki/zbar/index.php?title=Troubleshooting#Size.2FResolution

"""
from sys import argv
import zbar

# create a processor
proc = zbar.Processor()

# configure the Processor
proc.parse_config('enable')

# initialise the processor
device = '/dev/video0'
if len(argv) > 1:
	device = argv[1]
proc.init(device)

# set up a callback
def my_handler(proc,image,closure):
	#extract results
	for symbol in image:
		if not symbol.count:
			#do somthing useful with results
			print 'Decoded:', symbol.type, 'symbol', '"%s"' % symbol.data

proc.set_data_handler(my_handler)

#enable the preview window
proc.visible = True

# initiate scanning
proc.active = True

try:
	proc.user_wait()
except zbar.WindowClosed:
	pass

