"""
This is an example code taken from
http://sourceforge.net/apps/mediawiki/zbar/index.php?title=HOWTO:_Scan_images_using_the_API

This code takes the QR code as an input image and outputs the decoded message

"""
from sys import argv
import zbar
import Image

if len(argv) < 2: exit(1)

# Create a reader
scanner = zbar.ImageScanner()

# Configure the reader
scanner.parse_config('enable')

# obtain image data
pil = Image.open(argv[1]).convert('L')
width, height = pil.size
raw = pil.tostring()

# wrap image data
image = zbar.Image(width,height,'Y800',raw)

# scan the image for barcodes
scanner.scan(image)

# Extract results
for symbol in image:
	#do something useful with results
	print 'Decoded: ', symbol.type, 'symbol', '"%s"' % symbol.data

# clean up
del(image)
