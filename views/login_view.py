from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from views.inicio_view import open_incio_view

from controllers.login_controller import handle_login

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/login_views")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_login():

    window = Tk()

    window.geometry("1280x832")
    window.configure(bg = "#EDECF4")


    canvas = Canvas(
        window,
        bg = "#EDECF4",
        height = 832,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        570.0,
        356.0,
        anchor="nw",
        text="GoodDoctor",
        fill="#000000",
        font=("Inter SemiBold", 24 * -1)
    )

    canvas.create_text(
        501.0,
        405.0,
        anchor="nw",
        text="Enter your email to log in for this app",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        640.0,
        507.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=448.0,
        y=487.0,
        width=384.0,
        height=38.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: handle_login(entry_1,entry_2, window),
        relief="flat"
    )
    button_1.place(
        x=471.0,
        y=653.0,
        width=339.0,
        height=56.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        640.0,
        582.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=448.0,
        y=562.0,
        width=384.0,
        height=38.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        640.0,
        217.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()
