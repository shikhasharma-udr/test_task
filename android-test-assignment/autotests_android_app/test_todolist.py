from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy as MobileBy
import unittest

class ToDoListTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8.1',  # API level 27
            'deviceName': 'Android Emulator',  # Or your device name
            'appPackage': 'com.example.thesurgeonstodolist',  # Update with your app's package name
            'appActivity': '.MainActivity',  # Update with your app's main activity
            'automationName': 'UiAutomator2'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    
    def tearDown(self):
        self.driver.quit()

    def test_create_new_item(self):
        add_button = self.driver.find_element(MobileBy.ID, "com.example.thesurgeonstodolist:id/add_button")
        add_button.click()

        item_input = self.driver.find_element(MobileBy.ID, "com.example.thesurgeonstodolist:id/item_input")
        item_input.send_keys("New Item")

        confirm_button = self.driver.find_element(MobileBy.ID, "com.example.thesurgeonstodolist:id/confirm_button")
        confirm_button.click()

        # Verify the item is added
        new_item = self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='New Item']")
        self.assertIsNotNone(new_item)

        
    def test_create_new_item_with_priority(self):
        self.test_create_new_item()  # You could create a separate method for adding with priority if different

        priority_spinner = self.driver.find_element(MobileBy.ID, "com.example.thesurgeonstodolist:id/priority_spinner")
        priority_spinner.click()
        # Select priority (assuming it's a dropdown or similar UI element)
        high_priority = self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='High']")
        high_priority.click()
        
        confirm_button = self.driver.find_element(MobileBy.ID, "com.example.thesurgeonstodolist:id/confirm_button")
        confirm_button.click()
        
        # Verify the item with high priority is added
        high_priority_item = self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='High Priority Item']")
        self.assertIsNotNone(high_priority_item)

    def test_delete_specific_item(self):
        item_to_delete = self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='Item to Delete']")
        item_to_delete.click()

        delete_button = self.driver.find_element(MobileBy.ID, "com.example.thesurgeonstodolist:id/delete_button")
        delete_button.click()

        # Verify the item is deleted
        deleted_item = self.driver.find_elements(MobileBy.XPATH, "//android.widget.TextView[@text='Item to Delete']")
        self.assertEqual(len(deleted_item), 0)

    def test_delete_all_items(self):
        settings_button = self.driver.find_element(MobileBy.ID, "com.example.thesurgeonstodolist:id/settings_button")
        settings_button.click()

        delete_all_button = self.driver.find_element(MobileBy.ID, "com.example.thesurgeonstodolist:id/delete_all_button")
        delete_all_button.click()

        # Verify all items are deleted
        items = self.driver.find_elements(MobileBy.XPATH, "//android.widget.TextView")
        self.assertEqual(len(items), 0)

    def test_change_settings(self):
        settings_button = self.driver.find_element(MobileBy.ID, "com.example.thesurgeonstodolist:id/settings_button")
        settings_button.click()

        theme_switch = self.driver.find_element(MobileBy.ID, "com.example.thesurgeonstodolist:id/theme_switch")
        theme_switch.click()

        # Verify the theme change took effect
        main_layout = self.driver.find_element(MobileBy.ID, "com.example.thesurgeonstodolist:id/main_layout")
        self.assertEqual(main_layout.get_attribute("backgroundColor"), "dark_theme_color")  # Replace with actual check
