import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
import qrcode
from segno import helpers

# CREATE QR CODE 1
qr = pyqrcode.create(" Hi, My name is Dainius.\n"
                     " This is my first QR code with PYTHON :) \n I hope you like it :) \n"
                     " More about me: https://dainius.hostin.lt")
qr.png("E:\\DARBAI\\Phyton\\Mokymai\\QR\\text-QR.png", scale=9)

# CREATE QR CODE 2
# img = qrcode.make(" Hi, this is my WEB site: \n https://dainius.hostin.lt")
img = qrcode.make('https://dainius.hostin.lt')
img.save("E:\\DARBAI\\Phyton\\Mokymai\\QR\\url-QR.png")

# CREATE QR CODE 3
# qrcode = helpers.make_vcard(name='Dainius',
#                             displayname='Karpavičius',
#                             email='dainaklis@gmail.com',
#                             phone='+370 687 23733')

qrcode = helpers.make_vcard(name='Dainius',
                            displayname='Dainius Karpavičius',
                            org='SBA Urban',
                            title='Security',
                            phone='+370 687 23733',
                            email='dainaklis@gmail.com',
                            url='https://dainius.hostin.lt',
                            )
qrcode.designator
'5-L'

qrcode.save('E:\\DARBAI\\Phyton\\Mokymai\\QR\\vcard-QR.svg', scale=6)
# JEI NORIU PNG
qrcode.save('E:\\DARBAI\\Phyton\\Mokymai\\QR\\vcard-QR.png', scale=6)

# CREATE QR CODE 4 --------------------------------------------------------
qrcode2 = helpers.make_mecard(name='Doe,John', email='me@example.org', phone='+1234567')
qrcode2.designator
'3-L'

# qrcode2 = helpers.make_mecard(name='Doe,John',
#                              email=('me@example.org', 'another@example.org'),
#                              url=['http://www.example.org', 'https://example.org/~joe'])
qrcode2.save('E:\\DARBAI\\Phyton\\Mokymai\\QR\\mecard-QR.svg', scale=4)



# READ QR CODE
d = decode(Image.open("E:\\DARBAI\\Phyton\\Mokymai\\QR\\text-QR.png"))
print(d[0].data.decode("ascii"))
