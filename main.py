from selenium import webdriver
from time import sleep
from credentials import *
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
# Author Yassine Ahmed Ali
                

class FbBot:
    def __init__(self, nmessage):
        self.message = nmessage
        op = webdriver.ChromeOptions()
        op.add_argument("headless")
        self.driver = webdriver.Chrome(options=op)
        result = self.driver.get(
            "https://www.messenger.com/t/user-id")
        self.driver.find_element_by_name("email").send_keys(username)
        self.driver.find_element_by_name("pass").send_keys(password)
        self.driver.find_element_by_id(
            "loginbutton").click()
        element = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div")
        element.send_keys(self.message)
        element.send_keys(Keys.ENTER)
        html = self.driver.page_source
        soup = BeautifulSoup(html, features="html.parser")
        messages = soup.find_all("span")
        x = len(messages)
        self.last_message_1 = str(messages[x-1]).replace("<span>", "").replace("</span>", "")  
       

class CommandLine:
    def __init__(self):
        self.running = True
        self.main()

    def main(self):
        while self.running:
            self.message = input("> ")
            if self.message.lower() == "help":
                print('''
- 'last message': shows you the last message in your conversation
- 'send: <message>': allows you to send messages. 
                      ''')
            elif 'send:' in self.message.lower() and self.message.lower()[0] == "s":
                new_message = self.message.split(":")
                FbBot(new_message[1])
            elif self.message.lower() == "quit":
                self.running = False
            elif self.message.lower() == "last message":
                print("The last message in the conversation is: " + FbBot("").last_message_1)
            else:
                print("Unknown command, type 'help'")
      
                
CommandLine()
