from flask import Flask, request, send_file
import pytesseract
from PIL import Image
import io
from gtts import gTTS

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    image_data = request.data
    image = Image.open(io.BytesIO(image_data))
    
    # استخراج النص من الصورة
    text = pytesseract.image_to_string(image, lang='ara+eng')
    print("Extracted Text:", text)

    # تحويل النص إلى صوت
    tts = gTTS(text=text, lang='ar')
    tts.save("output.mp3")

    return send_file("output.mp3", mimetype="audio/mpeg")

if __name__ == '__main__':
    app.run()
