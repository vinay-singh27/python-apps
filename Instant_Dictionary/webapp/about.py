import justpy as jp
from webapp import layout, page


class About(page.Page):
    path = "/about"

    def serve(self):

        wp = jp.QuasarPage(tailwind=True)

        # import default layout
        lay = layout.DefaultLayout(a=wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is about page", classes="text-4xl m-2")
        jp.Div(a=div, text="""Originally spoken by small groups of people living along the lower Tiber River, 
        Latin spread with the increase of Roman political power, first throughout Italy and then throughout most of 
        western and southern Europe and the central and western Mediterranean coastal regions of Africa. 
        The modern Romance languages developed from the spoken Latin of various parts of the Roman Empire.
         During the Middle Ages and until comparatively recent times, Latin was the language most widely used 
         in the West for scholarly and literary purposes. Until the latter part of the 20th century its 
         use was required in the liturgy of the Roman Catholic Church.
        """, classes="text-lg")

        return wp



