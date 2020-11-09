from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from Personas import Persona
from Canciones import Cancion
from Comentarios import Comentario
from Canciones import PlayList
from Canciones import Solicitud

app = Flask(__name__)
CORS(app)

Usuarios = []
Usuarios.append(Persona('Usuario','Maestro','admin','admin',"administrador",0))
Usuarios.append(Persona('O','D','oscar','oscar',"cliente",1))
cont_user=2

Canciones = []
Canciones.append(Cancion(0,"Aries ft. Peter Hook & Georgia (Episode Three)","Gorillaz","Song Machine",2020,"https://upload.wikimedia.org/wikipedia/en/7/7a/Aries_single_cover.jpg","https://open.spotify.com/embed/track/25Gp0MpGdvrs4hL1u4L2TF","https://www.youtube.com/embed/PKXloFW_ZCA"))
Canciones.append(Cancion(1,"What I've Done","Linkin Park","Minutes to Midnight",2007,"https://upload.wikimedia.org/wikipedia/en/9/94/WhatI%27veDoneCover.jpg","https://open.spotify.com/embed/track/18lR4BzEs7e3qzc0KVkTpU","https://www.youtube.com/embed/8sgycukafqQ"))
Canciones.append(Cancion(2,"Strange Days","Three Days Grace","Outsider",2020,"https://i.ytimg.com/vi/A-_JrT20LiI/hqdefault.jpg","https://open.spotify.com/embed/track/5drGPNM0Uyl44tQfmmM2eW","https://www.youtube.com/embed/FMfboNTd_JA"))
Canciones.append(Cancion(3,"The World","Nightmare","Death Note",2007,"https://i.blogs.es/ed157d/230317-deathnote/450_1000.jpg","https://open.spotify.com/embed/track/1g0SlTCGN9j3OicWHfSKEn","https://www.youtube.com/embed/RvIx-SJvlNY"))
Canciones.append(Cancion(4,"Thrift Shop","Macklemore","Single",2012,"https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRzhRk0dGktXbRZVOdWISlkVJmMVACJ8T2l_Q&usqp=CAU","https://open.spotify.com/embed/track/1CmUZGtH29Kx36C1Hleqlz","https://www.youtube.com/embed/QK8mJJJvaes"))
cont_c=5

Comentarios = []
Comentarios.append(Comentario(0,0,";v","admin"))
Comentarios.append(Comentario(1,1,"Esta en Todo","admin"))
Comentarios.append(Comentario(2,2,"Me llega","O"))
Comentarios.append(Comentario(3,1,"YEAHHHH!!!","admin"))
Comentarios.append(Comentario(4,0,"Probando","admin"))
cont_comment=5

Individuales = []
Individuales.append(PlayList(0,1))
Individuales.append(PlayList(0,2))
Individuales.append(PlayList(1,0))
    
Solicitudes = []    
Solicitudes.append(Solicitud("Pokemon Theme","Jason Paige","Pokemon",1999,"https://ychef.files.bbci.co.uk/976x549/p08n74r9.jpg","https://open.spotify.com/embed/track/3OIHgTyQdiAGMmpjQaNxp3","https://www.youtube.com/embed/rg6CiPI6h2g"))
Solicitudes.append(Solicitud("Fat Lip","Sum 41","All The Good Shit",2001,"https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Sum41fatlip.jpg/220px-Sum41fatlip.jpg","https://open.spotify.com/embed/track/4KacUpvbA3Mfo05gttTjhN","https://www.youtube.com/embed/CMX2lPum_pg"))
Solicitudes.append(Solicitud("Through the Fire and Flames","DragonForce","Inhuman Rampage",2005,"https://upload.wikimedia.org/wikipedia/en/f/f6/Through_the_Fire_and_Flames_Cover_Art.jpg","https://open.spotify.com/embed/track/2eB7JqIY4hTTSz31h6bjwR","https://www.youtube.com/embed/0jgrCKhxE1s"))
Solicitudes.append(Solicitud("Chop Suey","System of a Down","Toxicity",2001,"https://images-na.ssl-images-amazon.com/images/I/31AH29QJKKL.jpg","https://open.spotify.com/embed/track/2DlHlPMa4M17kufBvI2lEN","https://www.youtube.com/embed/CSvFpBOe8eY"))
Solicitudes.append(Solicitud("El Poder Nuestro Es","Adrian Barba","Dragon Ball Z(Opening 2)",1993,"https://i1.sndcdn.com/artworks-000097674453-cmp9k1-t500x500.jpg","https://open.spotify.com/embed/track/2QlQq5csLYw2nrKf1MNfOu","https://www.youtube.com/embed/eaGh5e5Y4C4"))

@app.route('/', methods=['GET'])
def rutaInicial():
    print("Ruta Inicial")
    return("Ruta Inicial")

@app.route('/Login', methods=['POST'])
def Login():
    global Usuarios
    username = request.json['usuario']
    password = request.json['password']
    for usuario in Usuarios:
        if usuario.getUsuario() == username and usuario.getPassword()==password:
            Dato = {
                'message': 'Success',
                'usuario': usuario.getUsuario(),
                'tipo': usuario.getTipo(),
                'numero': usuario.getNumero()
                }
            break
        else:
            Dato = {
                'message': 'Failure',
                'usuario': ''
            }
    respuesta = jsonify(Dato)
    return(respuesta)        

@app.route('/Recuperar', methods=['POST'])
def Recuperar():
    global Usuarios
    username = request.json['usuario']
    for usuario in Usuarios:
        if usuario.getUsuario() == username:
            Dato = {
                'message': 'Success',
                'password': usuario.getPassword()
                }
            break
        else:
            Dato = {
                'message': 'Failure',
                'password': ''
            }
    respuesta = jsonify(Dato)
    return(respuesta)        

@app.route('/Personas', methods=['GET'])
def ObtenerUsuarios():
    global Usuarios
    Datos = []
    for usuario in Usuarios:
        Dato = {'name': usuario.getNombre(), 
        'lastname': usuario.getApellido(),
        'username': usuario.getUsuario(),
        'password': usuario.getPassword(),
        'tipo': usuario.getTipo(),
        'numero': usuario.getNumero()
        }
        Datos.append(Dato)
    respuesta = jsonify(Datos)    
    return(respuesta)

@app.route('/Canciones', methods=['GET'])
def ObtenerCanciones():
    global Canciones
    Datos = []
    for usuario in Canciones:
        Dato = {'id': usuario.getId(),
        'nombre': usuario.getNombre(), 
        'artista': usuario.getArtista(),
        'album': usuario.getAlbum(),
        'fecha': usuario.getFecha(),
        'imagen': usuario.getImagen(),
        'spotify': usuario.getSpotify(),
        'youtube': usuario.getYoutube()
        }
        Datos.append(Dato)
    respuesta = jsonify(Datos)    
    return(respuesta)    

@app.route('/Comentarios/<string:id>', methods=['GET'])
def ObtenerComentarios(id):
    global Comentarios
    n = int(id)
    Datos = []
    for usuario in Comentarios:
        if usuario.getId() == n:
            Dato = {
                'username':usuario.getUsuario(),
                'comentario':usuario.getComentario(),
                'No': usuario.getNo()
            }
            Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)         

@app.route('/PlayList/<string:numero>', methods=['GET'])
def ObtenerPlayList(numero):
    global Canciones
    global Individuales
    n = int(numero)
    Datos = []
    for usuario in Individuales:
        if n == usuario.getUsername():
            for cancion in Canciones:
                if usuario.getId() == cancion.getId():
                    Dato = {'id': cancion.getId(),
                    'nombre': cancion.getNombre(), 
                    'artista': cancion.getArtista(),
                    'album': cancion.getAlbum(),
                    'fecha': cancion.getFecha(),
                    'imagen': cancion.getImagen(),
                    'spotify': cancion.getSpotify(),
                    'youtube': cancion.getYoutube(),
                    'username': usuario.getUsername()
                    }
                    Datos.append(Dato)
    respuesta = jsonify(Datos)    
    return(respuesta)      

@app.route('/PlayList', methods=['GET'])
def ObtenerPlayListP():
    global Canciones
    global Individuales
    Datos = []
    for usuario in Individuales:
        for cancion in Canciones:
                if usuario.getId() == cancion.getId():
                    Dato = {
                    'Numero': usuario.getUsername(),
                    'id': cancion.getId(),
                    'nombre': cancion.getNombre(), 
                    'artista': cancion.getArtista(),
                    'album': cancion.getAlbum(),
                    'fecha': cancion.getFecha(),
                    'imagen': cancion.getImagen(),
                    'spotify': cancion.getSpotify(),
                    'youtube': cancion.getYoutube()
                    }
                    Datos.append(Dato)
    respuesta = jsonify(Datos)    
    return(respuesta)          

@app.route('/Solicitudes', methods=['GET'])
def ObtenerSolicitudes():
    global Solicitudes
    Datos = []
    for usuario in Solicitudes:
        Dato = {
            'nombre': usuario.getNombre(),
            'artista': usuario.getArtista(),
            'album': usuario.getAlbum(),
            'fecha': usuario.getFecha(),
            'imagen': usuario.getImagen(),
            'spotify': usuario.getSpotify(),
            'youtube': usuario.getYoutube(),
        }    
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)    

@app.route('/Personas/<string:username>', methods=['GET'])
def ObtenerPersona(username):
    global Usuarios
    Datos = []
    for usuario in Usuarios:
        if usuario.getUsuario() == username:    
            Dato = {'name': usuario.getNombre(), 
                'lastname': usuario.getApellido(),
                'username': usuario.getUsuario(),
                'password': usuario.getPassword(),
                'numero': usuario.getNumero()
            }
            Datos.append(Dato)
            break
    respuesta = jsonify(Datos)    
    return(respuesta)

@app.route('/Canciones/<string:id>', methods=['GET'])
def ObtenerCancion(id):
    global Canciones
    Datos = []
    for usuario in Canciones:
        if usuario.getId() == int(id):    
            Dato = {'nombre': usuario.getNombre(), 
                'artista': usuario.getArtista(),
                'album': usuario.getAlbum(),
                'fecha': usuario.getFecha(),
                'imagen': usuario.getImagen(),
                'spotify': usuario.getSpotify(),
                'youtube': usuario.getYoutube(),
                'id':usuario.getId()
            }
            Datos.append(Dato)
            break
    respuesta = jsonify(Datos)    
    return(respuesta)

@app.route('/Solicitudes/<string:nombre>', methods=['GET'])
def ObtenerSolicitud(nombre):
    print("Entro a Obtener una")
    global Solicitudes
    Datos = []
    print(nombre)
    for usuario in Solicitudes:
        print(nombre)
        if usuario.getNombre() == nombre: 
            print(nombre)
            Dato = {'nombre': usuario.getNombre(), 
                'artista': usuario.getArtista(),
                'album': usuario.getAlbum(),
                'fecha': usuario.getFecha(),
                'imagen': usuario.getImagen(),
                'spotify': usuario.getSpotify(),
                'youtube': usuario.getYoutube()
            }
            Datos.append(Dato)
            break

    print("Salio de Obtener una")
    respuesta = jsonify(Datos)    
    return(respuesta)

@app.route('/Personas/<string:username>', methods=['PUT'])
def ModificarPersona(username):
    global Usuarios
    for i in range(len(Usuarios)):
        if username == Usuarios[i].getUsuario():    
            print(username)
            print(Usuarios[i].getUsuario)
            Usuarios[i].setUsuario(request.json['username'])
            Usuarios[i].setNombre(request.json['name'])
            Usuarios[i].setApellido(request.json['lastname'])
            Usuarios[i].setPassword(request.json['password'])
            Usuarios[i].setTipo(request.json['tipo'])
            Dato = {'Modificado': 'Se modifico',
            'message':'Actualizado'
            }
            break  
        else:
            Dato = {'message':'No se Actualizo, ya existe el Nombre de Ususario'
            }
    resp = jsonify(Dato)
    return(resp)

@app.route('/Canciones/<string:id>', methods=['PUT'])
def ModificarCancion(id):
    global Canciones
    for i in range(len(Canciones)):
        if int(id) == Canciones[i].getId():    
            print(id)
            print(Canciones[i].getId())
            Canciones[i].setNombre(request.json['nombre'])
            Canciones[i].setArtista(request.json['artista'])
            Canciones[i].setAlbum(request.json['album'])
            Canciones[i].setFecha(request.json['fecha'])
            Canciones[i].setImagen(request.json['imagen'])
            Canciones[i].setSpotify(request.json['spotify'])
            Canciones[i].setYoutube(request.json['youtube'])
            Dato = {'Modificado': 'Se modifico',
            'message':'Actualizado'
            }
            break  
        else:
            Dato = {'No Modificado': 'No Se modifico',
            'message':'No se ha Actualizado'
            }
    resp = jsonify(Dato)        
    return(resp)

@app.route('/Personas/<string:username>', methods=['DELETE'])    
def EliminarUsuario(username):
    global Usuarios
    for i in range(len(Usuarios)):
        if  username == Usuarios[i].getUsuario():
            del Usuarios[i]
            Dato = {'Modificado': 'Se modifico',
            'message':'Eliminado'
            }
            break
        else:
            Dato = {'message':'No se Elimino, ya existe el Nombre de Ususario'
            }
    respuesta = jsonify(Dato)
    return(respuesta) 

@app.route('/Canciones/<string:id>', methods=['DELETE'])    
def EliminarCancion(id):
    global Canciones
    n = int(id)
    for i in range(len(Canciones)):
        if n == Canciones[i].getId():
            del Canciones[i]
            break
    return ("Se logro")    

@app.route('/Comentarios/<string:No>', methods=['DELETE'])    
def EliminarComentario(No):
    global Comentarios
    n = int(No)
    print(56+n)
    for i in range(len(Comentarios)):
        print(n+120)
        if n == Comentarios[i].getNo():
            Dato = {
                'message':'Success'
            }
            print(236+n)
            del Comentarios[i]
            break
        else:
            Dato = {
                'message':'Failure'
            }
    respuesta = jsonify(Dato)        
    return (respuesta)        

@app.route('/PlayList/<string:id>', methods=['DELETE'])    
def EliminardePlayList(id):
    global Individuales
    n= int(request.json['id'])
    np = int(id)
    for i in range(len(Individuales)):
        print(n+2)
        if np == Individuales[i].getUsername():
            print(n+56)
            if n == Individuales[i].getId():
                Dato = {
                    'message':'Si se elimino'
                }
                del Individuales[i]
                break
            else:
                Dato = {
                    'message':'Hizo user, pero no ID'
                }
        else:
            Dato = {
                    'message':'No encontro ni username'
                }        
    respuesta = jsonify(Dato)
    return(respuesta)            

@app.route('/Solicitudes/<string:nombre>', methods=['DELETE'])
def EliminarSolicitud(nombre):
    global Solicitudes
    print("Entro a Eliminar")
    print(nombre)
    for i in range(len(Solicitudes)):
        print(nombre)
        
        if nombre == Solicitudes[i].getNombre():
            print(nombre)
            
            del Solicitudes[i]
            Dato = {'Modificado': 'Se modifico',
            'message':'Eliminado'
            }
            break
        else:
            print("Es eklse del eliminar")
            print(nombre)

            Dato = {'No Modificado': 'No Se modifico',
            'message':'No Eliminado'
            }
    respuesta = jsonify(Dato)
    return(respuesta)        


@app.route('/Personas', methods=['POST'])
def RegistrarUsuarios():
    global Usuarios
    global cont_user
    flag = False 
    username = request.json['username']
    password = request.json['password']
    confirm = request.json['confirm']
    for usuario in Usuarios:
        if username == usuario.getUsuario():
            flag = True
            break
    if flag:
        Dato = {
                'message': 'Exists'
            }
    else:
        if  password == confirm :
            nuevo = Persona(request.json['name'], 
            request.json['lastname'], 
            request.json['username'], 
            request.json['password'],
            request.json['tipo'],
            cont_user)
            Usuarios.append(nuevo)
            Dato = {
                    'message': 'Success'
                }
        else:
            Dato = {
                    'message': 'Failure'
                }
    respuesta = jsonify(Dato)   
    cont_user+=1     
    return(respuesta)

@app.route('/Canciones', methods=['POST'])   
def RegistrarCanciones():
    global Canciones
    global cont_c
    print(request.json['nombre'])
    nuevo = Cancion(cont_c,
    request.json['nombre'],
    request.json['artista'],
    request.json['album'],
    request.json['fecha'],
    request.json['imagen'],
    request.json['spotify'],
    request.json['youtube']
    )
    Canciones.append(nuevo)
    cont_c+=1
    return("Se agregaron las Canciones correctamente")

@app.route('/Comentarios', methods=['POST'])   
def RegistrarComentarios():
    global Usuarios
    global Canciones
    global Comentarios
    global cont_comment

    nuevo = Comentario(cont_comment,
    int(request.json['id']),
    request.json['comentario'],
    request.json['username']
    )
    Comentarios.append(nuevo)
    print(int(request.json['id'])+1)
    cont_comment+=1
    return(request.json['id'])

@app.route('/PlayList/<string:id>', methods=['POST'])
def MeterAPlayList(id):
    global Individuales
    print(id)
    print(request.json['numero'])
    print(request.json['id'])
    
    nuevo = PlayList(
        int(id),
        int(request.json['id'])
    )
    Dato = {
        'message':'Success'
    }
    Individuales.append(nuevo)  
    print("Paso el append")
    respuesta = jsonify(Dato)
    return(respuesta)  

@app.route('/Solicitudes', methods=['POST'])
def RegistrarSolicitudes():
    global Solicitudes
    nuevo = Solicitud(
        request.json['nombre'],
        request.json['artista'],
        request.json['album'],
        request.json['fecha'],
        request.json['imagen'],
        request.json['spotify'],
        request.json['youtube']
    )
    Solicitudes.append(nuevo)
    return("Se agrego la Solicitud")



if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port=3000, debug=True)