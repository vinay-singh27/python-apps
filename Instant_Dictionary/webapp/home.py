import justpy as jp
from webapp import layout, page


class Home(page.Page):
    path = "/"

    @classmethod
    def serve(cls, request):
        wp = jp.QuasarPage(tailwind=True)

        # load default layout
        lay = layout.DefaultLayout(a=wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is Home page", classes="text-4xl m-2")
        jp.Div(a=div, text="""A dictionary is a listing of lexemes from the lexicon of one or more specific languages, 
        often arranged alphabetically (or by radical and stroke for ideographic languages), which may include 
        information on definitions, usage, etymologies, pronunciations, translation, etc. It is a lexicographical 
        reference that shows inter-relationships among the data.
        A broad distinction is made between general and specialized dictionaries. Specialized dictionaries include 
        words in specialist fields, rather than a complete range of words in the language. Lexical items that describe 
        concepts in specific fields are usually called terms instead of words, although there is no consensus whether 
        lexicology and terminology are two different fields of study. In theory, general dictionaries are supposed
         to be seismological, mapping word to definition, while specialized dictionaries are supposed to be 
         immunological, first identifying concepts and then establishing the terms used to designate them. 
         In practice, the two approaches are used for both types. There are other types of dictionaries that do not 
         fit neatly into the above distinction, for instance bilingual (translation) dictionaries, dictionaries of 
         synonyms (thesauri), and rhyming dictionaries. The word dictionary (unqualified) is usually understood to 
         refer to a general purpose monolingual dictionary.""",
               classes="text-lg")

        return wp



