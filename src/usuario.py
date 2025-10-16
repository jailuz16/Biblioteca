class Usuario:
    def __init__(self, id_usuario: str, nombre: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []
    
    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"
    
    def __eq__(self, other):
        if not isinstance(other, Usuario):
            return False
        return self.id_usuario == other.id_usuario
    
    def tomar_prestado(self, libro):
        self.libros_prestados.append(libro)
    
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            raise ValueError(f"El usuario no tiene prestado el libro '{libro.titulo}'")
        