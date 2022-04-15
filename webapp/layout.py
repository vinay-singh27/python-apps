import justpy as jp


class DefaultLayout(jp.QLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # layout
        header = jp.QHeader(a=self)
        q_toolbar = jp.QToolbar(a=header)

        # drawer
        drawer = jp.QDrawer(a=self, show_if_above=True, v_mode="left", bordered=True)
        scroll = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroll)
        a_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=qlist, text="Home", href="/", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classes)
        jp.Br(a=qlist)

        jp.QBtn(a=q_toolbar, dense=True, flat=True, round=True, icon="menu", click=self.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=q_toolbar, text="Instant Dictionary")

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
