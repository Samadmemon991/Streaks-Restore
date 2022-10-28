from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def friends():
    friends = input("Insert your friends usernames , separated\n")
    friendsArray = friends.split(",")
    friendsArray = list(map(str.strip, friendsArray))
    return friendsArray


def getInfo():
    f = open("info.txt", "r")
    info = []
    for line in f:
        info.append(line.split(':')[1].strip());
    print(info)
    return info;

info = getInfo()
print("streaks will be restored based on above information.")
friends = friends()
driver = webdriver.Chrome()
driver.maximize_window()
success_url = "https://support.snapchat.com/en-US/success"

for item in friends:

    driver.get("https://support.snapchat.com/en-US/i-need-help")
    driver.implicitly_wait(3)

    try:
        radio = driver.find_elements(By.CLASS_NAME, 'sc-radio-circle')
        radio[3].click()

        username = driver.find_element(
            By.XPATH, ("//input[@id='field-24281229']"))
        username.click()
        username.send_keys(info[0])

        email = driver.find_element(
            By.XPATH, ("//input[@id='field-24335325']"))
        email.click()
        email.send_keys(info[1])

        phone = driver.find_element(
            By.XPATH, ("//input[@id='field-24369716']"))
        phone.click()
        phone.send_keys(info[2])

        device = driver.find_element(
            By.XPATH, ("//input[@id='field-24369726']"))
        device.click()
        device.send_keys(info[3])

        friend_username = driver.find_element(
            By.XPATH, ("//input[@id='field-24369736']"))
        friend_username.click()
        friend_username.send_keys(item)

        when = driver.find_element(By.XPATH, ("//input[@id='field-24326423']"))
        when.click()
        when.send_keys("Today")

        streak = driver.find_element(
            By.XPATH, ("//input[@id='field-24641746']"))
        streak.click()
        streak.send_keys("9999")

        icon = driver.find_element(
            By.XPATH, ("//div[@class='ui dropdown selection']"))
        icon.click()
        no = driver.find_element(
            By.XPATH, ("//div[@data-value='hourglass-no']"))
        no.click()

        description = driver.find_element(
            By.XPATH, ("//textarea[@id='field-22808619']"))
        description.click()
        description.send_keys("I lost my snap streaks")

        result = WebDriverWait(driver, 120).until(
            lambda driver: driver.current_url == success_url, "Submission failure for "+item+": Timeout for reCaptcha is 120 sec")

        if result:
            print("Successfully submitted lost streaks form for "+item)

    except Exception as e:
        print(str(e))

driver.close()
