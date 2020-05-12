from flask import Flask, jsonify, request, redirect, url_for, flash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, jwt_refresh_token_required, create_refresh_token
from werkzeug.utils import secure_filename
import datetime
import os

UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JWT_SECRET_KEY'] = 'asdf'
jwt = JWTManager(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    expires = datetime.timedelta(days=365)
    ret = {
        'access_token': create_access_token(identity=username, expires_delta=expires)
    }
    return jsonify(ret), 200

@app.route('/api/auth_test', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/api/upload', methods=['GET', 'POST'])
@jwt_required
def upload_file():
    if request.method == 'POST':
        file_upload = request.files['file']
        if file_upload:
            filename = secure_filename(file_upload.filename)
            if allowed_file(filename):
                file_upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return {'status':'good'}
            else: return jsonify({"msg": "not allowed file type"}), 402

if __name__ == '__main__':
    app.run(debug=True)