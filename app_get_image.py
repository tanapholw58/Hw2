import os
from flask import Flask, render_template, request, make_response
from flask_restful import Resource , Api,reqparse
import json

app = Flask(__name__)
api = Api(app)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class img(Resource):
	def get(self):
		return make_response(render_template("img_upload.html"))


class upload(Resource):
	def post(self):
	    target = os.path.join(APP_ROOT, 'images/')
	    print(target)

	    if not os.path.isdir(target):
		os.mkdir(target)

	    for file in request.files.getlist("file"):
		print(file)
		filename = file.filename
		destination = "/".join([target, filename])
		print(destination)
		file.save(destination)
	    return {"code":"200","desc":"upload success"}

api.add_resource(img,'/')
api.add_resource(upload,'/upload')


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5555)
