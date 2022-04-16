import justpy as jp
from webapp import layout, page


class Home(page.Page):
    path = '/'

    @classmethod
    def serve(cls, request):

        wp = jp.QuasarPage(tailwind=True)

        # load default layout
        lay = layout.DefaultLayout(a=wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-green-100 h-screen p-2")
        jp.Div(a=div, text="Home", classes="text-6xl m-2 font-serif italic")
        jp.Br(a=div)

        jp.Div(a=div, text="""Aspect-Based Sentiment Analysis (ABSA) is a type of text analysis that categorizes 
        opinions by aspect and identifies the sentiment related to each aspect.
        By aspects, we consider attributes or components of an entity (a product or a service, in our case).
        """,
               classes="text-lg")
        jp.Br(a=div)
        jp.Img(src='../static/images/absa_example2.jpg', a=div, classes='m-2 p-2')

        return wp
