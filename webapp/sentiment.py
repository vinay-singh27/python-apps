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

        div = jp.Div(a=container, classes="bg-green-100 h-screen p-2")
        jp.Div(a=div, text="Entity Sentiment Analysis",
               classes="text-6xl m-2 font-serif italic")
        jp.Br(a=div)
        jp.Div(a=div, text="Extract the Entities in the text and get their sentiment",
               classes="text-lg m-2 p-2 font-sans ")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")

        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 border-purple-50 h-52 w-64 "
                                           "border-2 border-gray-500 rounded")
        input_box = jp.Input(a=input_div, placeholder="Enter the text here ...",
                             classes="m-2 bg-gray-100 border-2 border-gray-500 rounded w-100 h-40 focus:bg-white "
                                     "focus:outline-none focus:border-purple-500 py-2 px-4 ")
        button = jp.Button(a=input_div, click=get_sentiment, text="Calculate",
                           inputdiv=input_box, outputdiv=output_div,
                           classes="h-16 w-32 border-black-500 m-2 py-1 px-4 rounded "
                                   "text-black-800 bg-purple-500 hover:bg-red-500 hover:text-white ")

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
    print("Calculating Sentiment...")
    print(widget.input_box.value)
    defined = sentiment_analyzer.predict_sentiment(widget.input_box.value)
    print(defined)
    widget.outputdiv.text = defined
