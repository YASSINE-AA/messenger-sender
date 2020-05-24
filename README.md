# messenger-sender
This application uses BeautifulSoup and Selenium to send messenger messages and view the last message in a conversation.

### Setting it up:
First, you need to install selenium.

If you're on windows:
```
pip install selenium
```
If you're on linux or mac:
```
pip3 install selenium
```
Next, you need to download Chrome's webdriver from [this](https://sites.google.com/a/chromium.org/chromedriver/downloads) site.

After downloading the appropriate compressed archive file, you'll want to extract that to a folder and follow these steps:

For windows: simply click on the .exe file and it'll magically work.

For Linux: just execute these commands (make sure you're in the same directory as the file)
```
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

You'll also need to install BeautifulSoup:

If you're on windows:
```
pip install python-bs4
```
If you're on linux or mac:
```
pip3 install python-bs4
```

Happy Coding!
