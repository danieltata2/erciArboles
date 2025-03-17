import datetime
import flet as ft
import ddbb
import formularioPage
import consultasPag

def main(page: ft.Page):
    page.title = "CONTROL JARDIN"

    def route_change(e):
        page.views.clear()

        if page.route == "/formulario":
            page.views.append(
                ft.View(
                    route="/formulario",
                    controls=[formularioPage.main(page)]  # Asegúrate de que formularioPage.main(page) devuelva controles válidos
                )
            )

        elif page.route == "/consultas":
            page.views.append(
                ft.View(
                    route="/consultas",
                    controls=[consultasPag.main(page)]  # Asegúrate de que consultasPag.main(page) devuelva controles válidos
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go("/formulario")  # Esto inicia la aplicación con la ruta "/formulario"



if __name__ == "__main__":
    ft.app(target=main,view=ft.WEB_BROWSER,port=8080)
