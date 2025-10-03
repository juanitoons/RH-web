import flet as ft                                 # Importa la librería Flet para crear interfaces gráficas
from .consulta_empleado import consulta_empleado  # Importa la función para la pantalla de consulta

def inicio():                                     # Define la función principal que construye la vista de inicio
    # -------- Estado inicial --------
    menu_expandido = ft.Ref()                                           # Referencia para saber si el menú lateral está expandido o contraído
    menu_expandido.current = True
    contenido = ft.Container(expand=True, bgcolor="white", padding=24)  # Área de contenido dinámico
    menu_container = ft.Ref()                                           # Referencia para actualizar el menú lateral cuando se expanda/contraiga

    # -------- Contenido dinámico --------
    def mostrar_contenido(opcion, actualizar=False):  
        """
        Cambia el contenido principal según la opción seleccionada.
        - opcion: "menu_inicio", "menu_consulta" o "menu_subir"
        - actualizar: si True, actualiza el contenedor en la página inmediatamente
        """
        if opcion == "menu_inicio":   # Si la opción es el inicio
            # Pantalla de inicio con accesos rápidos a las secciones
            contenido.content = ft.Column(
                [
                    ft.Text("Inicio", size=28, weight=700, color="blue"),  # Título de la página
                    ft.Row(   # Fila de accesos rápidos
                        [
                            # Tarjeta "Consulta de empleados"
                            ft.Container(
                                content=ft.Column(   # Columna con ícono y texto
                                    [
                                        ft.Icon(name=ft.Icons.PERSON, size=40, color=ft.Colors.WHITE), # Ícono de persona
                                        ft.Text("Consulta de empleados", weight=700, color=ft.Colors.WHITE), # Texto
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER, # Centra el contenido
                                    spacing=6
                                ),
                                width=260,  # Ancho de la tarjeta
                                height=120, # Alto de la tarjeta
                                bgcolor="#0b6b5e",  # Color de fondo verde
                                border_radius=30,   # Bordes redondeados
                                alignment=ft.alignment.center, # Centrado
                                # Al hacer clic, cambia al contenido de consulta
                                on_click=lambda e: mostrar_contenido("menu_consulta", True)
                            ),
                            # Tarjeta "Subir Archivo"
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Icon(name=ft.Icons.UPLOAD_FILE, size=40, color=ft.Colors.WHITE), # Ícono de archivo
                                        ft.Text("Subir Archivo", weight=700, color=ft.Colors.WHITE),       # Texto
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER, # Centra el contenido
                                    spacing=6
                                ),
                                width=260,
                                height=120,
                                bgcolor="#0b6b5e",   # Fondo verde
                                border_radius=30,    # Bordes redondeados
                                alignment=ft.alignment.center,
                                # Al hacer clic, cambia al contenido de subir archivo
                                on_click=lambda e: mostrar_contenido("menu_subir", True)
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # Centra las tarjetas en la fila
                        spacing=24,  # Espaciado entre tarjetas
                    ),
                ],
                expand=True,  # Expande para llenar espacio
                spacing=20    # Espaciado entre elementos de la columna
            )
        elif opcion == "menu_consulta":   # Si se selecciona consulta
            # Llama a la función que retorna el layout de consulta de empleados
            contenido.content = consulta_empleado()
        elif opcion == "menu_subir":      # Si se selecciona subir archivo
            # Pantalla temporal de "Subir Archivo"
            contenido.content = ft.Column(
                [ft.Text("Pantalla: Subir Archivo", size=20, color="black")], # Texto simple
                expand=True
            )

        # Actualiza el contenedor si ya está montado en la página
        if actualizar:
            contenido.update()

    # -------- Menú lateral --------
    def alternar_menu(e):  
        """
        Expande o contrae el menú lateral
        """
        menu_expandido.current = not menu_expandido.current  # Cambia el estado expandido/colapsado
        menu_container.current.content = construir_menu()    # Reconstruye el menú
        menu_container.current.update()                      # Actualiza el menú en pantalla

    def construir_menu():  
        """
        Construye el menú lateral, con íconos centrados cuando está contraído
        """
        ancho = 220 if menu_expandido.current else 60  # Ancho del menú según estado expandido/colapsado

        # Lista de opciones del menú, centradas si el menú está contraído
        tiles = [
            ft.Container(
                content=ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.HOME),  # Ícono de inicio
                    title=ft.Text("Inicio") if menu_expandido.current else None,  # Texto visible solo expandido
                    content_padding=0,
                    on_click=lambda e: mostrar_contenido("menu_inicio", True)
                ),
                alignment=ft.alignment.center if not menu_expandido.current else None
            ),
            ft.Container(
                content=ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.PERSON), # Ícono de persona
                    title=ft.Text("Consulta") if menu_expandido.current else None,
                    content_padding=0,
                    on_click=lambda e: mostrar_contenido("menu_consulta", True)
                ),
                alignment=ft.alignment.center if not menu_expandido.current else None
            ),
            ft.Container(
                content=ft.ListTile(
                    leading=ft.Icon(name=ft.Icons.UPLOAD_FILE), # Ícono de subir archivo
                    title=ft.Text("Subir Archivo") if menu_expandido.current else None,
                    content_padding=0,
                    on_click=lambda e: mostrar_contenido("menu_subir", True)
                ),
                alignment=ft.alignment.center if not menu_expandido.current else None
            ),
        ]

        controls = []  # Lista de controles que contendrá el menú final

        # Título "Menú" y línea gris solo si el menú está expandido
        if menu_expandido.current:
            controls.append(
                ft.Container(
                    content=ft.Text("Menú", weight=700, size=20, color="#0b6b5e"), # Título
                    alignment=ft.alignment.center
                )
            )
            controls.append(ft.Divider(color="grey", thickness=1))  # Línea divisoria gris

        # Contenedor de la lista de opciones
        controls.append(
            ft.Container(
                expand=True,
                content=ft.ListView(  # Lista de opciones
                    controls=tiles,
                    expand=True,
                    padding=0,
                    spacing=8,
                )
            )
        )

        # Botón para alternar el menú
        controls.append(
            ft.IconButton(
                icon=ft.Icons.KEYBOARD_ARROW_LEFT if menu_expandido.current else ft.Icons.KEYBOARD_ARROW_RIGHT,
                icon_color=ft.Colors.WHITE,    # Color blanco del ícono
                bgcolor="#0b6b5e",           # Fondo verde del botón
                on_click=alternar_menu         # Acción al hacer clic
            )
        )

        # Contenedor final del menú lateral
        return ft.Container(
            width=ancho,  # Ancho dinámico
            bgcolor="white",
            padding=12,
            border=ft.border.only(right=ft.BorderSide(1, "grey")),  # Línea gris derecha
            content=ft.Column(controls, expand=True, spacing=8),    # Contenido del menú en columna
        )

    # -------- Header fijo --------
    header = ft.Container(
        content=ft.Row(
            [
                ft.Image(src="assets/logo-telnor.png", width=150)  # Logo en el header
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,          # Alinea elementos a los extremos
            vertical_alignment=ft.CrossAxisAlignment.CENTER        # Centra verticalmente
        ),
        bgcolor="white",  # Fondo blanco
        padding=ft.padding.symmetric(horizontal=10, vertical=10),  # Espaciado interno
        border=ft.border.only(bottom=ft.BorderSide(1, "grey"))     # Línea gris debajo del header
    )

    # -------- Layout principal --------
    # Combina header y fila con menú + contenido
    layout = ft.Column(
        [
            header,  # Header fijo
            ft.Row([
                ft.Container(ref=menu_container, content=construir_menu()),  # Menú lateral
                contenido  # Área de contenido dinámico
            ], expand=True)
        ],
        expand=True
    )

    mostrar_contenido("menu_inicio")   # Pantalla inicial
    return layout                      # Devuelve el layout completo
