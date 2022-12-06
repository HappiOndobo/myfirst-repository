import pyqrcode
from pyqrcode import QRCode

link = "https://www.iaicameroun.com"

output = pyqrcode.create(link)

output.svg("mypage.svg", scale=6)


#coded by @happiondobo