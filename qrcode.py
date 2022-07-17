import pyqrcode
import png
from pyqrcode import QRCode
str = "https://www.youtube.com/results?search_query=telusko+python"

qrcd = pyqrcode.create(str)

qrcd.svg("qrcd.svg", scale=10)