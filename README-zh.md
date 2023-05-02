# PyQt5 Auto Translate 

[English](README.md)

`pyqt5_auto_translate` 是一个用于 PyQt5 的自动翻译库，使您可以轻松地在 PyQt5 程序中实现多语言支持。您可以在几乎不修改原有代码并且不需要安装额外工具链的情况下增加多语言翻译支持。

 ## 安装 

使用 pip 安装： 

```bash
pip install pyqt5_auto_translate
```

## 目前支持翻译的组件

| 原始组件    | 支持翻译的组件        |
| ----------- | --------------------- |
| QLabel      | TranslatedQLabel      |
| QPushButton | TranslatedQPushButton |
| QCheckBox   | TranslatedQCheckBox   |
| QMenu       | TranslatedQMenu       |
| QAction     | TranslatedQAction     |

## 示例

### Python代码界面的翻译

这里是一个没有集成翻译的代码:

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

增加几行代码以支持翻译:

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



仅仅增加了这些就可以让原本的代码支持翻译功能, 并且可以在自定义的文件中自定义翻译的内容:

```

from pyqt5_auto_translate import \
    TranslatedQLabel as QLabel, \
    TranslatedQPushButton as QPushButton, translater, \
    ExampleTranslateMenuBar

translater.set_translation_file('translations.yml')

    window.setMenuBar(ExampleTranslateMenuBar())  # add the translated MenuBar
```

编写的翻译文件:

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



### UI界面的翻译

这里是一个没有集成翻译的代码:

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

增加几行代码以支持翻译:

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

对比:

```python
from pyqt5_auto_translate import ExampleTranslateMenuBar,load_ui_with_translation
load_ui_with_translation('example.ui', main_window)#here changed
main_window.setMenuBar(ExampleTranslateMenuBar())
```

## 贡献

如果您发现了任何错误或想要改进此库，请随时提出问题或拉取请求。我们欢迎您的贡献！