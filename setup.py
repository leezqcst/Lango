from setuptools import find_packages, setup

setup(
    name='Lango',
    version='0.20.1',
    description='Natural Language Framework for Matching Parse Trees and Modeling Conversation',
    packages=find_packages(),
    author='Michael Young',
    author_email='michaelyoung1995@gmail.com',
    url='https://github.com/ayoungprogrammer/lango',
    scripts=[],
    install_requires=[
        'nltk',
        'pycorenlp'
    ],
)
