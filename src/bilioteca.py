from .libro import Libro
from .usuario import Usuario
from .prestamo import Prestamo

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.usuarios = []
        self.prestamos = []
        self._contador_prestamos = 1
    
    def agregar_libro(self, libro: Libro):
        if libro in self.catalogo:
            raise ValueError(f"El libro '{libro.titulo}' ya existe en el catálogo")
        self.catalogo.append(libro)
    
    def eliminar_libro(self, isbn: str):
        libro = self.buscar_libro_por_isbn(isbn)
        if libro:
            self.catalogo.remove(libro)
            return True
        return False
    
    def registrar_usuario(self, usuario: Usuario):
        if usuario in self.usuarios:
            raise ValueError(f"El usuario '{usuario.nombre}' ya está registrado")
        self.usuarios.append(usuario)
    
    def buscar_libro_por_isbn(self, isbn: str):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                return libro
        return None
    
    def buscar_libro_por_titulo(self, titulo: str):
        return [libro for libro in self.catalogo if titulo.lower() in libro.titulo.lower()]
    
    def buscar_libro_por_autor(self, autor: str):
        return [libro for libro in self.catalogo if autor.lower() in libro.autor.lower()]
    
    def buscar_usuario_por_id(self, id_usuario: str):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None
    
    def prestar_libro(self, isbn: str, id_usuario: str):
        libro = self.buscar_libro_por_isbn(isbn)
        if not libro:
            raise ValueError(f"Libro con ISBN {isbn} no encontrado")
        
        usuario = self.buscar_usuario_por_id(id_usuario)
        if not usuario:
            raise ValueError(f"Usuario con ID {id_usuario} no encontrado")
        
        if not libro.disponible:
            raise ValueError(f"El libro '{libro.titulo}' no está disponible")
        
        # Realizar préstamo
        libro.prestar()
        usuario.tomar_prestado(libro)
        
        prestamo = Prestamo(f"P{self._contador_prestamos}", libro, usuario)
        self.prestamos.append(prestamo)
        self._contador_prestamos += 1
        
        return prestamo
    
    def devolver_libro(self, isbn: str, id_usuario: str):
        libro = self.buscar_libro_por_isbn(isbn)
        if not libro:
            raise ValueError(f"Libro con ISBN {isbn} no encontrado")
        
        usuario = self.buscar_usuario_por_id(id_usuario)
        if not usuario:
            raise ValueError(f"Usuario con ID {id_usuario} no encontrado")
        
        # Buscar préstamo activo
        prestamo_activo = None
        for prestamo in self.prestamos:
            if (prestamo.libro == libro and 
                prestamo.usuario == usuario and 
                not prestamo.devuelto):
                prestamo_activo = prestamo
                break
        
        if not prestamo_activo:
            raise ValueError(f"No existe un préstamo activo de este libro para este usuario")
        
        # Procesar devolución
        libro.devolver()
        usuario.devolver_libro(libro)
        prestamo_activo.marcar_devuelto()
        
        return prestamo_activo
    
    def obtener_libros_disponibles(self):
        return [libro for libro in self.catalogo if libro.disponible]
    
    def obtener_libros_prestados(self):
        return [libro for libro in self.catalogo if not libro.disponible]
    
    def obtener_prestamos_activos(self):
        return [prestamo for prestamo in self.prestamos if not prestamo.devuelto]