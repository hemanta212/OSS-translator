import sys
import time
import googletrans
from selenium import webdriver


def main():
    args = get_terminal_input()
    validate_the_args(args)
    url, orig_lang, dest_lang, browser_name = args

    try:
        browser = setup_browser(browser_name)
        navigate_and_pause_for_login(browser, url)
        fill_and_save_recursively(browser, orig_lang, dest_lang)
    except Exception as E:
        print("ERROR:", E)
        browser.close()
    else:
        browser.close()


def get_terminal_input():
    # First one is filename itself so slice it
    args = sys.argv[1:]
    print("GOT ARGS:", args)
    return args


def validate_the_args(args):
    if len(args) != 4:
        throw_error_and_exit()


def throw_error_and_exit():
    message = "Usage: python translator.py " "[url] [from] [to] [chrome or firefox]"
    print(message)
    sys.exit()


def setup_browser(browser_name):
    if browser_name == "firefox":
        browser = webdriver.Firefox()
    elif browser_name == "chrome":
        browser = webdriver.Chrome()
    return browser


def navigate_and_pause_for_login(browser, url):
    browser.get(url)
    time.sleep(40)
    browser.get(url)


def fill_and_save_recursively(browser, orig_lang, dest_lang):
    orig_text = get_original_text(browser)
    raw_translated_text = translate(orig_text, orig_lang, dest_lang)
    translated_text = sanitize(raw_translated_text)
    fill_and_submit(browser, translated_text)
    fill_and_save_recursively(browser, orig_lang, dest_lang)


def get_original_text(browser):
    text_field = browser.find_element_by_class_name("list-group-item-text")
    print("Got source string:", text_field.text)
    return text_field.text


def translate(orig_text, orig_lang, dest_lang):
    transaltor = googletrans.Translator()
    translated_text = transaltor.translate(orig_text, dest_lang, orig_lang).text
    print("Translated:", translated_text)
    return translated_text


def sanitize(raw_translated_text):
    raw_lines = raw_translated_text.split("\n")
    processed_lines = [process(line) for line in raw_lines if line.strip()]
    field_text = "\n".join(processed_lines)
    return field_text


def fill_and_submit(browser, translated_text):
    translation_texfield = browser.find_element_by_class_name("translation-editor")
    print("found editing field", translation_texfield)
    print("translated text is ", translated_text)
    translation_texfield.send_keys(translated_text)
    submit_button = browser.find_element_by_name("save")
    print("found submit field", translation_texfield)
    submit_button.click()


def process(line):
    text = line.replace("% $ S", " %$s ").replace("% $ s", " %$s ")
    text = text.replace("% S", " %s ").replace("% s", " %s ")
    text = text.replace("  ", " ")
    print("Processed Text:", text)
    return text


if __name__ == "__main__":
    main()
