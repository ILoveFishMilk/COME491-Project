import face_recognition
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/app', methods=['POST'])
def recognize():
    
    images = request.files.getlist('images')
    
    known_image = face_recognition.load_image_file(images[0])
    unknown_image = face_recognition.load_image_file(images[1])
    #known images should be pre encoded and stored in a database to reduce proccessing time
    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([known_encoding], unknown_encoding)

    return str(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)