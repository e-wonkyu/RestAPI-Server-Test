from flask import Flask, Response, request

from routes import accounts

app = Flask(__name__)

"""
    블루프린트 등록
"""
app.register_blueprint(accounts.account)


@app.route('/')
def index():
    resp = Response('{"test":"test"}',status=200,mimetype='application/json')
    return resp





"""
    Test 설정
"""


if __name__ == '__main__':
    app.run()



"""
    SSL 설정
"""

# @app.before_request
# def before_req():
#     if request.url.startswith('http://'):
#         url = request.url.replace('http://','https://',1)
#         code = 301
#         return redirect(url,code=code)
#
# if __name__ == '__main__':
#     ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
#     ssl_context.load_cert_chain(certfile='server.crt', keyfile='server.key')
#     app.run(host='0.0.0.0', port=443, ssl_context=ssl_context, debug=True)
#     app.run()
