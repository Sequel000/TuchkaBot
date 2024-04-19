from googletrans import Translator

# Класс для перевода текста
class Translate:
    # Создаем переменную содежащую класс библиотеки google translate
    def __init__(self):
        self.translator = Translator()
    # Функция перевода с "русского" на "английский"
    def ru_en(self, text):
        return self.translator.translate(text, dest='en').text
    # Функция перевода с "английского" на "русский"
    def en_ru(self, text):
        return self.translator.translate(text, dest='ru').text


if __name__ == '__main__':

    en_text = 'Hello World!'
    ru_text = 'Привет мир!'

    print(Translate().en_ru(text=en_text))
    print(Translate().ru_en(text=ru_text))
