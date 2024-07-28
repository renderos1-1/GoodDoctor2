from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import views.inicio_view


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/health_record_view")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_health_record():

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

    canvas.create_text(
        1107.0,
        58.0,
        anchor="nw",
        text="josuetsai@gmail.com",
        fill="#000000",
        font=("Poppins Regular", 10 * -1)
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
        x=297.0,
        y=61.0,
        width=59.198219299316406,
        height=84.0
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
        x=217.0,
        y=58.0,
        width=59.198219299316406,
        height=83.9999771118164
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
        x=137.0,
        y=61.0,
        width=59.198219299316406,
        height=84.0
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
        x=57.0,
        y=58.0,
        width=59.198219299316406,
        height=84.0
    )

    canvas.create_text(
        70.0,
        30.0,
        anchor="nw",
        text="¿Cómo te sientes hoy?",
        fill="#371B34",
        font=("Epilogue Medium", 16 * -1)
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
        x=1107.0,
        y=104.0,
        width=67.0,
        height=29.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1068.0,
        59.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        70.0,
        285.0,
        370.0,
        728.0,
        fill="#EDECF4",
        outline="")

    canvas.create_text(
        160.0,
        323.0,
        anchor="nw",
        text="Diagnoses",
        fill="#000000",
        font=("Poppins Regular", 24 * -1)
    )

    canvas.create_text(
        57.0,
        234.0,
        anchor="nw",
        text="Add previous diagnoses",
        fill="#000000",
        font=("Poppins Regular", 20 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        233.0,
        425.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=133.0,
        y=404.0,
        width=200.0,
        height=40.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        233.0,
        497.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=133.0,
        y=476.0,
        width=200.0,
        height=41.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        233.0,
        568.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=133.0,
        y=548.0,
        width=200.0,
        height=39.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        233.0,
        637.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=133.0,
        y=616.0,
        width=200.0,
        height=40.0
    )

    canvas.create_rectangle(
        400.0,
        285.0,
        700.0,
        728.0,
        fill="#EDECF4",
        outline="")

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        428.0,
        425.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        428.0,
        568.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        428.0,
        497.0,
        image=image_image_4
    )

    canvas.create_rectangle(
        742.0,
        215.0,
        1191.0,
        476.0,
        fill="#EDECF4",
        outline="")

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        961.0,
        313.5,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=842.0,
        y=294.0,
        width=238.0,
        height=37.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        961.0,
        370.5,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=842.0,
        y=351.0,
        width=238.0,
        height=37.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        961.0,
        427.5,
        image=entry_image_7
    )
    entry_7 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_7.place(
        x=842.0,
        y=408.0,
        width=238.0,
        height=37.0
    )

    canvas.create_text(
        843.0,
        243.0,
        anchor="nw",
        text="Vaccines",
        fill="#000000",
        font=("Poppins Regular", 24 * -1)
    )

    canvas.create_text(
        742.0,
        181.0,
        anchor="nw",
        text="Add previous vaccines",
        fill="#000000",
        font=("Poppins Regular", 20 * -1)
    )

    canvas.create_rectangle(
        742.0,
        535.0,
        1191.0,
        796.0,
        fill="#EDECF4",
        outline="")

    entry_image_8 = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(
        961.0,
        633.5,
        image=entry_image_8
    )
    entry_8 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_8.place(
        x=842.0,
        y=614.0,
        width=238.0,
        height=37.0
    )

    entry_image_9 = PhotoImage(
        file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(
        961.0,
        690.5,
        image=entry_image_9
    )
    entry_9 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_9.place(
        x=842.0,
        y=671.0,
        width=238.0,
        height=37.0
    )

    entry_image_10 = PhotoImage(
        file=relative_to_assets("entry_10.png"))
    entry_bg_10 = canvas.create_image(
        961.0,
        747.5,
        image=entry_image_10
    )
    entry_10 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_10.place(
        x=842.0,
        y=728.0,
        width=238.0,
        height=37.0
    )

    canvas.create_text(
        843.0,
        568.0,
        anchor="nw",
        text="Allergies",
        fill="#000000",
        font=("Poppins Regular", 24 * -1)
    )

    canvas.create_text(
        742.0,
        502.0,
        anchor="nw",
        text="Add previous allergies",
        fill="#000000",
        font=("Poppins Regular", 20 * -1)
    )

    canvas.create_text(
        482.0,
        323.0,
        anchor="nw",
        text="Procedures",
        fill="#000000",
        font=("Poppins Regular", 24 * -1)
    )

    canvas.create_text(
        422.0,
        234.0,
        anchor="nw",
        text="Add previous procedures",
        fill="#000000",
        font=("Poppins Regular", 20 * -1)
    )

    entry_image_11 = PhotoImage(
        file=relative_to_assets("entry_11.png"))
    entry_bg_11 = canvas.create_image(
        564.5,
        425.0,
        image=entry_image_11
    )
    entry_11 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_11.place(
        x=465.0,
        y=404.0,
        width=199.0,
        height=40.0
    )

    entry_image_12 = PhotoImage(
        file=relative_to_assets("entry_12.png"))
    entry_bg_12 = canvas.create_image(
        564.5,
        497.5,
        image=entry_image_12
    )
    entry_12 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_12.place(
        x=465.0,
        y=476.0,
        width=199.0,
        height=41.0
    )

    entry_image_13 = PhotoImage(
        file=relative_to_assets("entry_13.png"))
    entry_bg_13 = canvas.create_image(
        564.5,
        568.5,
        image=entry_image_13
    )
    entry_13 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_13.place(
        x=465.0,
        y=548.0,
        width=199.0,
        height=39.0
    )

    entry_image_14 = PhotoImage(
        file=relative_to_assets("entry_14.png"))
    entry_bg_14 = canvas.create_image(
        564.5,
        637.0,
        image=entry_image_14
    )
    entry_14 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_14.place(
        x=465.0,
        y=616.0,
        width=199.0,
        height=40.0
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        429.0,
        637.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        129.0,
        338.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        451.0,
        336.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        807.0,
        259.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        813.0,
        581.0,
        image=image_image_9
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        98.0,
        425.0,
        image=image_image_10
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(
        802.0,
        370.0,
        image=image_image_11
    )

    image_image_12 = PhotoImage(
        file=relative_to_assets("image_12.png"))
    image_12 = canvas.create_image(
        802.0,
        633.0,
        image=image_image_12
    )

    image_image_13 = PhotoImage(
        file=relative_to_assets("image_13.png"))
    image_13 = canvas.create_image(
        802.0,
        747.0,
        image=image_image_13
    )

    image_image_14 = PhotoImage(
        file=relative_to_assets("image_14.png"))
    image_14 = canvas.create_image(
        802.0,
        690.0,
        image=image_image_14
    )

    image_image_15 = PhotoImage(
        file=relative_to_assets("image_15.png"))
    image_15 = canvas.create_image(
        802.0,
        427.0,
        image=image_image_15
    )

    image_image_16 = PhotoImage(
        file=relative_to_assets("image_16.png"))
    image_16 = canvas.create_image(
        802.0,
        313.0,
        image=image_image_16
    )

    image_image_17 = PhotoImage(
        file=relative_to_assets("image_17.png"))
    image_17 = canvas.create_image(
        98.0,
        638.0,
        image=image_image_17
    )

    image_image_18 = PhotoImage(
        file=relative_to_assets("image_18.png"))
    image_18 = canvas.create_image(
        98.0,
        569.0,
        image=image_image_18
    )

    image_image_19 = PhotoImage(
        file=relative_to_assets("image_19.png"))
    image_19 = canvas.create_image(
        98.0,
        497.0,
        image=image_image_19
    )

    canvas.create_text(
        1107.0,
        27.0,
        anchor="nw",
        text="Josue Tsai",
        fill="#000000",
        font=("Poppins Regular", 15 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
