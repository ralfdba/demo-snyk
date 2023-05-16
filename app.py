from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hola', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		data = {"data": "hola curso"}
		return jsonify(data)


if __name__ == '__main__':
	app.run(debug=True)
