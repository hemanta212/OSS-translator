import sys
import time
import googletrans
from selenium import webdriver

args = sys.argv[1:]
print(args)

if len(args) < 4:
    print("Usage: python translator.py [url] [from] [to] [chrome or firefox]")
    sys.exit()
else:
    hosted_weblate_url = args[0]

# Init browser
if 'firefox' in args:
    browser = webdriver.Firefox()
else:
    browser = webdriver.Chrome()

def start():
    browser.get(hosted_weblate_url)
    # Sign in time for user
    time.sleep(40)
    browser.get(hosted_weblate_url)

def fill():
    eng_text = browser.find_element_by_class_name('list-group-item-text')
    print(eng_text.text, type(eng_text))

    transaltor = googletrans.Translator()
    translated_text = transaltor.translate(eng_text.text, args[2], args[1])
    translation_texfield = browser.find_element_by_class_name('translation-editor')
    translation_texfield.send_keys(translated_text.text)
    submit_button = browser.find_element_by_name('save')
    submit_button.click()
    time.sleep(1)
    fill()

def main():
    try:
        start()
        fill()
    except Exception as E:
        print("ERROR:", E)
        browser.close()
    else:
        browser.close()

if __name__ == '__main__':
    main()
