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

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="Aspect based Sentiment Analysis", classes="text-4xl m-2")

        jp.Div(a=div, text="""Aspect-Based Sentiment Analysis (ABSA) is a type of text analysis that categorizes 
        opinions by aspect and identifies the sentiment related to each aspect.
        By aspects, we consider attributes or components of an entity (a product or a service, in our case).
        """,
               classes="text-lg")

        return wp
