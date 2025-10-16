import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from libro import Libro

class TestLibro:
    def test_creacion_libro(self):
        libro = Libro("1234567890", "Cien años de soledad", "Gabriel García Márquez")
        assert libro.isbn == "1234567890"
        assert libro.titulo == "Cien años de soledad"
        assert libro.autor == "Gabriel García Márquez"
        assert libro.disponible == True
    
    def test_prestar_libro_disponible(self):
        libro = Libro("1234567890", "Cien años de soledad", "Gabriel García Márquez")
        libro.prestar()
        assert libro.disponible == False
    
    def test_prestar_libro_no_disponible(self):
        libro = Libro("1234567890", "Cien años de soledad", "Gabriel García Márquez")
        libro.prestar()
        with pytest.raises(ValueError, match="no está disponible"):
            libro.prestar()
    
    def test_devolver_libro(self):
        libro = Libro("1234567890", "Cien años de soledad", "Gabriel García Márquez")
        libro.prestar()
        libro.devolver()
        assert libro.disponible == True
    
    def test_igualdad_libros(self):
        libro1 = Libro("1234567890", "Cien años de soledad", "Gabriel García Márquez")
        libro2 = Libro("1234567890", "Cien años de soledad", "Gabriel García Márquez")
        libro3 = Libro("0987654321", "Rayuela", "Julio Cortázar")
        
        assert libro1 == libro2
        assert libro1 != libro3
    
    def test_str_libro(self):
        libro = Libro("1234567890", "Cien años de soledad", "Gabriel García Márquez")
        expected_str = "'Cien años de soledad' por Gabriel García Márquez (ISBN: 1234567890)"
        assert str(libro) == expected_str