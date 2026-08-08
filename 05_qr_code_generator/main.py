import qrcode

filepath = 'qrcode.png'
url = input("Enter the input you want turned into a qrcode: ").strip()

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(filepath)

print("QR code generated successfully!")

