from aiohttp import web 
import json
from business.create_pdf import create_pdf

class api_routes():

    @classmethod
    async def create_file_pdf(seft, request):
        try:
            name = request.query['nombre']
            last_name = request.query['apellido']
            age = request.query['edad']
            phone = request.query['telefono']
            email = request.query['correo']
            
            number_return =  create_pdf.create_file_pdf(name, last_name, age, phone, email)
            response_obj = {'status':True, 'code': number_return}
            
            return web.Response(text = json.dumps(response_obj), status= 200)
        except Exception as e:
            response_obj = {'status':'failed','message':str(e)}
            return web.Response(text= json.dumps(response_obj), status = 500)
            
    @classmethod
    async def get_file_pdf(seft, request):
        try:
            id = request.match_info.get('code', "Anonymous")
            code_base64 =  create_pdf.get_file_pdf(id)
            print(code_base64)
            response_obj = {'status':True, 'document_b64': str(code_base64).replace("b'", "").replace("'", "")}
            print(response_obj)
            return web.Response(text=json.dumps(response_obj), status = 200)
        except Exception as e:
            response_obj = {"status":"failed","message":str(e)}
            return web.Response(text= json.dumps(response_obj), status = 500)
        
        
    