class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
    
    def __str__(self):
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn})"
    
    def __eq__(self, other):
        if not isinstance(other, Libro):
            return False
        return self.isbn == other.isbn
    
    def prestar(self):
        if not self.disponible:
            raise ValueError(f"El libro '{self.titulo}' no está disponible")
        self.disponible = False
    
    def devolver(self):
        self.disponible = True