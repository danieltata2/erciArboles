import flet as ft

from ddbb import consultar_arboles


def main(page: ft.Page):
    page.title= "Consultas"

    def crear_tabla(datos):
        tabla.rows=[]
        for fila in datos:
            tabla.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(fila[0]))),# ID
                ft.DataCell(ft.Text(str(fila[1]))),#
                ft.DataCell(ft.Text(str(fila[2]))), #
                ft.DataCell(ft.Text(str(fila[3]))),#
                ft.DataCell(ft.Text(str(fila[4]))),#

            ]))


    #   objetos
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Altura")),
            ft.DataColumn(ft.Text("Fecha")),

        ]
    )


    columna_datos= ft.Column(
        controls=[
            ft.Text("CONSULTAS",size=49),
            tabla
        ]
    )

    #page.add(columna_datos)
    consultar_arboles()

    return columna_datos
