from PyQt5.QtGui import QFontDatabase

from definitions import ROOT_DIR


def get_styles(filename: str) -> str:
    return open(f'{ROOT_DIR}\\resources\\styles\\{filename}.qss').read()


def load_fonts():
    fonts = (
        'Montserrat-Regular.ttf',
        'Montserrat-Italic.ttf',
        'Montserrat-Medium.ttf',
        'Montserrat-SemiBold.ttf',
        'Montserrat-Bold.ttf'
    )

    for i in fonts:
        QFontDatabase().addApplicationFont(f'resources/fonts/{i}')
