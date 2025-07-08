# Sistema de Gestión de Personas – POO en Python

Este proyecto lo realicé para demostrar los principales conceptos de la Programación Orientada a Objetos usando Python. Fue desarrollado en el IDE PyCharm como parte de una actividad académica de la Universidad Estatal Amazónica.

---

## Objetivo

Aplicar los conceptos de clases, objetos, herencia, encapsulación y polimorfismo en un ejercicio práctico, entendiendo cómo funciona cada uno desde la lógica de programación.

---

##  Descripción del programa

El programa simula un pequeño sistema de gestión de personas dentro de una empresa. Se definen dos roles específicos:

-  **Empleado**
-  **Gerente**

Ambos heredan de una clase base llamada `Persona`.

---

##  Conceptos aplicados de POO

| Concepto        | Aplicación en el código                                                  |
|-----------------|--------------------------------------------------------------------------|
| **Clase**       | Se definen clases como `Persona`, `Empleado` y `Gerente`.               |
| **Objeto**      | Se crean objetos (instancias) de `Empleado` y `Gerente`.                |
| **Herencia**    | Las clases `Empleado` y `Gerente` heredan de la clase base `Persona`.   |
| **Encapsulación** | Uso de atributos privados (`__nombre`, `__edad`, etc.) en las clases.     |
| **Polimorfismo**| Cada clase redefine el método `hablar()` a su propia manera.            |

---

## Archivos del proyecto

| Archivo                | Descripción                                               |
|------------------------|-----------------------------------------------------------|
| `conocimiento-poo.py`  | Archivo principal que contiene todo el código y pruebas. |
| `README.md`            | Este documento, con toda la explicación del proyecto.    |

> El proyecto está hecho en un solo archivo por simplicidad, pero modularizable si se desea.

---

##  ¿Cómo ejecutar el código?

Puedes ejecutarlo de dos formas:

**Desde terminal:**
```bash
python conocimiento-poo.py
