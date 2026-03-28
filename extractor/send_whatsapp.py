# import pywhatkit as kit
# import time


# def send_messages(numbers, message):

#     # remove duplicates
#     unique_numbers = sorted(set(numbers))

#     # track already sent numbers
#     sent_numbers = set()

#     for num in unique_numbers:

#         # skip if already sent
#         if num in sent_numbers:
#             continue

#         try:

#             phone = "+91" + str(num)

#             print(f"Sending message to {phone}")

#             kit.sendwhatmsg_instantly(
#                 phone,
#                 message,
#                 wait_time=10,
#                 tab_close=True,
#                 close_time=5
#             )

#             # mark as sent
#             sent_numbers.add(num)

#             # delay before next message
#             time.sleep(7)

#         except Exception as e:

#             print("Error sending message:", num, e)



# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse
import time


def send_messages(numbers, message):

    unique_numbers = sorted(set(numbers))
    sent_numbers = set()

    print("Starting WhatsApp automation...")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.get("https://web.whatsapp.com")

    print("Scan QR Code to login")

    # wait for login
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "side"))
    )

    print("Login successful")

    encoded_message = urllib.parse.quote(message)

    for num in unique_numbers:

        if num in sent_numbers:
            continue

        try:

            phone = "+91" + str(num)

            print(f"Opening chat for {phone}")

            chat_url = f"https://web.whatsapp.com/send?phone={phone}&text={encoded_message}"

            driver.get(chat_url)

            # wait until message box appears
            message_box = WebDriverWait(driver, 40).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                )
            )

            time.sleep(2)

            # press ENTER to send message
            message_box.send_keys(Keys.ENTER)

            print(f"Message sent to {phone}")

            sent_numbers.add(num)

            time.sleep(5)

        except Exception as e:
            print(f"Error sending to {num}: {e}")

    print("All messages processed")

    driver.quit()
