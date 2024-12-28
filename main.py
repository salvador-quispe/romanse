import flet as ft
import random

# Función principal para la aplicación
def main(page: ft.Page):
    # Dimensiones y posicionamiento de la ventana (más grande para mejor espacio)
    page.window.width = 1000  # Aumentado
    page.window.height = 700  # Aumentado
    page.window.center()  # Centrar la ventana en la pantalla
    page.title = "Botón Interactivo"

    # Movimiento mínimo permitido para el botón 'No'
    movimiento_minimo = 50
    max_top = 500
    max_left = 800

    # Función para mostrar el mensaje cuando se presiona 'Sí'
    def mostrar_respuesta(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text("¡Sabía que dirías que sí! 🥰", size=40),  # Texto centrado y tamaño doble
            actions=[
                ft.ElevatedButton("Cerrar", on_click=lambda e: page.window.close())
            ]
        )
        page.dialog.open = True
        page.update()

    # Función para mover el botón 'No' a una posición aleatoria
    def mover_boton_no(e):
        # Obtener la posición actual del contenedor
        top_actual = btn_no.top
        left_actual = btn_no.left

        # Calcular nueva posición asegurando un mínimo de movimiento
        nuevo_top, nuevo_left = top_actual, left_actual
        while abs(nuevo_top - top_actual) < movimiento_minimo or abs(nuevo_left - left_actual) < movimiento_minimo:
            nuevo_top = random.randint(0, int(max_top))
            nuevo_left = random.randint(0, int(max_left))

        # Actualizar posición del contenedor
        btn_no.top = nuevo_top
        btn_no.left = nuevo_left
        page.update()

    # Crear el texto centrado
    texto = ft.Text(
        "¿QUIERES SER MI NOVIA? 💖💫😍?", 
        size=40,  # Tamaño ajustado
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    # Crear el botón 'Sí'
    btn_si = ft.Container(
        content=ft.ElevatedButton("Sí", on_click=mostrar_respuesta, width=225, height=90),  # Botón reducido
        top=400,
        left=250
    )

    # Crear el botón 'No'
    btn_no = ft.Container(
        content=ft.ElevatedButton("No  (Cerrar ventana)", on_click=mover_boton_no, width=225, height=90),  # Botón reducido
        top=400,
        left=550
    )

    # Añadir elementos en un Stack para permitir posiciones absolutas
    page.add(
        ft.Stack([
            ft.Container(content=texto, top=100, left=200),  # Texto centrado horizontalmente
            btn_si,  # Botón Sí con posición fija
            btn_no   # Botón No con movimiento aleatorio
        ])
    )

# Ejecutar la aplicación
ft.app(target=main)
