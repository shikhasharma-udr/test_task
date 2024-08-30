from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.subreddit_page import SubredditPage
from selenium import webdriver
import pytest

# Load scenarios
scenarios('../features/reddit.feature')

@given('the user is on the Reddit homepage')
def user_on_homepage(browser):
    browser.get('https://www.reddit.com/')
    return HomePage(browser)

@when('the user searches for "gaming"')
def search_gaming_subreddit(user_on_homepage):
    user_on_homepage.search_subreddit("gaming")

@then('the user opens the subreddit "gaming"')
def open_gaming_subreddit(browser):
    subreddit_page = SubredditPage(browser)
    subreddit_page.open_top_post()

@then('the user prints out the top most posts title')
def print_top_post_title(browser):
     subreddit_page = SubredditPage(browser)
     subreddit_page.open_top_post()

@then('the user performs login with username <Username> and password <Password>')
def user_logs_in(browser):
    subreddit_page = SubredditPage(browser)
    subreddit_page.login()

@then('the user downvotes the second post if its upvoted, upvotes otherwise')
def vote_on_second_post(browser):
    subreddit_page = SubredditPage(browser)
    subreddit_page.vote_on_second_post()
