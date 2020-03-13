# OSS-translator

This project uses selenium webdriver with help of ['googletrans'](https://pypi.org/project/googletrans) to translate strings for various oss project

It works very good for majority of strings. For dynamic strings however you will need to review it and manually edit parts of it.

Eg of dynamic strings.

    "%s has expired"

## Installation:

You will need python 3.4+ and selenium webdriver for firefox in your system path. If you use chrome get [chromedriver](http://chromedriver.chromium.org/downloads/) and add it to your system path.

```
git clone https://github.com/hemanta212/oss-translator.git
cd oss-translator
poetry install
poetry run python translator.py
```

## Usage

Go to hosted.webplate.org and navigate to project translate page. copy the url

Go to cmdline then type

```
python translate.py [url] [from] [to] [firefox or chrome]
```

Eg. If I need to contribute to a newpipe project to translate from english to nepali language in my firefox browser then.
The url will be [newpip project hosted webplate](https://hosted.weblate.org/translate/newpipe/strings/ne/?q=state%3A%3Ctranslated&offset=4)

Then,

```
python translate.py "https://hosted.weblate.org/translate/newpipe/strings/ne/?q=state%3A%3Ctranslated&offset=4" english nepali firefox
```

Note: 
* You may need to activate virtualenv if you use one or for poetry user user poetry run python instead of python.
* Do not forget the apostropes around url


* You will get 40 seconds to sign into the website.
* After 40 seconds the url will be redirected to the one you entered 
* Everything will be then done automatically.
