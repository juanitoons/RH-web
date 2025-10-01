import flet as ft  # Importa la librería Flet para crear interfaces gráficas
from views.inicio import inicio  # Importa la función inicio desde el módulo views.inicio

def main(page: ft.Page):
    # Configuración inicial de la página
    page.title = "Sistema de RH"  # Título de la ventana

    # Label de usuario
    lbl_nombre = ft.Text(
        "Usuario",        # Texto que se mostrará
        color="white",    # Color del texto
        size=20,          # Tamaño de la fuente
        weight=700        # Negrita (700 equivale a bold)
    )
    
    # Campo de texto para el usuario
    txt_usuario = ft.TextField(
        bgcolor="white",                   # Color de fondo del TextField
        color="blue",                       # Color del texto
        width=300,                          # Ancho del campo
        border_radius=ft.border_radius.all(50)  # Bordes redondeados
    )

    # Label de contraseña
    lbl_contrasena = ft.Text(
        "Contraseña",
        color="white",
        size=20,
        weight=700
    )

    # Campo de texto para la contraseña
    txt_contrasena = ft.TextField(
        bgcolor="white",                    # Fondo blanco
        color="black",                      # Texto negro
        width=300,                           # Ancho
        password=True,                       # Oculta el texto ingresado
        can_reveal_password=True,            # Permite mostrar la contraseña con un botón
        border_radius=ft.border_radius.all(50)  # Bordes redondeados
    )

        # Función para navegar a la página de inicio/dashboard
    def ir_a_inicio(e):
        dashboard_layout = inicio()  # Llama a la función inicio() que retorna un layout (Control)
        page.views.clear()           # Limpia las vistas actuales
        page.views.append(ft.View("/inicio", [dashboard_layout]))  # Agrega la vista del dashboard
        page.go("/inicio")           # Navega a la vista agregada

    # Botón "Aceptar" que ejecuta la función ir_a_inicio al hacer clic
    btn_aceptar = ft.ElevatedButton(
        "Aceptar",
        color="blue",
        bgcolor="white",
        on_click=ir_a_inicio
    )

    # Contenedor azul que agrupa los labels y campos de texto
    contenedor = ft.Container(
        content=ft.Column(
            [lbl_nombre, txt_usuario, lbl_contrasena, txt_contrasena, btn_aceptar],  # Controles dentro del contenedor
            alignment=ft.MainAxisAlignment.CENTER,                     # Centrar verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER          # Centrar horizontalmente
        ),
        bgcolor="blue",       # Color de fondo del contenedor
        padding=20,           # Espaciado interno
        border_radius=15,     # Bordes ligeramente redondeados
    )

    # Función para navegar a la página de inicio/dashboard
    def ir_a_inicio(e):
        dashboard_layout = inicio()  # Llama a la función inicio() que retorna un layout (Control)
        page.views.clear()           # Limpia las vistas actuales
        page.views.append(ft.View("/inicio", [dashboard_layout]))  # Agrega la vista del dashboard
        page.go("/inicio")           # Navega a la vista agregada

    # Botón "Olvidé mi contraseña" (aún sin funcionalidad)
    btn_olvide = ft.ElevatedButton(
        "Olvide mi contraseña",
        color="white",
        bgcolor="red"
    )

    # Agrega todos los elementos a la página principal
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="assets/logo-telnor.png", width=150, height=50),  # Logo de la empresa
                    contenedor,         # Contenedor azul con campos de login
                    btn_olvide          # Botón olvidé contraseña
                ],
                alignment=ft.MainAxisAlignment.CENTER,           # Centrar verticalmente
                horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Centrar horizontalmente
            ),
            expand=True,            # El contenedor ocupa todo el espacio disponible
            alignment=ft.alignment.center  # Centrar el contenedor en la página
        )
    )

# Ejecuta la aplicación de Flet y asigna la función main como target
ft.app(target=main)
