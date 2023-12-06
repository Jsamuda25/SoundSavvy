from flask import Flask, after_this_request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    return {'message': 'Hello, World!'}

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)