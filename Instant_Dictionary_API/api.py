import justpy as jp
import definition
import json


class Api:
    """
    Requests Handles at /?w=word
    """

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        # jp.Div(a=wp, text=word.title())
        defined = definition.Definition(word.lower()).get()
        response = {
            "word": word,
            "Definition": defined
        }
        wp.html = json.dumps(response)

        return wp



