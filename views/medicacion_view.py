from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/medicacion_view")

import views.inicio_view

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_medication():

    window = Tk()

    window.geometry("1280x818")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 818,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: window.destroy() or views.inicio_view.open_incio_view(),
        relief="flat"
    )
    button_1.place(
        x=1101.0,
        y=102.0,
        width=67.0,
        height=29.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        413.0,
        147.0,
        image=image_image_1
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
        x=174.0,
        y=641.0,
        width=249.0,
        height=59.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        301.0,
        409.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=115.0,
        y=394.0,
        width=372.0,
        height=28.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        301.0,
        492.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=115.0,
        y=477.0,
        width=372.0,
        height=28.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        174.5,
        572.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=115.0,
        y=559.0,
        width=119.0,
        height=25.0
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
        x=396.0,
        y=269.0,
        width=60.0,
        height=62.062652587890625
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
        x=310.0,
        y=271.0,
        width=59.198219299316406,
        height=62.062652587890625
    )

    canvas.create_text(
        119.0,
        370.0,
        anchor="nw",
        text="Name",
        fill="#424242",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        119.0,
        537.0,
        anchor="nw",
        text="Frecuencia",
        fill="#424242",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        252.0,
        567.0,
        anchor="nw",
        text="days",
        fill="#424242",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        108.0,
        246.0,
        anchor="nw",
        text="Type",
        fill="#424242",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        119.0,
        455.0,
        anchor="nw",
        text="Single dose, e.g. 1 tablet",
        fill="#424242",
        font=("Inter", 12 * -1)
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        887.7275085449219,
        683.2047100067139,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=596.0,
        y=653.7362060546875,
        width=583.4550170898438,
        height=56.937007904052734
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        887.7275085449219,
        573.1889629364014,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=596.0,
        y=543.720458984375,
        width=583.4550170898438,
        height=56.937007904052734
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        889.2724914550781,
        467.1023540496826,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=597.5449829101562,
        y=437.63385009765625,
        width=583.4550170898438,
        height=56.937007904052734
    )

    canvas.create_text(
        588.0,
        251.0,
        anchor="nw",
        text="Medicamentos",
        fill="#000000",
        font=("RalewayRoman Medium", 24 * -1)
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        887.7275085449219,
        361.01574516296387,
        image=entry_image_7
    )
    entry_7 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_7.place(
        x=596.0,
        y=331.5472412109375,
        width=583.4550170898438,
        height=56.937007904052734
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        1064.0,
        62.0,
        image=image_image_2
    )

    canvas.create_text(
        1101.0,
        68.0,
        anchor="nw",
        text="josuetsai@gmail.com",
        fill="#000000",
        font=("Poppins Regular", 10 * -1)
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
        x=141.0,
        y=271.0,
        width=59.198219299316406,
        height=62.062652587890625
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=225.0,
        y=271.0,
        width=59.198219299316406,
        height=62.062652587890625
    )

    canvas.create_text(
        1116.0,
        41.0,
        anchor="nw",
        text="Josue Tsai",
        fill="#000000",
        font=("Poppins Regular", 15 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
