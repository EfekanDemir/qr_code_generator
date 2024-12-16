import qrcode

def create_qr_code(url, file_name):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")


    if not file_name.endswith(".png"):
        file_name += ".png"
    img.save(file_name)
    print(f"QR kod '{file_name}' olarak kaydedildi!")
    print(f"Bu QR kodu tarandığında '{url}' adresine yönlendirecek.")

if __name__ == "__main__":

    website_url = input("QR kodun yönlendireceği internet adresini yazın (örn: https://www.example.com): ")
    if not website_url.startswith("http://") and not website_url.startswith("https://"):
        website_url = "https://" + website_url


    file_name = input("QR kod görüntüsünü kaydetmek için dosyanın adını yazın (örn: qr_code): ")
    create_qr_code(website_url, file_name)
