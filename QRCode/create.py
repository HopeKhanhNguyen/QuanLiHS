import qrcode

def create_qr(data):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        msv = data.split("|")[1]
        img.save(f"./imgQrCode/{msv}.png")
        return f"./imgQrCode/{msv}.png"
    except: pass