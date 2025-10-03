# consulta_empleado.py
import flet as ft

def consulta_empleado():
    return ft.Column(
        [
            ft.Text("Pantalla: Consulta de empleados", size=28, weight=700, color="blue"),
            ft.Text("Aquí irá tu lógica para consultar empleados...", size=16, color="black"),
        ],
        expand=True,
        spacing=20
    )
