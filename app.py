from flask import *
import redis
app= Flask(__name__)
r= redis.Redis(host='localhost', port=6379, db=0)
@app.route('/', methods=['GET', 'POST'])
def aplicacion():
    
    #r.set('hello','world')
    #value= r.get('hello')
    #print (value)   #imprime en la consola
    #return (value)   #retorna en localhost
    #data = request.form.get('input_name', default_value)
    return ("<form method='GET' action='/search'><input type='text' name='producto'/><input type='submit' value='Submit'/></form>")

@app.route('/search', methods=['GET', 'POST'])
#http://127.0.0.1:5000/login?username=usuario&password=clave
def busqueda():
    producto= request.args.get('producto')
    value= r.get(producto)
    if value==None:
        print("hola")
        return("<h3>hola mundo</h3>")
    else:
        response = {"nombre producto":str(producto),
                    "precio producto":str(value)}
        return jsonify(response)
    #password = request.args.get('password')
    #return username
'''@app.route('/search/<producto>', methods=['GET'])
def get_producto(producto):
    value= r.get(producto)
    if value==None:
        print("hola")
        return("<h3>hola mundo</h3>")
    else:
        response = {"nombre producto":str(producto),
                    "precio producto":str(value)}
        return jsonify(response)'''
if __name__=="__main__":
    app.run()