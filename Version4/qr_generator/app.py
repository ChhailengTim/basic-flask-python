import qrcode

def generate_qrcode(text, image_number):

    qr = qrcode.QRCode(
        version =1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save(f"qrimg_{image_number}.png")

image_number = 1    

while True:
    user_input = input("Enter the text or URL you want to generate a QR code for: ")

    if user_input.lower() == "exit":
        break

    generate_qrcode(user_input, image_number)

    image_number += 1