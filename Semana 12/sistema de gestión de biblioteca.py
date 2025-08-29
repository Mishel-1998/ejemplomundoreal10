# ==========================
# Sistema de Gestión de Biblioteca Digital
# ==========================

# --------------------------
# Clase Libro
# --------------------------
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Guardamos título y autor en una tupla inmutable
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]:40} | {self.info[1]:25} | {self.categoria:25} | ISBN: {self.isbn}"


# --------------------------
# Clase Usuario
# --------------------------
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"{self.nombre} (ID: {self.user_id})"


# --------------------------
# Clase Biblioteca
# --------------------------
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario ISBN -> Libro
        self.usuarios_registrados = {}  # Diccionario ID -> Usuario
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    # ----------------------
    # Métodos de gestión de libros
    # ----------------------
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro agregado: {libro.info[0]} de {libro.info[1]}")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            eliminado = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {eliminado.info[0]}")
        else:
            print(" No se encontró el libro con ese ISBN.")

    # ----------------------
    # Métodos de gestión de usuarios
    # ----------------------
    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.ids_usuarios:
            self.usuarios_registrados[usuario.user_id] = usuario
            self.ids_usuarios.add(usuario.user_id)
            print(f"👤 Usuario registrado: {usuario}")
        else:
            print("Ya existe un usuario con ese ID.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.ids_usuarios:
            eliminado = self.usuarios_registrados.pop(user_id)
            self.ids_usuarios.remove(user_id)
            print(f"Usuario dado de baja: {eliminado}")
        else:
            print(" No se encontró un usuario con ese ID.")

    # ----------------------
    # Métodos de préstamos
    # ----------------------
    def prestar_libro(self, user_id, isbn):
        if user_id not in self.usuarios_registrados:
            print(" Usuario no registrado.")
            return
        if isbn not in self.libros_disponibles:
            print(" Libro no disponible en este momento.")
            return

        usuario = self.usuarios_registrados[user_id]
        libro = self.libros_disponibles.pop(isbn)  # Se retira de disponibles
        usuario.libros_prestados.append(libro)
        print(f"Libro prestado: {libro.info[0]} -> {usuario.nombre}")

    def devolver_libro(self, user_id, isbn):
        if user_id not in self.usuarios_registrados:
            print(" Usuario no registrado.")
            return

        usuario = self.usuarios_registrados[user_id]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print(f"Libro devuelto: {libro.info[0]} por {usuario.nombre}")
                return
        print("El usuario no tiene ese libro en préstamo.")

    # ----------------------
    # Métodos de búsqueda
    # ----------------------
    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros_disponibles.values() if libro.info[0].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros_disponibles.values() if libro.info[1].lower() == autor.lower()]

    def buscar_por_categoria(self, categoria):
        return [libro for libro in self.libros_disponibles.values() if libro.categoria.lower() == categoria.lower()]

    # ----------------------
    # Métodos de consulta
    # ----------------------
    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios_registrados:
            usuario = self.usuarios_registrados[user_id]
            print("\nLIBROS PRESTADOS")
            print("-" * 80)
            if usuario.libros_prestados:
                for libro in usuario.libros_prestados:
                    print(f"  - {libro}")
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
            print("-" * 80)
        else:
            print("Usuario no registrado.")

    def mostrar_catalogo(self):
        print("\n CATÁLOGO DE LIBROS DISPONIBLES")
        print("-" * 120)
        print(f"{'Título':40} | {'Autor':25} | {'Categoría':25} | ISBN")
        print("-" * 120)
        for libro in self.libros_disponibles.values():
            print(libro)
        print("-" * 120)


# ==========================
# Pruebas del sistema
# ==========================
if __name__ == "__main__":
    # Crear biblioteca
    biblio = Biblioteca()

    # Crear libros
    libros = [
        Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "2004"),
        Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "222"),
        Libro("Gung Ho: Ardillas, castores y gansos", "Ken Blanchard & Sheldon Bowles", "Liderazgo / Motivación", "4001"),
        Libro("Los 7 hábitos de la gente altamente efectiva", "Stephen R. Covey", "Superación Personal", "2001"),
        Libro("Hábitos atómicos", "James Clear", "Superación Personal", "2007"),
        Libro("El arte de amar sin sufrir", "Walter Riso", "Superación Personal / Relaciones", "2012"),
        Libro("Sapiens: De animales a dioses", "Yuval Noah Harari", "Historia", "2005"),
        Libro("Cosmos", "Carl Sagan", "Ciencia / Divulgación", "2010"),
    ]

    # Agregar libros
    for libro in libros:
        biblio.agregar_libro(libro)

    # Registrar usuarios
    usuario1 = Usuario("Ana", "U01")
    usuario2 = Usuario("Luis", "U02")
    biblio.registrar_usuario(usuario1)
    biblio.registrar_usuario(usuario2)

    # Prestar libros
    biblio.prestar_libro("U01", "2004")  # Ana pide Cien Años de Soledad
    biblio.prestar_libro("U02", "222")   # Luis pide El Principito

    # Listar libros prestados
    biblio.listar_libros_prestados("U01")
    biblio.listar_libros_prestados("U02")

    # Mostrar catálogo
    biblio.mostrar_catalogo()

    # Buscar libros
    print("\n Búsqueda por autor 'Gabriel García Márquez':")
    for libro in biblio.buscar_por_autor("Gabriel García Márquez"):
        print(f"  - {libro}")

    print("\nBúsqueda por categoría 'Superación Personal':")
    for libro in biblio.buscar_por_categoria("Superación Personal"):
        print(f"  - {libro}")
