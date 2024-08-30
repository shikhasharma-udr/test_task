Feature: Reddit automation script
    Scenario: Search for a subreddit and interact with posts
    Given the user is on the Reddit homepage
    When the user searches for "gaming"
    Then the user opens the subreddit "gaming"
    Then the user prints out the top most posts title
    Then the user performs login with username <Username> and password <Password>
    Then the user downvotes the second post if its upvoted, upvotes otherwise
