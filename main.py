# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import webbrowser

from selenium import webdriver


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    browser = webdriver.Firefox()
    browser.get(
        'http://10.152.4.9:9081/cas/login?service=http%3A%2F%2F10.152.4.9%3A9081%2Fsso%2FtsysLoginController.do%3Fmethod%3Dindex')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
