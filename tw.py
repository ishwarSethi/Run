from flask import flask, request
from twilio import twiml


app = Flask(__name__)


app,route('/sms' , methods=['POST'])
def sms():
	number = request.from['From']
	message_body = request.from['Body']
	
	resp = twiml.Response()
	resp.message('Hello {}, you said:  {}'.format(number, message_body))
	return str(resp)
	
if __name__ == '__main__':
	app.run()
	
