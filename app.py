from flask import Flask, request, render_template,send_from_directory
app = Flask(__name__)
import os
# from uuid import uuid4

# from model import find_img_type
from model import sign
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html', value='hi')
    if request.method == 'POST':
        target = os.path.join(APP_ROOT, 'static\\images')
        print(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        print(filename)
        destination = os.path.join(target,filename)
        print(destination)
        file.save(destination)
        # print(request.files)
        # if 'file' not in request.files:
        #   print('file not uploaded')
        #   return
        file = request.files['file']
        name=sign(file).capitalize()
        print(type(name))
        # category, flower_name = get_flower_name(image_bytes=image)
        # get_flower_name(image_bytes=image)
        # tensor = get_tensor(image_bytes=image)
        # print(get_tensor(image_bytes=image))
        # signdata={'sign_name':name.category}
        return render_template('result.html', signs=name, filename=filename)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0' ,port=8008)