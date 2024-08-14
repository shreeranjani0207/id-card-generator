from os import name
from re import template
from flask import Flask, render_template, request
import qrcode
import io
import base64
from PIL import Image

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/', methods=["POST"])
def getdata():
    name = request.form['name']
    fr = request.form['vali1']
    to = request.form['vali2']
    dob = request.form['dob']
    branch = request.form['branch']
    gender = request.form['gender']
    address = request.form['address']
    email = request.form['email']
    blood = request.form['blood']
    mob = request.form['mob']
    id = request.form['id']

    info = f"\nName of Student  : {name} \nGender : {gender} \nAddress = {address}\nEmail : {email}\nMobile No : {mob} \nDate Of Birth : {dob} \nBranch : {branch} \nReg ID : {id} \nBlood group : {blood} "

    img = qrcode.make(info)
    img.save("qr_image.jpeg")
    im = Image.open("qr_image.jpeg")
    data = io.BytesIO()
    im.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())

    return render_template('main.html', name=name, fr=fr, to=to, dob=dob, branch=branch, id=id, img_data = encoded_img_data.decode("utf-8"))


if __name__ == "__main__":
    app.run(debug=True)
