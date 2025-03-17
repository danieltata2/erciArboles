import datetime
import flet as ft
import ddbb
def main(page: ft.Page):
    page.title = "CONTROL JARDIN"

    def crear_arbol(e):
        nombre=nombre_tf.value
        tipo=tipos_drop.value
        altura=altura_tf.value
        fecha=date_picker.value
        ddbb.insertar_arbol(nombre,tipo,altura,fecha)

    def volver(e):
        page.go("/consultas")

    def get_tipos():
        lista_tipos = []
        lista_tipos.append(ft.dropdown.Option(text="PERENNE", key="PERENNE"))
        lista_tipos.append(ft.dropdown.Option(text="Caduca", key="Caduca"))
        return lista_tipos

    def abrir_selector(e):
        date_picker.open = True
        page.update()

    def seleccionar_fecha(e):
        # Actualiza el texto de la fecha seleccionada
        fecha_txt.value = f"{date_picker.value.day}/{date_picker.value.month}/{date_picker.value.year}"
        date_picker.open = False  # Cierra el selector
        page.update()

    # Definir los objetos dentro de main
    nombre_tf = ft.TextField(label="NOMBRE", width=300)
    tipos_drop = ft.Dropdown(label="TIPO", width=300, options=get_tipos())
    altura_tf = ft.TextField(label="ALTURA", width=300)

    date_picker = ft.DatePicker(value=datetime.datetime.now(), on_change=seleccionar_fecha)
    fecha_txt = ft.Text(f"{date_picker.value.day}/{date_picker.value.month}/{date_picker.value.year}", size=20)





    columna_datos = ft.Column(
        controls=[
            ft.Text("ARBOLES", size=40),
            nombre_tf,
            tipos_drop,
            altura_tf,
            fecha_txt,
            ft.FilledButton("SELECCIONAR FECHA", on_click=abrir_selector),
            ft.FilledButton("CREAR ARBOLES", on_click=crear_arbol)
        ],
    )

    page.overlay.append(date_picker)  # Añadir el DatePicker a la capa de superposición
    #page.add(columna_datos)
    return columna_datos