import yaml
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QActionGroup, QAction, QMenu
from PyQt5.QtCore import pyqtSignal, QObject
import os
from PyQt5.uic import loadUi


class Translater(QObject):
    language_changed_signal = pyqtSignal()

    def __init__(self):
        super(Translater, self).__init__()
        self.global_lang = None
        self.global_languages = None
        self.global_translations = None
        self.file_path = None

    def set_translation_file(self, file_path):
        self.file_path = file_path
        self.load_translations()

    def load_translations(self):
        self.global_translations = self.load_translations_file(self.file_path)["translations"]
        self.global_languages = self.load_translations_file(self.file_path)["supported_languages"]
        self.global_lang = self.global_languages[0]

    def load_translations_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def get_translation(self, key, lang, translations):
        if key:
            if self.file_path:
                if key in translations:
                    if lang in translations[key]:
                        return translations[key][lang]
                    else:
                        print(f"\033[91mLanguage '{lang}' not found for key '{key}'.\033[0m")
                        return key
                else:
                    print(f"\033[91mKey '{key}' not found.\033[0m")
                    return key
            else:

                self.file_path = os.path.join(os.path.dirname(__file__), 'translations.yml')

                self.load_translations()
                print(
                    f'\033[91mWarning: You haven\'t provide your translation file yet, using the default translation file.\033[0m')  # raise Exception("TranslaterFileNotProvidedError")
                return self.get_translation(key, lang, self.global_translations)


translater = Translater()


class TranslatedQPushButton(QPushButton):
    def __init__(self, key=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        translater.language_changed_signal.connect(self.language_changed)
        self.key = None
        if key is not None:
            self.setText(key)

    def setText(self, key):
        self.key = key
        text = translater.get_translation(key, translater.global_lang, translater.global_translations)
        super().setText(text)

    def language_changed(self):
        if self.key:
            self.setText(self.key)


class TranslatedQLabel(QLabel):
    def __init__(self, key=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        translater.language_changed_signal.connect(self.language_changed)
        self.key = None
        if key is not None:
            self.setText(key)

    def setText(self, key, second=None):
        self.key = key
        text = translater.get_translation(key, translater.global_lang, translater.global_translations)
        if second is not None:
            text = text + ": " + second
        super().setText(text)

    def language_changed(self):
        if self.key:
            self.setText(self.key)


class TranslatedQCheckBox(QCheckBox):
    def __init__(self, key=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        translater.language_changed_signal.connect(self.language_changed)
        self.key = None
        if key is not None:
            self.setText(key)

    def setText(self, key):
        self.key = key
        text = translater.get_translation(key, translater.global_lang, translater.global_translations)
        super().setText(text)

    def language_changed(self):
        if self.key:
            self.setText(self.key)


class TranslatedQMessageBox(QMessageBox):
    def __init__(self, key=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        translater.language_changed_signal.connect(self.language_changed)
        self.key = None
        if key is not None:
            self.setText(key)

    def setText(self, key):
        self.key = key
        text = translater.get_translation(key, translater.global_lang, translater.global_translations)
        super().setText(text)

    def setWindowTitle(self, title):
        self.title = title
        text = translater.get_translation(title, translater.global_lang, translater.global_translations)
        super().setWindowTitle(text)

    def language_changed(self):
        if self.key:
            self.setText(self.key)
        if self.title:
            self.setWindowTitle(self.title)


class TranslatedQMenu(QMenu):
    def __init__(self, title=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        translater.language_changed_signal.connect(self.language_changed)
        self.title = title

        if title:
            self.setWindowTitle(title)

    def setWindowTitle(self, title):
        self.title = title
        text = translater.get_translation(title, translater.global_lang, translater.global_translations)
        super().setTitle(text)

    def language_changed(self):
        if self.title:
            self.setWindowTitle(self.title)


class TranslatedQAction(QAction):
    def __init__(self, key=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        translater.language_changed_signal.connect(self.language_changed)
        self.key = None
        if key is not None:
            self.key = key
            self.setText(key)

    def setText(self, key):
        self.key = key
        text = translater.get_translation(key, translater.global_lang, translater.global_translations)
        super().setText(text)

    def language_changed(self):
        if self.key:
            self.setText(self.key)


class AutoTranslatedQMenu(TranslatedQMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_menu_bar()

    def init_menu_bar(self):
        language_group = QActionGroup(self)
        language_group.setExclusive(True)

        for lang_name in translater.global_languages:
            language_action = TranslatedQAction(lang_name, self, checkable=True)
            language_action.triggered.connect(
                lambda checked, l=lang_name: self.on_language_changed(l) if checked else None)
            self.addAction(language_action)
            language_group.addAction(language_action)

        self.actions()[0].setChecked(True)

    def on_language_changed(self, lang):
        translater.global_lang = lang
        translater.language_changed_signal.emit()


class ExampleTranslateMenuBar(QMenuBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_menu_bar()

    def init_menu_bar(self):
        self.language_menu = AutoTranslatedQMenu("Language", self)
        self.addMenu(self.language_menu)


def translate_widget(widget):
    if isinstance(widget, QLabel):
        return TranslatedQLabel(widget.text(), parent=widget.parent())
    elif isinstance(widget, QPushButton):
        return TranslatedQPushButton(widget.text(), parent=widget.parent())
    elif isinstance(widget, QCheckBox):
        return TranslatedQCheckBox(widget.text(), parent=widget.parent())
    elif isinstance(widget, QMenu):
        return TranslatedQMenu(widget.title(), parent=widget.parent())
    elif isinstance(widget, QAction):
        return TranslatedQAction(widget.text(), parent=widget.parent())
    else:
        return widget


def translate_ui_widgets(parent_widget):
    for child_widget in parent_widget.findChildren(QWidget):
        new_widget = translate_widget(child_widget)
        if new_widget != child_widget:
            child_widget.setParent(None)
            new_widget.setGeometry(child_widget.geometry())
            new_widget.setObjectName(child_widget.objectName())


def load_ui_with_translation(ui_file_path, parent=None):
    widget = loadUi(ui_file_path, parent)
    translate_ui_widgets(widget)
    return widget


def run_example():
    class MainWidget(QWidget):
        def __init__(self, *args, **kwargs):
            super(MainWidget, self).__init__(*args, **kwargs)
            self.layout = QVBoxLayout()
            self.language_button = TranslatedQPushButton()
            self.language_button.setText('language')
            self.layout.addWidget(self.language_button)
            hbox1 = QHBoxLayout()
            button1 = TranslatedQPushButton('button')
            hbox1.addWidget(button1)
            button2 = TranslatedQPushButton('button')
            hbox1.addWidget(button2)
            self.layout.addLayout(hbox1)
            hbox2 = QHBoxLayout()
            label1 = TranslatedQLabel()
            label1.setText('label')
            hbox2.addWidget(label1)
            checkbox1 = TranslatedQCheckBox()
            checkbox1.setText('checkbox')
            hbox2.addWidget(checkbox1)
            self.layout.addLayout(hbox2)
            self.setLayout(self.layout)

    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)

    main_window = QMainWindow()
    main_widget = MainWidget()
    main_window.setCentralWidget(main_widget)
    menu_bar = QMenuBar()
    main_window.setMenuBar(menu_bar)
    file_menu = TranslatedQMenu('file')
    file_menu.addMenu(AutoTranslatedQMenu('Language'))
    menu_bar.addMenu(file_menu)
    edit_menu = TranslatedQMenu('edit_menu')
    menu_bar.addMenu(edit_menu)
    main_window.show()
    sys.exit(app.exec_())


def run_ui_example():
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.uic import loadUi

    app = QApplication(sys.argv)

    main_window = QMainWindow()

    load_ui_with_translation(os.path.join(os.path.dirname(__file__), 'example.ui'), main_window)
    main_window.setMenuBar(ExampleTranslateMenuBar())
    main_window.show()

    sys.exit(app.exec_())

# if __name__ == '__main__':
#     run_example()
#     run_ui_example()
