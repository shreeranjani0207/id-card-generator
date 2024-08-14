import qrcode
import io
import base64
from PIL import Image
from flask import Flask , render_template


app = Flask(__name__)
@app.route('/')
def trial():
    img = qrcode.make("info")
    img.save("qr_image.jpeg")
    im = Image.open("qr_image.jpeg")
    data = io.BytesIO()
    im.save(data , "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())


    return render_template('trial.html' , img_data = encoded_img_data.decode("utf-8") )

if __name__ == "__main__":
    app.run(debug= True)





