# PyQt5 Auto Translate

[中文](README-zh.md)

`pyqt5_auto_translate` is an automatic translation library for PyQt5, which allows you to easily add multi-language support to your PyQt5 programs with minimal modification to your existing code and without the need for additional toolchains.

## Installation

Install using pip:

```bash
pip install pyqt5_auto_translate
```

## Currently Supported Translated Components

| Original Component | Translated Component  |
| ------------------ | --------------------- |
| QLabel             | TranslatedQLabel      |
| QPushButton        | TranslatedQPushButton |
| QCheckBox          | TranslatedQCheckBox   |
| QMenu              | TranslatedQMenu       |
| QAction            | TranslatedQAction     |

## Example

### Translating the Python Code Interface

Here is an example code without integrated translation:

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QProgressBar, QSlider, QLCDNumber, QGroupBox
)
class ExampleUI(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.title_label = QLabel("Example UI")
        self.layout.addWidget(self.title_label)
        self.hbox_layout = QHBoxLayout()
        self.layout.addLayout(self.hbox_layout)
        self.hbox_layout.addWidget(QLabel("Username: "))
        self.username_input = QLineEdit()
        self.hbox_layout.addWidget(self.username_input)
        self.hbox_layout2 = QHBoxLayout()
        self.layout.addLayout(self.hbox_layout2)
        self.hbox_layout2.addWidget(QLabel("Password: "))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.hbox_layout2.addWidget(self.password_input)
        self.submit_button = QPushButton("Submit")
        self.layout.addWidget(self.submit_button)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.layout.addWidget(self.progress_bar)
        self.slider = QSlider(Qt.Horizontal)
        self.layout.addWidget(self.slider)
        self.lcd_number = QLCDNumber()
        self.lcd_number.setSegmentStyle(QLCDNumber.Flat)
        self.layout.addWidget(self.lcd_number)
        self.group_box = QGroupBox("Options")
        self.group_box_layout = QVBoxLayout()
        self.group_box.setLayout(self.group_box_layout)
        self.checkbox1 = QPushButton("Option 1")
        self.checkbox2 = QPushButton("Option 2")
        self.checkbox3 = QPushButton("Option 3")
        self.group_box_layout.addWidget(self.checkbox1)
        self.group_box_layout.addWidget(self.checkbox2)
        self.group_box_layout.addWidget(self.checkbox3)
        self.layout.addWidget(self.group_box)
        self.setLayout(self.layout)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = ExampleUI()
    window.setCentralWidget(ui)
    window.show()
    sys.exit(app.exec_())
```

To enable translation support, only a few lines of code are needed, and there's no need to modify the original code. Here is the modified code that supports translation:

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QProgressBar, QSlider, QLCDNumber, QGroupBox
)
# 
from pyqt5_auto_translate import \
    TranslatedQLabel as QLabel, \
    TranslatedQPushButton as QPushButton, translater, \
    ExampleTranslateMenuBar

translater.set_translation_file('translations.yml')


class ExampleUI(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.title_label = QLabel("Example UI")
        self.layout.addWidget(self.title_label)
        self.hbox_layout = QHBoxLayout()
        self.layout.addLayout(self.hbox_layout)
        self.hbox_layout.addWidget(QLabel("Username: "))
        self.username_input = QLineEdit()
        self.hbox_layout.addWidget(self.username_input)
        self.hbox_layout2 = QHBoxLayout()
        self.layout.addLayout(self.hbox_layout2)
        self.hbox_layout2.addWidget(QLabel("Password: "))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.hbox_layout2.addWidget(self.password_input)
        self.submit_button = QPushButton("Submit")
        self.layout.addWidget(self.submit_button)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.layout.addWidget(self.progress_bar)
        self.slider = QSlider(Qt.Horizontal)
        self.layout.addWidget(self.slider)
        self.lcd_number = QLCDNumber()
        self.lcd_number.setSegmentStyle(QLCDNumber.Flat)
        self.layout.addWidget(self.lcd_number)
        self.group_box = QGroupBox("Options")
        self.group_box_layout = QVBoxLayout()
        self.group_box.setLayout(self.group_box_layout)
        self.checkbox1 = QPushButton("Option 1")
        self.checkbox2 = QPushButton("Option 2")
        self.checkbox3 = QPushButton("Option 3")
        self.group_box_layout.addWidget(self.checkbox1)
        self.group_box_layout.addWidget(self.checkbox2)
        self.group_box_layout.addWidget(self.checkbox3)
        self.layout.addWidget(self.group_box)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setMenuBar(ExampleTranslateMenuBar())  # add the translated MenuBar

    ui = ExampleUI()
    window.setCentralWidget(ui)
    window.show()
    sys.exit(app.exec_())

```



```
from pyqt5_auto_translate import \
    TranslatedQLabel as QLabel, \
    TranslatedQPushButton as QPushButton, translater, \
    ExampleTranslateMenuBar

translater.set_translation_file('translations.yml')

    window.setMenuBar(ExampleTranslateMenuBar())  # add the translated MenuBar
```

Translation file:

```yaml
#translations.yml
supported_languages:
  - en
  - zh-CN
  - zh-TW

translations:
  en:
    en: English
    zh-CN: 英语
    zh-TW: 英語
  zh-CN:
    en: Simplified Chinese
    zh-CN: 简体中文
    zh-TW: 簡體中文
  zh-TW:
    en: Traditional Chinese
    zh-CN: 繁体中文
    zh-TW: 繁體中文
  language:
    en: language
    zh-CN: 语言
    zh-TW: 語言
  Language:
    en: Language
    zh-CN: 语言
    zh-TW: 語言
  Options:
    en: Options
    zh-CN: 选项
    zh-TW: 選項

  Option 1:
    en: Option 1
    zh-CN: 选项1
    zh-TW: 選項1

  Option 2:
    en: Option 2
    zh-CN: 选项2
    zh-TW: 選項2

  Option 3:
    en: Option 3
    zh-CN: 选项3
    zh-TW: 選項3

  'Password: ':
    en: Password
    zh-CN: 密码
    zh-TW: 密碼

  Submit:
    en: Submit
    zh-CN: 提交
    zh-TW: 提交

  Example UI:
    en: Example UI
    zh-CN: 示例界面
    zh-TW: 範例介面

  'Username: ':
    en: Username
    zh-CN: 用户名
    zh-TW: 使用者名稱
```



### Translating UI

Here is an example code without integrated translation:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

app = QApplication(sys.argv)

main_window = QMainWindow()

load_ui_with_translation('example.ui', main_window)
main_window.show()

sys.exit(app.exec_())
```

Here is an example code with integrated translation:

```python
from pyqt5_auto_translate import ExampleTranslateMenuBar,load_ui_with_translation #here changed
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

main_window = QMainWindow()

load_ui_with_translation('example.ui', main_window)#here changed
main_window.setMenuBar(ExampleTranslateMenuBar()) #here changed
main_window.show()

sys.exit(app.exec_())
```

In the code with integrated translation, the `ExampleTranslateMenuBar()` is added to provide a translated menu bar. Also, the `load_ui_with_translation` function is imported from `pyqt5_auto_translate`.

## Contribution

If you find any errors or would like to improve this library, please feel free to raise issues or pull requests. We welcome your contributions!