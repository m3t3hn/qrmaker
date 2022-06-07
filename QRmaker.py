import qrcode
qr = qrcode.QRCode(version=1,
error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=10,border=4)
qr.add_data(input("the data you want to add (link or whatever you want):"))
qr.make(fit=True)
img = qr.make_image(fill_color='black',back_color='white')
img.save("output.png")
print("output.png is saved in the current directory.")
