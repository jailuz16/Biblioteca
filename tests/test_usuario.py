import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from usuario import Usuario
from libro import Libro

class TestUsuario:
    def test_creacion_usuario(self):
        usuario = Usuario("U001", "Juan Pérez")
        assert usuario.id_usuario == "U001"
        assert usuario.nombre == "Juan Pérez"
        assert usuario.libros_prestados == []
    
    def test_tomar_libro_prestado(self):
        usuario = Usuario("U001", "Juan Pérez")
        libro = Libro("1234567890", "Cien años de soledad", "Gabriel García Márquez")
        
        usuario.tomar_prestado(libro)
        assert len(usuario.libros_prestados) == 1
        assert libro in usuario.libros_prestados
    
    def test_devolver_libro_existente(self):
        usuario = Usuario("U001", "Juan Pérez")
        libro = Libro("1234567890", "Cien años de soledad", "Gabriel García Márquez")
        
        usuario.tomar_prestado(libro)
        usuario.devolver_libro(libro)
        assert len(usuario.libros_prestados) == 0
    
    def test_devolver_libro_inexistente(self):
        usuario = Usuario("U001", "Juan Pérez")
        libro = Libro("1234567890", "Cien años de soledad", "Gabriel García Márquez")
        otro_libro = Libro("0987654321", "Rayuela", "Julio Cortázar")
        
        usuario.tomar_prestado(libro)
        with pytest.raises(ValueError, match="no tiene prestado"):
            usuario.devolver_libro(otro_libro)
    
    def test_igualdad_usuarios(self):
        usuario1 = Usuario("U001", "Juan Pérez")
        usuario2 = Usuario("U001", "Juan Pérez")
        usuario3 = Usuario("U002", "María García")
        
        assert usuario1 == usuario2
        assert usuario1 != usuario3
    
    def test_str_usuario(self):
        usuario = Usuario("U001", "Juan Pérez")
        expected_str = "Usuario: Juan Pérez (ID: U001)"
        assert str(usuario) == expected_str