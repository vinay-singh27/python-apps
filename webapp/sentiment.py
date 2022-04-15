import justpy as jp
from webapp import layout, page
import requests
from sentiment_analysis import PredictSentiment


class Sentiment(page.Page):
    path = "/sentiment"

    @classmethod
    def serve(cls, request):
        wp = jp.QuasarPage(tailwind=True)

        # default layout
        lay = layout.DefaultLayout(a=wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Entity Sentiment Analysis",
               classes="text-4xl m-2")
        jp.Div(a=div, text="Get the sentiment of all the entities present in the text",
               classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")

        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 border-purple-200 h-40")
        input_box = jp.Input(a=input_div, placeholder="Type in a word here...", outputdiv=output_div,
                             classes="m-2 bg-gray-100 border-2 border-gray-500 rounded w-64 focus:bg-white "
                                     "focus:outline-none focus:border-purple-500 py-2 px-4")
        input_box.on('input', get_sentiment)

        return wp

    # @staticmethod
    # def get_sentiment(widget, msg):
    #     defined = PredictSentiment().predict_sentiment(widget.value)
    #     # req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")
    #     # data = req.json()
    #     # defined = "\n".join(data["Definition"])
    #     widget.outputdiv.text = defined


sentiment_analyzer = PredictSentiment()


def get_sentiment(widget, msg):

    defined = sentiment_analyzer.predict_sentiment(widget.value)
    widget.outputdiv.text = defined

