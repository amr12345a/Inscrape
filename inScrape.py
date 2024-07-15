from selenium import webdriver
import time
import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# By Amr Elkhamisy
# This is a script to scrape your data from Instagram or Facbook, it's a simple script that uses selenium to scrape data from
print("1-Instagram   2-Facebook")
rte = input("Choose 1 or 2: ")
if "1" in str(rte):
    headss = ["Phone", "Name", "User Name", "Actual Bio", "Email", "Gender", "Website",
              "Contact Names", "Contact Numbers", "Follow Requests", "Login Activities",
              "Search History", "Followers", "Following", "Bios", "Blocked", "Ads Interests",
              "Emails Sent", "Login", "Logout", "Password Changes",
              "Date Joined", "Date of Birth", "Date Upgraded", "Former Usernames", "Formers Gmails",
              "Story Poll Votes", "Hashtags you follow", "Former Phones", "Story Bookmarked Music",
              "Former full names", "Former links in bio", "Story emoji slider votes",
              "story question responses", "story countdown follows",
              "story quiz responses", "Account privacy changes", "Apps and Websites", "Emails Sent Others",
              "accounts you hide stories from", "Photos"]
    kilo = 0
    # Filtered Topics
    heads = []
    # Showing topics info var to choose
    info = "Choose From: "
    for sf in headss:
        info += str(kilo) + "- " + sf + "  "
        kilo += 1
    print(info)
    # If it's all, will get all variables, if it's numbers seperated with commas will filter them
    headss_num = input("Choosed Ones (1,6 for example) or type all: ")
    if "all" in headss_num:
        heads = headss
    else:
        for poto in headss_num.split(","):
            print(poto)
            heads.append(headss[int(poto)])

    print(heads)
    # Opening the window
    driver = webdriver.Chrome()
    password_changes = []
    # Asking For email, and password
    email = input("Email or Username: ")
    password = input("Password: ")
    # Defining Variables
    phone = ""
    name = ""
    user_name = ""
    actual_bio = ""
    email_of_mine = ""
    gender = ""
    date_joined = ""
    data_of_birth = ""
    date_upgraded = ""
    contact_names = []
    contact_numbers = []
    follow_requests = []
    logins = []
    search_history = []
    followers = []
    following = []
    story_poll_votes = []
    story_emoji_slider_votes = []
    story_question_responses = []
    story_countdown_follows = []
    story_quiz_responses = []
    hashtags_you_follow = []
    former_phones = []
    manage_access = []
    story_bookmarked_music = []
    accounts_you_hide_stories_from = []
    former_full_names = []
    former_links_in_bio = []
    account_privacy_changes = []
    logouts_date = []
    website = ""
    emails = []
    former_usernames = []
    bios = []
    emails_others = []
    blocked = []
    logins_date = []
    former_emails = []
    ads_interests = []
    photos = []

    row = 1
    if __name__ == '__main__':
        # Variables used:
        # z for list locating
        # as you see each date in a new list there
        # p for list switching
        # and ws for scrolling
        driver.get("https://www.instagram.com/accounts/login/")
        # Time wait (To avoid element not found error)
        time.sleep(10)
        # Adding username and password
        driver.find_element(By.NAME, "username").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        # Clicking on login button
        driver.find_element(By.CSS_SELECTOR, ".L3NKy").click()
        time.sleep(10)
        for fik in heads:
            # Check if one of wanted data from about overview data
            if fik in str(["Phone", "Name", "User Name", "Actual Bio", "Email", "Gender", "Website"]):
                driver.get("https://www.instagram.com/accounts/edit/")
                time.sleep(2)
                # Get info in https://www.instagram.com/accounts/edit/
                if fik == "Name":
                    name += str(driver.find_element_by_id("pepName").get_attribute("value"))
                if fik == "User Name":
                    user_name += str(driver.find_element_by_id("pepUsername").get_attribute("value"))
                if fik in "Phone":
                    phone += str(driver.find_element_by_id("pepPhone Number").get_attribute("value"))
                if fik in "Email":
                    email_of_mine += str(driver.find_element_by_id("pepEmail").get_attribute("value"))
                if fik in "Website":
                    website += str(driver.find_element_by_id("pepWebsite").get_attribute("value"))
                if fik in "Actual Bio":
                    actual_bio += str(driver.find_element_by_id("pepBio").text)
                if fik in "Gender":
                    gender += str(driver.find_element_by_id("pepGender").get_attribute("value"))

            if fik in str(["Date Joined", "Date of Birth", "Date Upgraded"]):
                # Time Delay to be more realistic (avoiding ban) and to ensure site load
                time.sleep(3)
                driver.get("https://www.instagram.com/accounts/access_tool/")

                if fik in "Date Joined":
                    date_joined = str(driver.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/article/main/div/div[1]/section[1]/section[1]/div").text)
                if fik in "Date of Birth":
                    data_of_birth = str(driver.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/article/main/div/div[1]/section[1]/section[6]/div").text)
                if fik in "Date Upgraded":
                    date_upgraded = str(driver.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/article/main/div/div[1]/section[1]/section[7]/div").text)
            if fik in ["Contact Names", "Contact Numbers"]:
                z = 1
                # Opening Contact History
                driver.get("https://www.instagram.com/accounts/contact_history/")
                time.sleep(3)
                while True:
                    try:
                        # Getting Contact History and Add it in a List
                        if fik in "Contact Names":
                            contact_names.append(str(driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/div[1]/div[5]/div[" + str(
                                    z) + "]/div/div[1]/h1").text))
                        if fik in "Contact Numbers":
                            contact_numbers.append(str(driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/div[1]/div[5]/div[" + str(
                                    z) + "]/div/div[2]/h1").text))

                        z += 1
                    except:
                        break

                print(contact_numbers)
                print(contact_names)
            if fik in "Login Activities":
                z = 2
                driver.get("https://www.instagram.com/session/login_activity/")
                # Time Delay to be more realistic (avoiding ban) and to ensure site load
                time.sleep(3)
                while True:
                    try:
                        # Getting Login-s and Add it in a List
                        logi = ""
                        logi += str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/div/div[2]/div[3]/div[" + str(
                                z) + "]/div/div/div[2]/div[1]/div/div").text).replace("\xa0·\xa0", " ").replace(",",
                                                                                                                "") + " "
                        logi += str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/div/div[2]/div[3]/div[" + str(
                                z) + "]/div/div/div[2]/div[2]/div/div").get_attribute("innerText")).replace(
                            "\xa0·\xa0", " ")
                        logins.append(logi)
                        z += 2
                    except:
                        break

                print(logins)

            if fik in "Follow Requests":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/current_follow_requests")
                # Time Delay to be more realistic (avoiding ban) and to ensure site load
                time.sleep(3)
                while True:
                    try:
                        # Getting Follow Requests and Add it in a List
                        follow_requests.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(z) + "]").text))
                        z += 1
                    except:
                        break
            if fik in "Blocked":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/accounts_you_blocked")
                # Time Delay to be more realistic (avoiding ban) and to ensure site load
                time.sleep(3)

                while True:
                    try:
                        # Getting Blocked Accounts and Add it in a List
                        blocked.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(z) + "]").text))
                        z += 1
                    except:
                        break
            if fik in "Search History":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/search_history")
                # Time Delay to be more realistic (avoiding ban) and to ensure site load
                time.sleep(3)

                while True:
                    try:
                        # Getting Search History and Add it in a List
                        search_history.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(z) + "]").text))
                        z += 1
                    except:
                        break

            if fik in "Bios":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/former_bio_texts")
                # Time Delay to be more realistic (avoiding ban) and to ensure site load
                time.sleep(3)

                while True:
                    try:
                        # Getting Bios since account opened and Add it in a List
                        bios.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(z) + "]").text))
                        z += 1
                    except:
                        break
            if fik in "Ads Interests":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/ads_interests")
                # Time Delay to be more realistic (avoiding ban) and to ensure site load
                time.sleep(3)

                while True:
                    try:
                        # Getting Ads Interests and Add it in a List
                        ads_interests.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(z) + "]").text))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Followers":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/accounts_following_you")
                # Time Delay to be more realistic (avoiding ban) and to ensure site load
                time.sleep(3)

                while True:
                    try:
                        # Getting Followers and Add it in a List
                        followers.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(z) + "]").text))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Following":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/accounts_you_follow")
                # Time Delay to be more realistic (avoiding ban) and to ensure site load
                time.sleep(3)

                while True:
                    try:
                        # Getting Following and Add it in a List
                        following.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(z) + "]").text))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in ["Emails Sent", "Emails Sent Others"]:
                z = 2
                driver.get("https://www.instagram.com/emails/emails_sent/")
                # Time Delay to be more realistic (avoiding ban) and to ensure site load
                time.sleep(2)
                while True:
                    try:
                        try:
                            # Getting Emails Sent and Add it in a List
                            if fik == "Emails Sent":
                                emeil = ""
                                emeil += str(driver.find_element_by_xpath(
                                    "/html/body/div[1]/section/main/div/article/div/div[2]/div[2]/div[" + str(
                                        z) + "]/div[2]").text) + " "
                                emails.append(emeil.replace("\\n", ", ").replace(r"\n", ", ").replace("\n", ", "))
                                z += 1
                            else:
                                raise StopIteration
                        except:
                            if fik == "Emails Sent Others":
                                z = 2
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/section/main/div/article/div/div[2]/div[1]/a[2]").click()
                                time.sleep(2)
                                while True:
                                    try:
                                        emeil = ""
                                        emeil += str(driver.find_element_by_xpath(
                                            "/html/body/div[1]/section/main/div/article/div/div[2]/div[2]/div[" + str(
                                                z) + "]/div[2]").text).replace(",", " ")
                                        emails_others.append(emeil.replace("\\n", ", ").replace(r"\n", ", ").replace("\n", ", "))
                                        z += 1
                                    except:
                                        raise StopIteration
                            else:
                                raise StopIteration

                    except StopIteration:
                        break
            if fik in "Login":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/logins")
                # Time Delay to be more realistic (avoiding ban) and to ensure site load
                time.sleep(2)
                while True:
                    try:
                        # Getting logins_date and Add it in a List
                        logins_date.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Logout":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/logouts")
                # Time Delay to be more realistic (avoiding ban) and to ensure site load
                time.sleep(2)
                while True:
                    try:
                        # Getting logouts_date and Add it in a List
                        logouts_date.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Password Changes":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/password_changes")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting Password Changes and Add it in a List
                        password_changes.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Former Usernames":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/former_usernames")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting Former Usernames and Add it in a List
                        former_usernames.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(z) + "]").text))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Formers Gmails":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/former_emails")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting Formers Gmails and Add it in a List
                        former_emails.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(z) + "]").text))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Hashtags you follow":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/hashtags_you_follow")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting Hashtags you follow and Add it in a List
                        hashtags_you_follow.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(z) + "]").text))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Former Phones":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/former_phones")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting Former Phones and Add it in a List
                        former_phones.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(z) + "]").text))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Story Poll Votes":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/story_poll_votes")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting Story Poll Votes and Add it in a List
                        story_poll_votes.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Story emoji slider votes":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/story_emoji_slider_votes")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting Story emoji slider votes and Add it in a List
                        story_emoji_slider_votes.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "story question responses":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/story_question_responses")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting story question responses and Add it in a List
                        story_question_responses.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "story countdown follows":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/story_countdown_follows")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting story countdown follows and Add it in a List
                        story_countdown_follows.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Story Bookmarked Music":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/story_bookmarked_music")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting Story Bookmarked Music and Add it in a List
                        story_bookmarked_music.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "story quiz responses":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/story_quiz_responses")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting story quiz responses and Add it in a List
                        story_quiz_responses.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Former links in bio":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/former_links_in_bio")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting Former links in bio and Add it in a List
                        former_links_in_bio.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Former full names":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/former_full_names")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting Former full names and Add it in a List
                        former_full_names.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "accounts you hide stories from":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/accounts_you_hide_stories_from")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting accounts you hide stories from and Add it in a List
                        accounts_you_hide_stories_from.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Account privacy changes":
                z = 1
                driver.get("https://www.instagram.com/accounts/access_tool/account_privacy_changes")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting Account privacy changes and Add it in a List
                        account_privacy_changes.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break
            if fik in "Apps and Websites":
                z = 1
                driver.get("https://www.instagram.com/accounts/manage_access/")
                time.sleep(2)
                # Time Delay to be more realistic (avoiding ban) and to ensure site load

                while True:
                    try:
                        # Getting Apps and Websites and Add it in a List
                        manage_access.append(str(driver.find_element_by_xpath(
                            "/html/body/div[1]/section/main/div/article/main/section/div[" + str(
                                z) + "]").text).replace(", ", " "))
                        z += 1
                    except:
                        try:
                            # Clicking on view more button to get more for the list
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/section/main/div/article/main/button").click()
                            time.sleep(2)
                            continue
                        except:
                            break

            # Check If data is of Photos, if so, will get the username to get to profile, then get all images of the
            # User, then download it.
            if fik == "Photos":
                t = 0
                driver.get("https://www.instagram.com/accounts/edit/")
                time.sleep(2)
                user = str(driver.find_element_by_id("pepUsername").get_attribute("value"))

                while True:
                    driver.get("https://www.instagram.com/" + user)
                    try:
                        driver.find_elements_by_class_name("_9AhH0")[t].click()
                        time.sleep(3)
                        try:
                            imgs = driver.find_elements_by_class_name("FFVAD")[len(driver.find_elements_by_class_name("FFVAD"))-1]
                            photos.append(imgs.get_attribute("src"))
                        except:
                            pass
                        t += 1
                    except:
                        break

                image = 1
                for ifa in photos:
                    try:
                        img_data = requests.get(ifa).content
                        with open('image' + str(image) + '.jpg', 'wb') as handler:
                            handler.write(img_data)
                        print("Image " + str(image) + " Downloaded")
                        image += 1
                    except Exception as e:
                        print(e)
                        pass

        # Adding data to a data frame
        datas_to_scrape = [phone, name, user_name, actual_bio,
                           email_of_mine, gender, website,
                           str(contact_names).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(contact_numbers).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(follow_requests).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(logins).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(search_history).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(followers).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(following).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(bios).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(blocked).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(ads_interests).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(emails).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(logins_date).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(logouts_date).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(password_changes).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           date_joined, data_of_birth, date_upgraded,
                           str(former_usernames).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(former_emails).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(story_poll_votes).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(hashtags_you_follow).replace("[", "").replace("]", "").replace("'", "").replace(", ",
                                                                                                               "\n"),
                           str(former_phones).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(story_bookmarked_music).replace("[", "").replace("]", "").replace("'", "").replace(", ",
                                                                                                                  "\n"),
                           str(former_full_names).replace("[", "").replace("]", "").replace("'", "").replace(", ",
                                                                                                             "\n"),
                           str(former_links_in_bio).replace("[", "").replace("]", "").replace("'", "").replace(", ",
                                                                                                               "\n"),
                           str(story_emoji_slider_votes).replace("[", "").replace("]", "").replace("'", "").replace(
                               ", ",
                               "\n"),
                           str(story_question_responses).replace("[", "").replace("]", "").replace("'", "").replace(
                               ", ",
                               "\n"),
                           str(story_countdown_follows).replace("[", "").replace("]", "").replace("'", "").replace(", ",
                                                                                                                   "\n"),
                           str(story_quiz_responses).replace("[", "").replace("]", "").replace("'", "").replace(", ",
                                                                                                                "\n"),
                           str(account_privacy_changes).replace("[", "").replace("]", "").replace("'", "").replace(", ",
                                                                                                                   "\n"),
                           str(manage_access).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(emails_others).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(accounts_you_hide_stories_from).replace("[", "").replace("]", "").replace("'",
                                                                                                         "").replace(
                               ", ", "\n"),
                           str(photos).replace("[", "").replace("]", "").replace("'",
                                                                                                         "").replace(
                               ", ", "\n")]

        print(len(datas_to_scrape))
        # List of filtered data
        datas_to_scrape_filtered = []
        # if all get all datas_to_scrape that contains all possible
        if "all" in headss_num:
            datas_to_scrape_filtered = datas_to_scrape
        else:
            # filter unwanted data and add wanted ones
            for poto in headss_num.split(","):
                print(poto)
                datas_to_scrape_filtered.append(datas_to_scrape[int(poto)])

        # put results in results.txt file
        heads_num = 0
        results = open("results_instagram.txt", "w+", encoding="utf8")
        print(datas_to_scrape_filtered)
        for data in datas_to_scrape_filtered:
            print(heads, heads_num)
            results.write("\n\n\n\n########## " + str(heads[heads_num]) + " ##########\n\n")
            results.write(str(data) + "\n")
            heads_num += 1

        results.close()
        driver.close()
else:

    # All Topics To Scrape
    headss = ["Name", "Job", "Education", "Living in", "From", "Relationship", "Mobile", "search", "LIKEDPOSTS",
              "REMOVEDFRIENDS", "FRIENDS", "SENTFRIENDREQUESTS", "RECEIVEDFRIENDREQUESTS", "interests",
              "TAGSBYOTHERSCLUSTER", "WALLCLUSTER", "HIDDENSTORIES", "LIKEDINTERESTS", "following", "LOGINSLOGOUTS",
              "ACTIVESESSIONS", "COMMENTSCLUSTER", "VIDEOWATCH", "GROUPMEMBERSHIP", "STATUSCLUSTER",
              "ARCHIVED", "QUESTIONSCLUSTER", "saved", "saved link", "CREATEDEVENTS", "EVENTRSVPS", "INVITEDEVENTS",
              "MARKETPLACESELLERRESPONSES", "GROUPPOSTS", "CHANGECONTEXTUALPROFILE", "ARCHIVEDSTORIES",
              "NOTECLUSTER", "VIDEOPOLLSVOTED", "YOURPLACES", "VIDEO_SEARCH", "VOICESEARCH",
              "PRIVACYCHECKUPINTERACTION",
              "PRIVACYCHECKUPREMINDER", "RECOGNIZEDDEVICES", "ALLAPPS", "YOURTIMELINEPOSTS",
              "TAGGEDPHOTOS", "TRASH", "primary_location", "Photos", "personal_info_grouping", "Messenger",
              "about_places", "about_contact_and_basic_info", "FRIENDS_PHOTOS", "about_family_and_relationships",
              "about_life_events", "about_details", "about_work_and_education"]

    kilo = 0
    # Filtered Topics
    heads = []
    # Showing topics info var to choose
    info = "Choose From: "
    for sf in headss:
        info += str(kilo) + "- " + sf + "  "
        kilo += 1

    print(info)
    # If it's all, will get all variables, if it's numbers seperated with commas will filter them
    headss_num = input("Choosed Ones (1,6 for example) or type all: ")
    if "all" in headss_num:
        heads = headss
    else:
        for poto in headss_num.split(","):
            print(poto)
            heads.append(headss[int(poto)])

    print(heads)
    # Login Details
    dri = webdriver.Chrome()
    dri.maximize_window()
    email = input("Email: ")
    password = input("Password: ")

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    list11 = []
    list12 = []
    list13 = []
    list14 = []
    list15 = []
    list16 = []
    list17 = []
    list18 = []
    list19 = []
    list20 = []
    list21 = []
    list22 = []
    list23 = []
    list24 = []
    list25 = []
    list26 = []
    list27 = []
    list28 = []
    list29 = []
    list30 = []
    list31 = []
    list32 = []
    list33 = []
    list34 = []
    list35 = []
    list36 = []
    list37 = []
    list38 = []
    list39 = []
    list40 = []
    list41 = []
    list42 = []
    list43 = []
    list45 = []
    list46 = []
    list47 = []
    list48 = []
    list49 = []
    list50 = []
    list51 = []
    list52 = []

    fullname = ""
    work = ""
    edu = ""
    Lives = ""
    he_from = ""
    relation = ""
    mobile = ""
    # Variables used:
    # z for list locating
    # as you see each date in a new list there
    # p for list switching
    # and ws for scrolling
    if __name__ == '__main__':
        # Login Progress
        dri.get("https://www.facebook.com/")
        time.sleep(3)
        dri.find_element_by_id("email").send_keys(email)
        dri.find_element_by_id("pass").send_keys(password)
        dri.find_element_by_name("login").click()
        time.sleep(3)
        # Scraping Data
        for fik in heads:
            # Check if one of wanted data from about overview data
            if fik in str(["Name", "Job", "Education", "Living in", "From", "Relationship", "Mobile"]):
                time.sleep(3)
                dri.get("https://www.facebook.com/profile.php?&sk=about_overview")
                time.sleep(5)


                if fik in "Name":
                    fullname = str(dri.find_element_by_xpath(
                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/span/h1").text)

                if fik in "Job":
                    try:
                        work = str(dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div").text)
                    except:
                        work = ""
                        pass
                if fik in "Education":
                    try:
                        edu = str(dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]").text)
                    except:
                        edu = ""
                        pass
                if fik in "Living in":
                    try:
                        Lives = str(dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div").text)
                    except:
                        Lives = ""
                        pass
                if fik in "From":
                    try:
                        he_from = str(dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div/div[1]/div/div[2]/div").text)
                    except:
                        he_from = ""
                        pass
                if fik in "Relationship":
                    try:
                        relation = str(dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[5]/div/div/div[1]/div/div[2]/div").text)
                    except:
                        relation = ""
                        pass
                if fik in "Mobile":
                    try:
                        mobile = str(dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[6]/div/div/div[1]/div/div[2]/div").text)
                    except:
                        mobile = ""
                        pass

            # Check If data is of search history and scrape it
            if fik == "search":
                z = 2
                p = 2
                ws = 1000
                time.sleep(3)
                dri.get("https://www.facebook.com/*/allactivity/?category_key=search&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]"
                                                      "/div[1]/div[2]/div/div/div/div/div/div[" + str(p) +
                                                      "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/span")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list1.append(datee)
                        list1.append(kt)
                        list1.append(str(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span/span/span/div").text) + " " + str(i.text) + ", ")

                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1

                    except:
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p + 1) + "]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/span")

                            p += 1
                            z = 2
                            pass
                        except:

                            break
            # Check If data is of LIKEDPOSTS and scrape it
            if fik == "LIKEDPOSTS":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=LIKEDPOSTS&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list2.append(datee)
                        list2.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list2.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list2.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list2.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of COMMENTSCLUSTER and scrape it
            if fik == "COMMENTSCLUSTER":
                time.sleep(3)
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=COMMENTSCLUSTER&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list15.append(datee)
                        list15.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list15.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list15.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list15.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of REMOVEDFRIENDS and scrape it
            if fik == "REMOVEDFRIENDS":
                z = 2
                p = 2
                ws = 100
                time.sleep(3)

                dri.get("https://www.facebook.com/*/allactivity?category_key=REMOVEDFRIENDS&entry_point=ayi_hub")
                time.sleep(6)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list3.append(datee)
                        list3.append(kt)
                        list3.append(str(i.text))
                        list3.append(str(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/div[2]/div/span/div").text))


                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list3.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list3.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            try:
                                list3.append(str(i.text) + " " + str(
                                    dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p)
                                        + "]/div[" + str(z)
                                        + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            except:
                                list3.append(" ")
                                pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of FRIENDS and scrape it
            if fik == "FRIENDS":
                z = 2
                p = 2
                ws = 100
                time.sleep(3)
                dri.get("https://www.facebook.com/*/allactivity/?category_key=FRIENDS&entry_point=ayi_hub")
                time.sleep(3)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list4.append(datee)
                        list4.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list4.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list4.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list4.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of FRIENDS_PHOTOS, if so, it will scrape all friends list and download all photos
            if fik == "FRIENDS_PHOTOS":
                z = 2
                p = 2
                ws = 100
                linksss = []
                time.sleep(3)
                dri.get("https://www.facebook.com/*/allactivity/?category_key=FRIENDS&entry_point=ayi_hub")
                time.sleep(3)
                while True:
                    try:

                        linksss.append(str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div[1]/div/a").get_attribute("href")))
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)
                        time.sleep(1)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

                print(linksss)

                for link in linksss:
                    phot = []
                    if "id" in link:
                        dri.get(link + "&sk=photos")
                    else:
                        dri.get(link + "/photos")

                    time.sleep(2)

                    namef = str(dri.find_element_by_xpath(
                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/span/h1").text)
                    os.mkdir(namef)
                    z = 1
                    while True:
                        try:
                            list48.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div[1]/div[" + str(
                                    z) + "]/div/div/a").get_attribute("href")))
                            phot.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div[1]/div[" + str(
                                    z) + "]/div/div/a").get_attribute("href")))
                            z += 1

                        except:
                            break

                    image = 1
                    for ifa in phot:
                        try:
                            dri.get(ifa)
                            time.sleep(3)

                            img = str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/img").get_attribute(
                                "src"))
                            img_data = requests.get(img).content
                            with open(namef + '/image' + str(image) + '.jpg', 'wb') as handler:
                                handler.write(img_data)
                            print("Image " + str(image) + " Downloaded")
                            image += 1
                        except Exception as e:
                            print(e)
                            pass


            # Check If data is of SENTFRIENDREQUESTS and scrape it
            if fik == "SENTFRIENDREQUESTS":
                z = 2
                p = 2
                ws = 100
                time.sleep(3)
                dri.get("https://www.facebook.com/*/allactivity?category_key=SENTFRIENDREQUESTS&entry_point=ayi_hub")
                time.sleep(3)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list5.append(datee)
                        list5.append(kt)
                        list5.append(str(i.text))
                        try:
                            list5.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/div[2]/div/span/div").text))
                        except:
                            pass

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list5.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list5.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            try:
                                list5.append(str(i.text) + " " + str(
                                    dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p)
                                        + "]/div[" + str(z)
                                        + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            except:
                                list5.append(" ")
                                pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of RECEIVEDFRIENDREQUESTS and scrape it
            if fik == "RECEIVEDFRIENDREQUESTS":
                z = 2
                p = 2
                ws = 100
                time.sleep(3)
                dri.get(
                    "https://www.facebook.com/*/allactivity?category_key=RECEIVEDFRIENDREQUESTS&entry_point=ayi_hub")
                time.sleep(3)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list6.append(datee)
                        list6.append(kt)
                        list6.append(str(i.text))
                        try:
                            list6.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/div[2]/div/span/div").text))
                        except:
                            pass

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list6.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list6.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            try:
                                list6.append(str(i.text) + " " + str(
                                    dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p)
                                        + "]/div[" + str(z)
                                        + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            except:
                                list6.append(" ")
                                pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of interests and scrape it
            if fik == "interests":
                z = 1
                time.sleep(3)
                dri.get(
                    "https://www.facebook.com/adpreferences/?section=interests&entry_product=information_about_you")
                time.sleep(10)
                try:
                    dri.find_element_by_xpath(
                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[9]/div").click()
                except:
                    pass
                time.sleep(5)

                while True:
                    try:
                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[8]/div/div[" + str(
                                z) + "]/div/div/div[1]/div/div[1]/div/div/div/span")
                        kt += str(i.text)
                        list7.append(kt)
                        z += 1
                    except:
                        break

            # Check If data is of TAGSBYOTHERSCLUSTER and scrape it
            if fik == "TAGSBYOTHERSCLUSTER":
                z = 2
                p = 2
                ws = 100
                time.sleep(3)
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=TAGSBYOTHERSCLUSTER&entry_point=ayi_hub")
                time.sleep(3)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list8.append(datee)
                        list8.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list8.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list8.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list8.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of WALLCLUSTER and scrape it
            if fik == "WALLCLUSTER":
                z = 2
                p = 2
                ws = 100
                time.sleep(3)
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=WALLCLUSTER&entry_point=ayi_hub")
                time.sleep(3)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list9.append(datee)
                        list9.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list9.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list9.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list9.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of HIDDENSTORIES and scrape it
            if fik == "HIDDENSTORIES":
                z = 2
                p = 2
                ws = 100
                time.sleep(3)
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=HIDDENSTORIES&entry_point=ayi_hub")
                time.sleep(3)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list10.append(datee)
                        list10.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]")
                            list10.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list10.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list10.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of LIKEDINTERESTS and scrape it
            if fik == "LIKEDINTERESTS":
                z = 2
                p = 2
                ws = 100
                time.sleep(3)
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=LIKEDINTERESTS&entry_point=ayi_hub")
                time.sleep(3)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list11.append(datee)
                        list11.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]")
                            list11.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list11.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]").text) + ", ")
                        except:
                            list11.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of following and scrape it
            if fik == "following":
                z = 1
                ws = 100
                dri.get(
                    "https://www.facebook.com/profile.php?&sk=following")
                time.sleep(4)
                while True:
                    try:
                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]"
                            "/div/div/div/div/div/div/div/div/div[3]/div[" + str(
                                z) + "]/div[2]/div/a/span")

                        kt += str(i.text)

                        list12.append(kt)
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800

                        z += 1
                    except:
                        break

            # Check If data is of LOGINSLOGOUTS and scrape it
            if fik == "LOGINSLOGOUTS":
                z = 2
                p = 2
                ws = 100
                time.sleep(3)
                dri.get(
                    "https://www.facebook.com/*/allactivity?category_key=LOGINSLOGOUTS&entry_point=ayi_hub")
                time.sleep(3)
                while True:
                    try:
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span/span/span/div")
                        datee = str(
                            dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]"
                                                      "/div[1]/div[2]/div/div/div/div/div/div[" + str(p) +
                                                      "]/div[1]/div/div/div/div/div/h2/span/span").text)
                        list13.append(datee)
                        kt = ""

                        kt += str(dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div/div/div/div/div[2]/div/div/div/div[2]/span/span").text) + " "
                        kt += str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text)
                        list13.append(str(i.text))
                        list13.append(kt + ", ")
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1

                    except:
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div["
                                + str(
                                    p) + "]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span/span/span/div")

                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of ACTIVESESSIONS and scrape it
            if fik == "ACTIVESESSIONS":
                z = 2
                p = 2
                ws = 100
                time.sleep(3)
                dri.get(
                    "https://www.facebook.com/*/allactivity?category_key=ACTIVESESSIONS&entry_point=ayi_hub")
                time.sleep(3)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]"
                                                      "/div[1]/div[2]/div/div/div/div/div/div[" + str(p) +
                                                      "]/div[1]/div/div/div/div/div/h2/span/span").text) + ", "
                        list14.append(datee)
                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span/span/span/div")
                        kt += str(dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/span").text) + " "
                        kt += str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text)
                        list14.append(str(i.text))
                        list14.append(kt + ", ")
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1

                    except:
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div["
                                + str(
                                    p) + "]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span/span/span/div")

                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of VIDEOWATCH and scrape it
            if fik == "VIDEOWATCH":
                z = 2
                p = 2
                ws = 100
                time.sleep(3)
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=VIDEOWATCH&entry_point=ayi_hub")
                time.sleep(3)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list16.append(datee)
                        list16.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/div[2]/div/span/div")
                            list16.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list16.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list16.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of GROUPMEMBERSHIP and scrape it
            if fik == "GROUPMEMBERSHIP":
                z = 2
                p = 2
                ws = 100
                time.sleep(3)
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=GROUPMEMBERSHIP&entry_point=ayi_hub")
                time.sleep(3)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list17.append(datee)
                        list17.append(kt)
                        list17.append(str(i.text))
                        try:
                            list17.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/div[2]/div/span/div").text))
                        except:
                            pass

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list17.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list17.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            try:
                                list17.append(str(i.text) + " " + str(
                                    dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p)
                                        + "]/div[" + str(z)
                                        + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            except:
                                list17.append(" ")
                                pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of STATUSCLUSTER and scrape it
            if fik == "STATUSCLUSTER":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=STATUSCLUSTER&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list18.append(datee)
                        list18.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list18.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list18.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list18.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of ARCHIVED and scrape it
            if fik == "ARCHIVED":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=ARCHIVED&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]"
                                                      "/div[1]/div[2]/div/div/div/div/div/div[" + str(p) +
                                                      "]/div[1]/div/div/div/div/div/h2/span/span").text)
                        list19.append(datee)
                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/"
                            "div[1]/div/div/div/div[" + str(
                                p)
                            + "]/div[" + str(z)
                            + "]/div[2]/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                        kt += str(i.text)

                        list19.append(kt + str(dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/"
                            "div[1]/div/div/div/div[" + str(
                                p)
                            + "]/div[" + str(z)
                            + "]/div[2]/div[1]/div/a").get_attribute("href")) + ", ")
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800

                        z += 1
                    except:
                        try:
                            try:
                                i = dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/"
                                    "div[1]/div/div/div/div[" + str(
                                        p)
                                    + "]/div[2]/div[2]/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                            except:
                                break


                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of QUESTIONSCLUSTER and scrape it
            if fik == "QUESTIONSCLUSTER":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=QUESTIONSCLUSTER&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        kt = ""
                        i = dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/"
                                                      "div[2]/div/div/div/div/div/div[" + str(p)
                                                      + "]/div[" + str(z)
                                                      + "]/div/div[1]/div/a/div[1]/div[2]"
                                                        "/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list20.append(kt)
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800

                        z += 1
                    except:
                        try:
                            try:
                                i = dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/"
                                    "div[2]/div/div/div/div/div/div[" + str(p)
                                    + "]/div[2]/div/div[1]/div/a/div[1]/div[2]"
                                      "/div/div/div/div[1]/span/span/span/div")
                            except:
                                break

                            datee = str(
                                dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]"
                                                          "/div[1]/div[2]/div/div/div/div/div/div[" + str(p) +
                                                          "]/div[1]/div/div/div/div/div/h2/span/span").text) + ", "
                            list20.append(datee)
                            p += 1
                            z = 2
                            pass
                        except:

                            break
            if "saved" == fik:
                z = 1
                dri.get(
                    "https://www.facebook.com/saved/")
                time.sleep(4)
                ws = 100
                while True:
                    try:
                        kt = ""
                        tk = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div["
                            + str(z) + "]/div/div/div/div[2]/a/span/span")

                        kt += str(i.text) + " "

                        list21.append(kt)
                        bb = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div["
                            + str(z) + "]/div/div/div/div[1]/div/a")

                        tk += str(bb.get_attribute("href")) + " "

                        list22.append(tk)
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800

                        z += 1
                    except:
                        break

            # Check If data is of CREATEDEVENTS and scrape it
            if fik == "CREATEDEVENTS":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=CREATEDEVENTS&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list23.append(datee)
                        list23.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list23.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list23.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list23.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of EVENTRSVPS and scrape it
            if fik == "EVENTRSVPS":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=EVENTRSVPS&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list24.append(datee)
                        list24.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list24.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list24.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list24.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of INVITEDEVENTS and scrape it
            if fik == "INVITEDEVENTS":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=INVITEDEVENTS&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list25.append(datee)
                        list25.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list25.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list25.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list25.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of MARKETPLACESELLERRESPONSES and scrape it
            if fik == "MARKETPLACESELLERRESPONSES":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=MARKETPLACESELLERRESPONSES&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list26.append(datee)
                        list26.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list26.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list26.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list26.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of GROUPPOSTS and scrape it
            if fik == "GROUPPOSTS":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=GROUPPOSTS&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list27.append(datee)
                        list27.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list27.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list27.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list27.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of CHANGECONTEXTUALPROFILE and scrape it
            if fik == "CHANGECONTEXTUALPROFILE":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=CHANGECONTEXTUALPROFILE&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list28.append(datee)
                        list28.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list28.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list28.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list28.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of ARCHIVEDSTORIES and scrape it
            if fik == "ARCHIVEDSTORIES":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=ARCHIVEDSTORIES&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list29.append(datee)
                        list29.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list29.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list29.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list29.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of NOTECLUSTER and scrape it
            if fik == "NOTECLUSTER":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=NOTECLUSTER&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list30.append(datee)
                        list30.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list30.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list30.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list30.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of VIDEOPOLLSVOTED and scrape it
            if fik == "VIDEOPOLLSVOTED":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=VIDEOPOLLSVOTED&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list31.append(datee)
                        list31.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list31.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list31.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list31.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of YOURPLACES and scrape it
            if fik == "YOURPLACES":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=YOURPLACES&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list32.append(datee)
                        list32.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list32.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list32.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list32.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of VIDEO_SEARCH and scrape it
            if fik == "VIDEO_SEARCH":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=VIDEO_SEARCH&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list33.append(datee)
                        list33.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list33.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list33.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list33.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of VOICESEARCH and scrape it
            if fik == "VOICESEARCH":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=VOICESEARCH&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list34.append(datee)
                        list34.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list34.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list34.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list34.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of PRIVACYCHECKUPINTERACTION and scrape it
            if fik == "PRIVACYCHECKUPINTERACTION":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=PRIVACYCHECKUPINTERACTION&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list35.append(datee)
                        list35.append(kt)
                        list35.append(str(i.text))
                        try:
                            list35.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/span").text))
                            list35.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/div[2]").text)+", ")
                        except:
                            pass

                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/span")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of PRIVACYCHECKUPREMINDER and scrape it
            if fik == "PRIVACYCHECKUPREMINDER":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=PRIVACYCHECKUPREMINDER&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list36.append(datee)
                        list36.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list36.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list36.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list36.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of RECOGNIZEDDEVICES and scrape it
            if fik == "RECOGNIZEDDEVICES":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=RECOGNIZEDDEVICES&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list37.append(datee)
                        list37.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list37.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list37.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list37.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of ALLAPPS and scrape it
            if fik == "ALLAPPS":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity/?category_key=ALLAPPS&entry_point=ayi_hub")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list38.append(datee)
                        list38.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list38.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list38.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list38.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of YOURTIMELINEPOSTS and scrape it
            if fik == "YOURTIMELINEPOSTS":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity?activity_history=false&category_key=YOURTIMELINEPOSTS&manage_mode=false")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[1]/div/div/div/div/div/h2/span/span").text)

                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list39.append(datee)
                        list39.append(kt)

                        try:
                            dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div")
                            list39.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + " ")

                            list39.append(str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/div[2]/div/span/div").text).replace(
                                "Public", "Public ") + ", ")
                        except:
                            list39.append(str(i.text) + " " + str(
                                dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p)
                                    + "]/div[" + str(z)
                                    + "]/div/div[1]/div/a").get_attribute("href")) + ", ")
                            pass
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1
                        print(z, ws)

                    except Exception as e:
                        print(e)
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[2]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of TAGGEDPHOTOS and scrape it
            if fik == "TAGGEDPHOTOS":
                z = 2
                p = 2
                ws = 100
                dri.get(
                    "https://www.facebook.com/*/allactivity?activity_history=false&category_key=TAGGEDPHOTOS&manage_mode=false")
                time.sleep(4)
                while True:
                    try:
                        datee = str(
                            dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]"
                                                      "/div[1]/div[2]/div/div/div/div/div/div[" + str(p) +
                                                      "]/div[1]/div/div/div/div/div/h2/span/span").text)
                        list40.append(datee)
                        kt = ""
                        i = dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/"
                                                      "div[2]/div/div/div/div/div/div[" + str(p)
                                                      + "]/div[" + str(z)
                                                      + "]/div/div[1]/div/a/div[1]/div[2]"
                                                        "/div/div/div/div[1]/span/span/span/div")

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                    p)
                                + "]/div[" + str(z)
                                + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/span").text)
                        except:
                            pass

                        list40.append(kt)
                        list40.append(str(i.text) + str(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/"
                                                      "div[2]/div/div/div/div/div/div[" + str(p)
                                                      + "]/div[" + str(z)
                                                      + "]/div/div[1]/div/a").get_attribute("href")) + ", ")

                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800

                        z += 1
                    except:
                        try:
                            try:
                                i = dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/"
                                    "div[2]/div/div/div/div/div/div[" + str(p)
                                    + "]/div[2]/div/div[1]/div/a/div[1]/div[2]"
                                      "/div/div/div/div[1]/span/span/span/div")
                            except:
                                break

                            p += 1
                            z = 2
                            pass
                        except:

                            break

            if fik == "TRASH":
                z = 2
                p = 2
                ws = 100
                time.sleep(3)
                dri.get("https://www.facebook.com/*/allactivity/?category_key=TRASH&entry_point=ayi_hub")
                time.sleep(3)
                while True:
                    try:
                        kt = ""
                        i = dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[" + str(
                                p) + "]/div[" + str(
                                z) + "]/div[2]/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                        try:
                            kt += str(dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[" + str(
                                    p) + "]/div[" + str(
                                    z) + "]/div[2]/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        except:
                            try:
                                kt += str(dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                        p) + "]/div[" + str(
                                        z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                            except:
                                try:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/span/div/div/span/span").text) + " "
                                except:
                                    kt += str(dri.find_element_by_xpath(
                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[" + str(
                                            p) + "]/div[" + str(
                                            z) + "]/div/div[1]/div/a/div[1]/div[2]/div/div/div/div[2]/span/div/div/span/span").text) + " "

                        list42.append(
                            str(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/"
                                                          "div[1]/div[2]/div/div[1]/div/div/div/div[" + str(
                                p) + "]/div[1]/div/div/div/div/div/h2/span/span").text))
                        list42.append(kt)

                        list42.append(str(i.text) + " " + str(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]"
                                                                                        "/div/div[3]/div/div/div["
                                                                                        "1]/div[1]/div[2]/div/div["
                                                                                        "1]/div/div/div/div[" +
                                                                                        str(p) + "]/div[" + str(z)
                                                                                        + "]/div[2]/div[1]/div/a").get_attribute("href"))
                                      + ", ")
                        dri.execute_script("window.scrollTo(0," + str(ws) + ")")
                        ws += 800
                        z += 1

                    except:
                        try:
                            i = dri.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[" + str(
                                    p) + "]/div[2]/div[2]/div[1]/div/a/div[1]/div[2]/div/div/div/div[1]/span/span/span/div")
                            p += 1
                            z = 2
                            pass
                        except:

                            break

            # Check If data is of primary_location and scrape it
            if fik == "primary_location":
                dri.get(
                    "https://www.facebook.com/primary_location/info/")
                time.sleep(4)
                list41.append(str(dri.find_element_by_xpath(
                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/span").text))

            # Check If data is of Photos, if so, it will scrape all photos list and download all photos
            if fik == "Photos":
                dri.get("https://www.facebook.com/profile.php?&sk=photos")
                z = 1
                while True:
                    try:
                        list43.append(str(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div[1]/div["+str(z)+"]/div/div/a").get_attribute("href")))
                        z += 1

                    except:
                        break

                image = 1
                for ifa in list43:
                    try:
                        dri.get(ifa)
                        time.sleep(3)
                        img = str(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/img").get_attribute("src"))
                        img_data = requests.get(img).content
                        with open('image'+str(image)+'.jpg', 'wb') as handler:
                            handler.write(img_data)
                        print("Image "+str(image)+" Downloaded")
                        image += 1
                    except Exception as e:
                        print(e)
                        pass

            # Check If data is of personal_info_grouping and scrape it.
            if fik == "personal_info_grouping":
                dri.get("https://www.facebook.com/your_information/?tab=your_information&tile=personal_info_grouping")
                time.sleep(4)
                try:
                    list45.append(str(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/div[2]/div/div/div/div[3]/span").text))
                except:
                    pass

            # Check If data is of Messenger and scrape all messages from chats, and download all photos.
            # Gets chats from start until program gives unable
            # to get element error (program reached the end of the chats)
            # fif variable that gets each chat row from top to the end.
            # Program get photos only with scontent.xx.fbcdn.net
            if fik == "Messenger":
                image = 1
                dri.get("https://www.facebook.com/messages/t/")
                time.sleep(2)
                time.sleep(3)
                z = 1
                p = 3
                time.sleep(3)
                while True:
                    try:
                        try:
                            dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div["+str(p)+"]/div[1]/div[2]/div/div/div["+str(z)+"]").click()
                            time.sleep(3)
                        except Exception as e:
                            print(e)
                            pass

                        time.sleep(6)
                        w = open("results_messenger.txt", "a+", encoding="utf8")
                        w.write("\n"+"## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##"+"\n")
                        w.write(str(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div["+str(p)+"]/div[1]/div[2]/div/div/div["+str(z)+"]/div[1]/div/a/div/div[2]/div[1]/div/div/div[1]/span/span/span/span").text) + "\n\n\n")
                        w.close()
                        photoss = []
                        linkss = []

                        flf = 1
                        while True:
                            try:
                                fa = dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[" + str(
                                        flf) + "]")
                                actions = ActionChains(dri)
                                actions.move_to_element(fa).perform()
                                if "friends on Facebook" in str(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div[1]").text):
                                    break
                            except Exception as e:
                                print(e)
                                break

                        flf = 1
                        time.sleep(2)
                        while True:
                            try:
                                try:
                                    actions = ActionChains(dri)
                                    actions.move_to_element(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div[3]/div["+str(flf)+"]/div/div/div[2]/div[2]/div[1]")).perform()
                                except:
                                    pass
                                w = open("results_messenger.txt", "a+", encoding="utf8")
                                fa = dri.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div/div/div[3]/div[" + str(
                                        flf) + "]")
                                w.write(str(fa.text).replace(
                                    "Enter", "").partition("Write to")[0] + "\n")

                                for fs in fa.find_elements_by_tag_name("a"):
                                    linkss.append(str(fs.get_attribute("href")) + "\n")

                                for fs in fa.find_elements_by_tag_name("img"):
                                    if "scontent.xx.fbcdn.net" in str(fs.get_attribute("src")):
                                        photoss.append(str(fs.get_attribute("src")))

                                w.close()
                                flf += 1
                            except Exception as e:
                                print(e)
                                break
                        z += 1
                        w = open("results_messenger.txt", "a+", encoding="utf8")
                        w.write("\n" + "## Links ##" + "\n")
                        w.close()
                        for ff in linkss:
                            w = open("results_messenger.txt", "a+", encoding="utf8")
                            w.write(ff + "\n")
                            w.close()

                        w = open("results_messenger.txt", "a+", encoding="utf8")
                        w.write("\n" + "## Photos ##" + "\n")
                        w.close()

                        for ff in photoss:
                            w = open("results_messenger.txt", "a+", encoding="utf8")
                            w.write(ff + "\n")
                            w.close()
                            img_data = requests.get(ff).content
                            with open('image' + str(image) + '.jpg', 'wb') as handler:
                                handler.write(img_data)
                            print("Image " + str(image) + " Downloaded")
                            image += 1

                        w = open("results_messenger.txt", "a+", encoding="utf8")
                        w.write("\n\n\n\n\n")
                        w.close()

                        actions = ActionChains(dri)
                        actions.move_to_element(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div["+str(p)+"]/div[1]/div[2]/div/div/div["+str(z)+"]")).perform()


                    except Exception as e:
                        try:
                            dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div["+str(p+1)+"]/div[1]/div[2]/div/div/div["+str(z)+"]")
                            print(e)
                            p += 1
                            pass
                        except:
                            print(e)
                            break

            # Check If data is of about_places and scrape it
            if fik == "about_places":
                dri.get("https://www.facebook.com/profile.php?&sk=about_places")
                time.sleep(3)
                fsa = 3
                while True:
                    try:
                        list46.append(str(dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[" + str(
                                fsa) + "]/div/div/div[1]/div/div[2]/div[1]/a").text))
                        list46.append(str(dri.find_element_by_xpath(
                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[" + str(
                                fsa) + "]/div/div/div[1]/div/div[2]/div[2]").text))
                        list46.append(", ")
                        fsa += 1
                    except:
                        break

            # Check If data is of about_contact_and_basic_info and scrape it
            if fik == "about_contact_and_basic_info":
                dri.get("https://www.facebook.com/profile.php?&sk=about_contact_and_basic_info")
                time.sleep(3)
                try:
                    list47.append(str(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]").text).replace('\\n', ', '))
                except Exception as e:
                    print(e)
                    pass

            if fik == "about_family_and_relationships":
                dri.get("https://www.facebook.com/profile.php?&sk=about_family_and_relationships")
                time.sleep(3)
                try:
                    list49.append(str(dri.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]").text).replace('\\n', ', '))
                except Exception as e:
                    print(e)
                    pass

            if fik == "about_life_events":
                dri.get("https://www.facebook.com/profile.php?&sk=about_life_events")
                time.sleep(3)
                fsa = 3
                try:
                    list50.append(str(dri.find_element_by_xpath(
                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]").text).replace(
                        '\\n', ', '))
                except Exception as e:
                    print(e)
                    pass

            if fik == "about_details":
                dri.get("https://www.facebook.com/profile.php?id=100054807167102&sk=about_details")
                time.sleep(3)
                fsa = 3
                try:
                    list51.append(str(dri.find_element_by_xpath(
                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]").text).replace(
                        '\\n', ', '))
                except Exception as e:
                    print(e)
                    pass

            if fik == "about_work_and_education":
                dri.get("https://www.facebook.com/profile.php?id=100054807167102&sk=about_work_and_education")
                time.sleep(3)
                fsa = 3
                try:
                    list52.append(str(dri.find_element_by_xpath(
                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]").text).replace(
                        '\\n', ', '))
                except Exception as e:
                    print(e)
                    pass

        # List of all possible data
        datas_to_scrape = [fullname, work, edu, Lives, he_from, relation, mobile,
                           str(list1).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n").replace(
                               '"',
                               ""),
                           str(list2).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n").replace('"', ""),
                           str(list3).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list4).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list5).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list6).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list7).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list8).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list9).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list10).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list11).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list12).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list13).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list14).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list15).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list16).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list17).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list18).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list19).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list20).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list21).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list22).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list23).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list24).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list25).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list26).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list27).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list28).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list29).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list30).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list31).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list32).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list33).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list34).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list35).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list36).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list37).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list38).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list39).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list40).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list42).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list41).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list43).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list45).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           "in results_messenger.txt file",
                           str(list46).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list47).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n").replace("\\n", "\n").replace(r"\n", "\n"),
                           str(list48).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n"),
                           str(list49).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n").replace("\\n", "\n").replace(r"\n", "\n"),
                           str(list50).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n").replace("\\n", "\n").replace(r"\n", "\n"),
                           str(list51).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n").replace("\\n", "\n").replace(r"\n", "\n"),
                           str(list52).replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n").replace("\\n", "\n").replace(r"\n", "\n")]
        print(len(datas_to_scrape))
        # List of filtered data
        datas_to_scrape_filtered = []
        # if all get all datas_to_scrape that contains all possible
        if "all" in headss_num:
            datas_to_scrape_filtered = datas_to_scrape
        else:
            # filter unwanted data and add wanted ones
            for poto in headss_num.split(","):
                print(poto)
                datas_to_scrape_filtered.append(datas_to_scrape[int(poto)])

        # put results in results.txt file
        heads_num = 0
        results = open("results_facebook.txt", "w+", encoding="utf8")
        print(datas_to_scrape_filtered)
        for data in datas_to_scrape_filtered:
            print(heads, heads_num)
            results.write("\n\n\n\n########## " + str(heads[heads_num]) + " ##########\n\n")
            results.write(str(data) + "\n")
            heads_num += 1

        results.close()  # Close txt the file
        dri.close()  # Close Driver Time
        # Code Done
