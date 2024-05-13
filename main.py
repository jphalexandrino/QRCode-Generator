import segno

text = input("Coloque o texto que você gostaria que se tornasse um QR Code: ")

qrcode = segno.make_qr(text)
qrcode.save(
    "qrcode.png",
    scale=5,
)
