from googletrans import Translator


class Translate:

    def __init__(self):
        self.translator = Translator()

    def ru_en(self, text):
        return self.translator.translate(text, dest='en').text

    def en_ru(self, text):
        return self.translator.translate(text, dest='ru').text


if __name__ == '__main__':

    en_text = 'Hello World!'
    ru_text = 'Привет мир!'

    print(Translate().en_ru(text=en_text))
    print(Translate().ru_en(text=ru_text))
