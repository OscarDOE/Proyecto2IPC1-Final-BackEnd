class Persona():
    
    def __init__(self, nombre, apellido, usuario, password, tipo, numero):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.tipo = tipo
        self.numero = numero

    def getNombre(self):
        return self.nombre
            
    def getApellido(self):
        return self.apellido
        
    def getUsuario(self):
        return self.usuario

    def getPassword(self):
        return self.password    

    def getTipo(self):
        return self.tipo       

    def getNumero(self):
        return self.numero





    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setPassword(self, password):
        self.password = password        

    def setTipo(self, tipo):
        self.tipo = tipo         

    def setNumero(self, numero):
        self.numero = numero     