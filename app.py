import json
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

#H-1
@app.route('/users', methods=['GET'])
def get_users():
 return jsonify({'payload':'success'})
#H-2
@app.route('/user', methods=['POST'])
def post_user():
 return jsonify({'payload':'success'})
#H-3
@app.route('/user', methods=['DELETE'])
def delete_user():
 return jsonify({'payload':'success'})
#H-4
@app.route('/user', methods=['PUT'])
def put_user():
 return jsonify({'payload':'success'})
#H-5
@app.route('/api/v1/users', methods=['GET'])
def get_users_v1():
 return jsonify({'payload':[]})
#H-6
@app.route('/api/v1/user', methods=['POST'])
def post_user_v1():
  email = request.args.get('email')
  name = request.args.get('name')
  return jsonify({
            'payload': {
                'email':email,
                'name':name,
            }
        })
#H-7
@app.route('/api/v1/user/add', methods=['POST'])
def post_user_add_v1():
  email = request.form.get('email')
  name = request.form.get('name')
  id = request.form.get('id')
  return jsonify({
            'payload': {
                'email':email,
                'name':name,
                'id': id,
            }
        })
#H-8
@app.route('/api/v1/user/create', methods=['POST'])
def create_user_v1():
  data = request.json
  email = data.get('email')
  name = data.get('name')
  id = data.get('id')
  return jsonify({
            'payload': {
                'email':email,
                'name':name,
                'id': id,
            }
        })



if __name__ == "__main__":
    app.run(debug=True)