from distutils.log import debug
from flask import Flask, render_template
from datetime import datetime
import os

# application init
app = Flask(__name__)

# insert variable

def get_current_time():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return current_time

def get_docker_logo():
    """
    Return a logo from static directory
    """
    img_dir = './static'
    img_path = os.listdir(img_dir)[0]
    return img_path

# routing
@app.route('/')
def index():
    t = get_current_time()
    d = get_docker_logo()
    return render_template(r'hi_docker.html', current_time = t, docker_logo = d)

# execute app
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 80)