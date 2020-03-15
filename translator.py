import sys
import time
import googletrans
from selenium import webdriver


def main():
    args = get_terminal_input()
    validate_the_args()
    url, orig_lang, dest_lang, browser = args
    try:
        setup_browser(browser)
        navigate_and_pause_for_login(url)
        fill_and_save_recursively(browser, orig_lang, dest_lang)
    except Exception as E:
        print("ERROR:", E)
        browser.close()
    else:
        browser.close()


def get_terminal_input():
    # First one is filename itself so slice it
    return sys.argv[1:]


def validate_the_args():
    if len(args) != 4:
        throw_error_and_exit()


def throw_error_and_exit():
    message = "Usage: python translator.py " "[url] [from] [to] [chrome or firefox]"
    sys.exit()


def setup_browser(args):
    if "firefox" in args:
        browser = webdriver.Firefox()
    elif "chrome" in args:
        browser = webdriver.Chrome()


def navigate_and_pause_for_login(url):
    browser.get(url)
    time.sleep(40)
    browser.get(url)


def fill_and_save_recursively(browser, orig_lang, dest_lang):
    eng_text = get_english_text(browser)
    raw_translated_text = translate(eng_text, orig_lang, dest_lang)
    translated_text = sanitize(raw_translated_text)
    fill_and_submit(browser, translated_text)
    fill_and_save_recursively(browser, orig_lang, dest_lang)


def get_english_text(browser):
    text_field = browser.find_element_by_class_name("list-group-item-text")
    print("Got source string:", text_field.text, type(eng_text))
    return text_field.text


def translate(eng_text, orig_lang, dest_lang):
    transaltor = googletrans.Translator()
    translated_text = transaltor.translate(eng_text, dest_lang, orig_lang).text
    print("Translated:", translated_text)
    return translated_text


def sanitize(raw_translated_text):
    raw_lines = text.split("\n")
    processed_lines = [process(line) for line in lines if line.strip()]
    field_text = "\n".join(processed_lines)


def fill_and_submit(browser, translated_text):
    translation_texfield = browser.find_element_by_class_name("translation-editor")
    translation_texfield.send_keys(translated_text)
    submit_button = browser.find_element_by_name("save")
    submit_button.click()


def process(text):
    text = text.replace("% $ S", " %$s ").replace("% $ s", " %$s ")
    text = text.replace("% S", " %s ").replace("% s", " %s ")
    text = text.replace("  ", " ")
    return text


if __name__ == "__main__":
    main()
