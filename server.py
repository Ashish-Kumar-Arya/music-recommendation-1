from flask import Flask,request,jsonify
import json
import pickle

app = Flask(__name__)

@app.route('/get_songs', methods=['GET'])
def get_songs():
    response = jsonify(drop)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

songs = pickle.load(open('songs.pkl','rb'))
songs_list = songs['song'].values
drop = []
for i in songs_list:
    drop.append(i)

if __name__ == "__main__":
    app.run()