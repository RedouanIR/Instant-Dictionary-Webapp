import justpy as jp
from definition import Definition



class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls, request):
        wp = jp.QuasarPage(tailwind=True)
        mainDiv = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        titleDiv = jp.Div(a=mainDiv, text="Instant English Dictionary", classes="text-4x1 m-2")
        descriptionDiv = jp.Div(a=mainDiv, text="Get the definiton of any English word instantly as you type."
                                , classes="text-lg")

        input_grid = jp.Div(a=mainDiv, classes="grid grid-cols-2")
        output_div = jp.Div(a=mainDiv, classes="m-2 p-2 text-lg border-2 h-40")
        input_box = jp.Input(a=input_grid, placeholder="Type in a word here....", output = output_div,
                             classes="m-2 bg-gray-100 rounded w-64 focus:bg-white focus:outline-none "
                                     "focus:border-purple-500"
                                     "py-2 px-4")
        input_box.on('input', cls.get_definition)


        #input_button = jp.Button(a=input_grid, text="get definition",
         #                       classes="border-3 text-gray-500",
          #                       click=cls.get_definition,
           #                      outputdiv=output_div,
            #                     inputbox = input_box)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        widget.output.text = "".join(Definition(widget.value).get())
