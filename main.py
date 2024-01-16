import pyautogui
from time import sleep
from pyautogui import ImageNotFoundException





def openning_youtube(url):
    browser = pyautogui.locateCenterOnScreen('images/firefox_image.png', confidence=0.9)

    pyautogui.moveTo(browser)
    pyautogui.click()
    sleep(2)
    pyautogui.hotkey('ctrl', 't')
    sleep(1)
    pyautogui.write(url)
    pyautogui.hotkey('enter')
    sleep(1.5)


def subcribing(channel_name):
    #searching for youtube channel
    pressing_button('search_button.png')
    
    pyautogui.write(channel_name)
    pyautogui.hotkey('enter')
    sleep(2)

    #raising exception if u didnt find the channel
    try:
        pressing_button('subscribe_button.png')
    except ImageNotFoundException as e:
        print(f'Could not find channel: {channel_name}')
        

    

def pressing_button(image_button):
    #function for pressing button
    image_location = pyautogui.locateCenterOnScreen(f'images/{image_button}', confidence=0.9)
    pyautogui.moveTo(image_location)
    pyautogui.click()
    sleep(0.5)


def main():
    channel_name = pyautogui.prompt(text='netflix', title='Enter channel name to which u wanna subcribe: ')
    url = 'https://www.youtube.com/'
    openning_youtube(url)
    subcribing(channel_name)

if __name__ == '__main__':
    main()

