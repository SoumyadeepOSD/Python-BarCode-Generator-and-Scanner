import pyqrcode
import png
from pyqrcode import QRCode

link = 'www.youtube.com'
url = pyqrcode.create(link)
url.png('barcode.png', scale=6)
