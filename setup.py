from setuptools import setup, find_packages

setup(
    name='Sentia',
    version='0.1',
    packages=find_packages(),
    install_requires=['flair','re','pandas','pdfplumber','duckduckgo_search','urllib3','googlesearch','requests','bs4'],
    author='Harshvardhan Jadhav',
    author_email='jadhavharshvardhan6301@gmail.com',
    description='Information extraction reconnaissance purposes with relational searches for deep searching, encompasses ML and AI models to aid in insights, produce sentiments, entities and relations on searches data *In development*',
    url='https://github.com/Harshj6301/Sentia',
)
