from flask import Flask, render_template, Response, jsonify,request
from main import Stream
import os

app = Flask(__name__,static_url_path='/static')
stream = Stream()

def get_video_files():
    video_files = []
    video_dir = 'D:\courses\web\static\\videos'  
    for filename in os.listdir(video_dir):
        if filename.endswith('.mp4'):
            video_files.append(filename)
    return video_files


@app.route('/')
def index():
    video_files = get_video_files()
    return render_template('index.html', video_files=video_files)

@app.route('/video')
def video():
    stream_source = request.args.get('source', 'webcam')  
    if stream_source == 'webcam':
        return Response(stream.processing(), mimetype='multipart/x-mixed-replace; boundary=frame')
    elif stream_source == 'rtsp':
        rtsp_url = request.args.get('rtsp_url')
        return Response(stream.processing(rtsp_url), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return "Invalid stream source", 400

@app.route('/refresh-video-list')
def refresh_video_list():
    video_files = get_video_files()
    return jsonify(video_files)

if __name__ == '__main__':
    app.run(debug=True)
