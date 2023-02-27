import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://instagram.com/sahil_sachin?igshid=ZDdkNTZiNTM="
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("instagram.svg", scale = 8) 