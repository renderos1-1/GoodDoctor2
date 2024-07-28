from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from .activity_tracker_view import open_activity_tracker
from .medicacion_view import open_medication
from .health_record_view import open_health_record
from .body_measurements_view import open_body_measurements


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/inicio_view")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def open_incio_view():

    window = Tk()

    window.geometry("1280x832")
    window.configure(bg = "#EDECF4")


    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=832,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        160.0,
        fill="#EDECF4",
        outline="")

    canvas.create_text(
        1123.0,
        59.0,
        anchor="nw",
        text="josuetsai@gmail.com",
        fill="#000000",
        font=("Poppins Regular", 8 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1075.0,
        59.0,
        image=image_image_1
    )

    canvas.create_text(
        90.0,
        65.0,
        anchor="nw",
        text="Welcome Josué!",
        fill="#422C81",
        font=("Inter Bold", 48 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        397.0,
        325.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        807.0,
        325.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        397.0,
        599.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        807.0,
        583.0,
        image=image_image_5
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: window.destroy() or open_activity_tracker(),
        relief="flat"
    )
    button_1.place(
        x=253.0,
        y=435.0,
        width=137.0,
        height=32.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: window.destroy() or open_health_record(),
        relief="flat"
    )
    button_2.place(
        x=253.0,
        y=706.0,
        width=119.0,
        height=31.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: window.destroy() or open_body_measurements(),
        relief="flat"
    )
    button_3.place(
        x=663.0,
        y=706.0,
        width=179.0,
        height=31.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: window.destroy() or open_medication(),
        relief="flat"
    )
    button_4.place(
        x=663.0,
        y=435.0,
        width=106.0,
        height=32.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=1116.0,
        y=101.0,
        width=67.0,
        height=29.0
    )

    canvas.create_text(
        1128.0,
        41.0,
        anchor="nw",
        text="Josue Tsai",
        fill="#000000",
        font=("Poppins Regular", 12 * -1)
    )
    window.resizable(False, False)
    window.mainloop()