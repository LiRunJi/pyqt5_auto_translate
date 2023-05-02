from setuptools import setup, find_packages

setup(
    name="pyqt5_auto_translate",
    version="0.1.0",
    description="A lightweight and easy-to-use library for automating the translation of PyQt5 widgets.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="RunJi",
    author_email="ryanlee02@foxmail.com",
    url="https://github.com/LiRunJi/pyqt5_auto_translate",
    packages=find_packages(),
    package_data={'pyqt5_auto_translate': ['translations.yml', 'example.ui']},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.6",
    install_requires=[
        'PyYAML>=5.4.1',
        'PyQt5>=5.15.4'
    ],
)
