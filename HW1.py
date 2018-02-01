from flask import Flask ,request
from flask_restful import Resource , Api,reqparse
import json ,time
from datetime import datetime, date

today = date.today()

app=Flask (__name__)
api=Api(app)
parser =reqparse.RequestParser()
parser.add_argument('birthday')

class Hello(Resource):
	def get(self):
		args=parser.parse_args()
		name=args['birthday']
		d,m,y=name.split('-')
		age=today.year-int(y)
		return{"Birthday":name,"age":str(age)}

api.add_resource(Hello,'/timestamp')

if __name__ =='__main__':
	app.run(host='0.0.0.0',port=5500)
