import justpy as jp
from sentiment_analysis import PredictSentiment
import json


class API:
    """
    Requests Handles at /?w=sentence
    """

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        text = req.query_params.get('w')
        # jp.Div(a=wp, text=word.title())
        sentiment_df = PredictSentiment.predict_sentiment(text)
        response = {
            "word": text,
            "Sentiment": sentiment_df
        }
        wp.html = json.dumps(response)

        return wp





