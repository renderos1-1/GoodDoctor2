from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import views.inicio_view

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/activity_tracker_view")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_activity_tracker():

    window = Tk()

    window.geometry("1280x832")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 832,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        160.0,
        fill="#EDECF4",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        201.0,
        90.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=92.0,
        y=210.0,
        width=261.0,
        height=223.5
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=406.0,
        y=247.0,
        width=249.0,
        height=59.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=406.0,
        y=328.0,
        width=249.0,
        height=59.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=93.0,
        y=477.0,
        width=484.0,
        height=64.0
    )

    canvas.create_text(
        294.0,
        620.0,
        anchor="nw",
        text="40:00:05",
        fill="#000000",
        font=("Poppins SemiBold", 44 * -1)
    )

    canvas.create_rectangle(
        100.0,
        596.0,
        245.0,
        734.0,
        fill="#EDECF4",
        outline="")

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        172.0,
        670.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        970.0,
        434.0,
        image=image_image_3
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: window.destroy() or views.inicio_view.open_incio_view(),
        relief="flat"
    )
    button_5.place(
        x=1125.0,
        y=105.0,
        width=67.0,
        height=29.0
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        1089.0,
        59.0,
        image=image_image_4
    )

    canvas.create_text(
        1143.0,
        37.0,
        anchor="nw",
        text="Josue Tsai",
        fill="#000000",
        font=("Poppins Regular", 12 * -1)
    )

    canvas.create_text(
        1125.0,
        57.0,
        anchor="nw",
        text="josuetsai@gmail.com",
        fill="#000000",
        font=("Poppins Regular", 10 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
