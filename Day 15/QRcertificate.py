import qrcode
import uuid
from urllib.parse import quote_plus 
def Certificate_Url_QR():
    name = input("Enter name: ").strip()
    subject = input("Enter Subject: ").strip()
    unique_id = str(uuid.uuid4())
    safe_name = quote_plus(name)
    safe_subject = quote_plus(subject)
    certificate1 = (
        "file:///C:/LPU/Semister%204/Python%20Certificate/"
        "Penumalli%20Dindi%20Venkat-%20Python%20Certificate_%20PPA.pdf"
    )
    certificate2 = (
        "file:///C:/LPU/Semister%205/CSE%20322%20Automata/Certificate.pdf"
    )
    if name.lower() == "venkat":
        url = certificate1
        cert_type = "Certificate 1"
    else:
        url = certificate2
        cert_type = "Certificate 2"
    certificate_url = (
        f"{url}"
        f"?id={unique_id}"
        f"&name={safe_name}"
        f"&subject={safe_subject}"
    )
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(certificate_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    file_name = rf"C:\Wipro\Gitrepo\Python-Automotive-Batch9\Day 15\{safe_name}_certificate_qr.png"
    img.save(file_name)
    print("\n✅ QR Code generated successfully!")
    print("Candidate Name  :", name)
    print("Subject         :", subject)
    print("Unique ID       :", unique_id)
    print("Certificate Type:", cert_type)
    print("QR URL          :", certificate_url)
    print("Saved File      :", file_name)
Certificate_Url_QR()
