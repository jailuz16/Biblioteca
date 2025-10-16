from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, id_prestamo: str, libro, usuario):
        self.id_prestamo = id_prestamo
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=14)
        self.devuelto = False
    
    def __str__(self):
        estado = "Devuelto" if self.devuelto else "Pendiente"
        return f"Préstamo {self.id_prestamo}: {self.libro.titulo} -> {self.usuario.nombre} ({estado})"
    
    def marcar_devuelto(self):
        self.devuelto = True
        self.fecha_devolucion = datetime.now()