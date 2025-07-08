# Hola, este programa lo hice para demostrar los conceptos de Programación Orientada a Objetos en Python.
# Aquí voy a usar clases, herencia, encapsulación, polimorfismo y objetos, como me lo pidieron en la tarea.

# Primero defino mi clase principal (base), que se llama Persona.
# Esta clase representa a cualquier persona, como empleado o gerente.
class Persona:
    def __init__(self, nombre, edad):
        # Estos atributos los encapsulé, por eso tienen doble guion bajo (__).
        self.__nombre = nombre
        self.__edad = edad

    # Este método me devuelve la información básica de una persona.
    def obtener_informacion(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"

    # Este método se puede sobrescribir en las clases hijas para mostrar polimorfismo.
    def hablar(self):
        return "Hola, soy una persona."

# Ahora creo la clase Empleado, que hereda de Persona.
# Con esto demuestro el concepto de herencia.
class Empleado(Persona):
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad)  # Aquí llamo al constructor de la clase base.
        self.__cargo = cargo  # Este atributo también está encapsulado.

    # Aquí sobrescribo el método para que el empleado tenga su propia forma de mostrar información.
    def obtener_informacion(self):
        return f"{super().obtener_informacion()}, Cargo: {self.__cargo}"

    # Polimorfismo: el método hablar se comporta diferente en esta clase.
    def hablar(self):
        return "Hola, soy un empleado."

# Esta es otra clase hija llamada Gerente, también hereda de Persona.
# Sirve para demostrar que puedo tener varias clases derivadas de una sola base.
class Gerente(Persona):
    def __init__(self, nombre, edad, departamento):
        super().__init__(nombre, edad)
        self.__departamento = departamento

    def obtener_informacion(self):
        return f"{super().obtener_informacion()}, Departamento: {self.__departamento}"

    def hablar(self):
        return "Hola, soy el gerente del departamento."

# En esta parte creo objetos de tipo Empleado y Gerente para probar todo.
empleado1 = Empleado("Carlos Pérez", 30, "Analista")
gerente1 = Gerente("Laura Gómez", 40, "Tecnología")

# Aquí voy a ponerlos en una lista para usar polimorfismo más fácil.
personas = [empleado1, gerente1]

# Recorro la lista y llamo a los métodos que cada clase tiene.
# Esto demuestra cómo el mismo método puede comportarse distinto (polimorfismo).
for persona in personas:
    print(persona.obtener_informacion())  # Aquí veo la info completa de cada objeto.
    print(persona.hablar())               # Aquí se nota el polimorfismo.
    print("-" * 40)  # Solo es una línea separadora para que el resultado se vea más ordenado.
