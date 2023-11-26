import justpy as jp


class Home:
    path = "/"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        mainDiv = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        titleDiv = jp.Div(a=mainDiv, text="this the home page", classes="text-4x1 m-2")
        textDiv = jp.Div(a=mainDiv, text="just some text to put on screen", classes="text-lg")
        return wp

