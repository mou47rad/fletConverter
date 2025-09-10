import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            content=ft.ElevatedButton(
                text="زر في الوسط",
                bgcolor="red",
                color="white",
                on_click=lambda e: print("تم الضغط على الزر"),
            ),
            alignment=ft.alignment.center
            expand=True,
        )
    )

ft.app(main)
