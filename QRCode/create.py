import qrcode, os

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
        img_path = os.path.join(os.getcwd(),  'imgQrCode', f"{msv}.png")
        path_dir = os.path.dirname(img_path)
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
        img.save(img_path)
        return img_path
    except: pass