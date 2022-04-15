import justpy as jp
import inspect

from webapp.about import About
from webapp.home import Home
from webapp.sentiment import Sentiment
from webapp import page

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)

jp.justpy(port=8001)
