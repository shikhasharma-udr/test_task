from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class HomePage(BasePage):
    # TODO : better way to access the search bar, which is not working at the moment as its inside shadow dom.
    # need more time and efforts to research on how to access these components.
    #SEARCH_BOX = (By.NAME, "q")    
    #LOGIN_BUTTON = (By.LINK_TEXT, "Log In")

    def search_subreddit(self, subreddit_name):
        print(subreddit_name)
        #Approach 1: 
        #login_button = self.wait_for_element(self.LOGIN_BUTTON)
        #print(login_button.id)
        #login_button.click()
        #Approach 2:
        my_elements = self.driver.find_elements(By.TAG_NAME, 'faceplate-search-input')
        for search_box in my_elements:
           print(search_box.get_attribute("outerHTML"))
           #search_box.send_keys("value",subreddit_name)  
           #search_box.click()       
           #ssearch_box.submit()
           #break
  
