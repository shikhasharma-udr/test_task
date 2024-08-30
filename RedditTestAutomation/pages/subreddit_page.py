from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
from selenium.webdriver.common.keys import Keys

class SubredditPage(BasePage):
    FIRST_POST_TITLE = (By.TAG_NAME, "article")    
    LOGIN_BUTTON = (By.LINK_TEXT, "Log In")
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")   
    USERNAME = 'username'
    PASSWORD = 'password'

    def open_top_post(self):
        my_elements = self.driver.find_elements(By.TAG_NAME, "article")
        for my_element in my_elements:
           #print(search_box.get_attribute("outerHTML"))           
           print(my_element.text)
           # break from here as we only need to access first article here
           break
        # Another approach could be :
        # print(my_elements[1].text)

    def login(self):
        # Access login button on the page
        login_button = self.wait_for_element(self.LOGIN_BUTTON)
        # Click on the login button
        login_button.click()
        # access username field
        user_field = self.wait_for_element(self.USERNAME_FIELD)
        # send user name input
        user_field.send_keys(self.USERNAME)
        # access password field
        pwd_field = self.wait_for_element(self.PASSWORD_FIELD)
        # send password input
        pwd_field.send_keys(self.PASSWORD)
        # send the enter key to initiate login
        pwd_field.send_keys(Keys.RETURN)
        time.sleep(2)

    def vote_on_second_post(self):   
        # access the second post on the page             
        second_post = self.driver.find_element(By.XPATH,".//*[@id='main-content']/shreddit-feed/article[2]/shreddit-post")
        # try to read the shadow_root element 
        #scp = self.driver.execute_script('document.querySelector("button[class='' group button flex justify-center aspect-square p-0 border-0 button-secondary disabled:text-interactive-content-disabled button-plain  inline-flex items-center hover:text-action-upvote focus-visible:text-action-upvote'']")')
        #shadow_root_element = self.driver.execute_script(scp, second_post)      
        #print(shadow_root_element.text)
        # try to read the children
        #third = self.driver.execute_script('return arguments[0].shadowRoot', shadow_root_element)
        # Since the upvote and downvote components are in shadow dom , the buttons are not accessible by xpath.
        # need mroe time to research on how to access these.
        # the approach could be :
        # second_post = self.driver.find_element(self.SECOND_POST)
        # upvote = second_post.find_element(self.UPVOTE_BUTTON)
        # downvote = second_post.find_element(self.DOWNVOTE_BUTTON)

        # if "upvoted" in upvote.get_attribute("class"):
        #     downvote.click()
        # else:
        #     upvote.click()

