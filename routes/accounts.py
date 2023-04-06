from flask import Blueprint, request, make_response, Response

account = Blueprint("accounts",__name__,url_prefix='/account')


def methodForm():
   method = request.method
   try:
      if method == 'POST':
         data = request.json
         param1 = data['param']
      elif method == 'GET':
         param1 = request.args.get('param', '')
      elif method == 'PUT':
         3
      elif method == 'DELETE':
         4
      else :
         5
   except Exception as e:
      print(e)


@account.route('/register',methods=['GET','POST','PUT','GET'])
def register():
   method = request.method
   try:
      if method == 'POST':
         1
      elif method == 'GET':
        2
      elif method == 'PUT':
         3
      elif method == 'DELETE':
         4
      else :
         5
   except Exception as e:
      print(e)
   return 'register'
