import justpy as jp


@jp.SetRoute("/")
def home():
    wp = jp.QuasarPage(tailwind=True)
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    # div 1
    div1 = jp.Div(a=div, classes="grid grid-cols-3 gap-4 p-4")
    in_1 = jp.Input(a=div1, placeholder="Enter First Value",
                    classes="form-input")
    in_2 = jp.Input(a=div1, placeholder="Enter Second Value",
                    classes="form-input")
    d_output = jp.Div(a=div1, text="Results goes here..",
                      classes="text-gray-600")
    jp.Div(a=div1, text="Yet another div",
           classes="text-gray-600")
    jp.Div(a=div1, text="Again another div..",
           classes="text-gray-600")

    # calculate button in div 2
    div2 = jp.Div(a=div, classes="grid grid-cols-3 gap-4")
    jp.QBtn(a=div2, text="Calculate", click=sum_up, in1=in_1, in2=in_2,
            d=d_output,
            classes="border border-black-500 m-2 py-1 px-4 rounded "
                    "text-grey-400 hover:bg-red-500 hover:text-white")

    return wp


def sum_up(widget, msg):
    sum1 = float(widget.in1.value) + float(widget.in2.value)
    widget.d.text = sum1


def mouse_enter(widget, msg):
    pass


# jp.Route("/", home)

jp.justpy()
