import qrcode


img = qrcode.make("https://github.com/GonnaFlyMethod/QRCode-generator-web-app/blob/main/README.md")
img.save("test_file.png")