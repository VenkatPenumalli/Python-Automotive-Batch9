import qrcode
def generate_qr():
    Project_Title = "\n PROJECT TITLE :: AUTOSAR TIMING AND PERFORMANCE TESTING WITH PYTON"
    Name = "\n STUDENT NAME :: Penumalli Dindi Venkat"
    Name2 = "\n STUDENT NAME :: Sannapaneni Sai Ram"
    Batch = "\n BATCH :: 25SUB4527_WiproNGA_AutomotiveTesting"
    data = f"{Project_Title} \n{Name} \n{Name2} \n{Batch}" 
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
        r"C:\Wipro\Gitrepo\Python-Automotive-Batch9\Capstone\student_details_QRuserinp.png"
    )
    print("QR Code generated successfully!")
    print("QR Data:\n", data)
generate_qr()