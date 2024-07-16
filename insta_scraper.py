import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variables used:
# z for list locating
# as you see each date in a new list there
# p for list switching
# and ws for scrolling
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

# Defining Variables


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
emails = []
former_usernames = []
bios = []
emails_others = []
blocked = []
logins_date = []
former_emails = []
ads_interests = []
photos = []
password_changes = []


# Main Function
def get_kilo():
    kilo = 0
    # Showing topics info var to choose
    info = "Choose From: "
    for sf in headss:
        info += str(kilo) + "- " + sf + "  "
        kilo += 1
    print(info)
    return kilo


def get_heads():
    heads = []
    # If it's all, will get all variables, if it's numbers seperated with commas will filter them
    headss_num = input("Choosed Ones (1,6 for example) or type all: ")
    if "all" in headss_num:
        heads = headss
    else:
        for poto in headss_num.split(","):
            print(poto)
            heads.append(headss[int(poto)])

    print(heads)
    return heads, headss_num


def main():
    global kilo, heads, headss_num
    kilo = get_kilo()
    heads, headss_num = get_heads()

    # Opening the window
    # TODO use undected_chrome driver to avoid getting block on users accounts + use english languge just we may need to use in Xpath
    driver = webdriver.Chrome()
    # Asking For email, and password
    email = input("Email or Username: ")
    password = input("Password: ")
    scraper(driver, email, password)


def scraper(driver, email, password):
    phone = ""
    name = ""
    user_name = ""
    actual_bio = ""
    email_of_mine = ""
    gender = ""
    date_joined = ""
    data_of_birth = ""
    date_upgraded = ""
    website = ""

    driver.get("https://www.instagram.com/accounts/login/")
    # Time wait (To avoid element not found error)
    time.sleep(10)
    # Adding username and password
    driver.find_element(By.NAME, "username").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    # Clicking on login button
    driver.find_element(By.CSS_SELECTOR, '#loginForm [type="submit"]').click()
    # TODO find make the login function and make it call itself in case of wrong password and email or at least show error message
    time.sleep(10)
    for fik in heads:
        # TODO replace this with a better pythonic way to get the data

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

        elif fik in str(["Date Joined", "Date of Birth", "Date Upgraded"]):
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
        elif fik in ["Contact Names", "Contact Numbers"]:
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
        elif fik in "Login Activities":
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

        elif fik in "Follow Requests":
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
        elif fik in "Blocked":
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
        elif fik in "Search History":
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

        elif fik in "Bios":
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
        elif fik in "Ads Interests":
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
        elif fik in "Followers":
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
        elif fik in "Following":
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
        elif fik in ["Emails Sent", "Emails Sent Others"]:
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
                                    emails_others.append(
                                        emeil.replace("\\n", ", ").replace(r"\n", ", ").replace("\n", ", "))
                                    z += 1
                                except:
                                    raise StopIteration
                        else:
                            raise StopIteration

                except StopIteration:
                    break
        elif fik in "Login":
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
        elif fik in "Logout":
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
        elif fik in "Password Changes":
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
        elif fik in "Former Usernames":
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
        elif fik in "Formers Gmails":
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
        elif fik in "Hashtags you follow":
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
        elif fik in "Former Phones":
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
        elif fik in "Story Poll Votes":
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
        elif fik in "Story emoji slider votes":
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
        elif fik in "story question responses":
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
        elif fik in "story countdown follows":
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
        elif fik in "Story Bookmarked Music":
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
        elif fik in "story quiz responses":
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
        elif fik in "Former links in bio":
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
        elif fik in "Former full names":
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
        elif fik in "accounts you hide stories from":
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
        elif fik in "Account privacy changes":
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
        elif fik in "Apps and Websites":
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
        elif fik == "Photos":
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
                        imgs = driver.find_elements_by_class_name("FFVAD")[
                            len(driver.find_elements_by_class_name("FFVAD")) - 1]
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
