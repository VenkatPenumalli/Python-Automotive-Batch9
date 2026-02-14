import qrcode
def generate_qr():
    with open(r"C:\Wipro\Gitrepo\Python-Automotive-Batch9\Day 15\qr.txt", "r") as file:
        data = file.read().strip()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(
        r"C:\Wipro\Gitrepo\Python-Automotive-Batch9\Day 15\student_details_qr.png"
    )
    print("QR Code generated successfully!")
    print("QR Data:\n", data)
generate_qr()
