from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigating to the Youtube homepage
driver.get("https://www.youtube.com")
time.sleep(5)

# Finding the search bar and entering text
search_bar = driver.find_element("xpath", "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
search_bar.send_keys("Software testing")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "Software testing - YouTube" in driver.title

# Selecting a video from the search results
video_link = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-search-pyv-renderer/div/ytd-ad-slot-renderer/div/ytd-in-feed-ad-layout-renderer/div/ytd-promoted-video-renderer/div/div/div[1]/a")
video_link.click()

# Waiting for the video details page to load
time.sleep(5)

# Click on Channel Link below the video player
channel_link = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a")
channel_link.click()

# Waiting for the popup to open
time.sleep(5)

# Clicking on minimize button
playlist_button = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[4]/div/div[1]")
playlist_button.click()
time.sleep(2)

# Clicking on profile button
signIn_button = driver.find_element("xpath", "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")
signIn_button.click()
time.sleep(2)

driver.close()



