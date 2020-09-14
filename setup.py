from setuptools import setup
import translator

setup(
    name = translator.__name__,
    description = translator.__description__,
    version = translator.__version__,
    author = translator.__author__,
    url = translator.__url__,
    license = translator.__license__,
    packages = ['translator'],
    entry_points  = {
            'console_scripts': [
                'yoda = translator.__main__:translate'
            ]
        },
    install_requires = translator.__dependencies__
)
