class Comentario():
    def __init__(self,No, id, comentario, usuario):
        self.No = No
        self.id = id
        self.comentario = comentario
        self.usuario = usuario



    def getNo(self):
        return self.No

    def getId(self):
        return self.id

    def getComentario(self):
        return self.comentario

    def getUsuario(self):
        return self.usuario



    def setNo(self, No):
        self.No = No

    def setId(self, id):
        self.id = id
    
    def setComentario(self, comentario):
        self.comentario = comentario
    
    def setUsuario(self, usuario):
        self.usuario = usuario

