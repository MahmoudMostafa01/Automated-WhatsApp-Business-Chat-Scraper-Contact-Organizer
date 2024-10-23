from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import re
import os
from datetime import datetime  # Import to get today's date

# Specify the path to the testing Chrome executable
chrome_options = Options()
chrome_options.binary_location = r'D:\chrome-win64\chrome-win64\chrome.exe'
chrome_options.add_argument("--user-data-dir=C:\\Users\\Mahmoud Mostafa\\AppData\\Local\\Google\\Chrome for Testing\\User Data")
chrome_options.add_argument("--profile-directory=Default")  # Adjust to your profile (usually "Default" if it's the main profile)

# Disable sandbox mode to avoid permission issues
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--remote-debugging-port=9222")

# Create a service object for ChromeDriver
chrome_service = Service(executable_path=r'D:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')

# Initialize the WebDriver with the Chrome options and service
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for user to scan the QR code
input("Press Enter after scanning QR code")

# Wait for chats to load
wait = WebDriverWait(driver, 60)
try:
    # Access archived chats
    archived_chats_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pane-side"]/button/div/div[2]/div/div')))
    archived_chats_button.click()
    time.sleep(5)  # Wait for archived chats to load

    # Now we are inside the archived chat pane
    # Make sure to select the chat elements only from this section
    archived_chat_pane = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div')))

       # Initialize a variable to track new chats
    phone_numbers = []
    last_scroll_position = 0

    while True:
        # Extract chat elements from the archived chat pane only
        chat_elements = archived_chat_pane.find_elements(By.CSS_SELECTOR, "._ak8q")
        print(f"Number of archived chats found: {len(chat_elements)}")

        # Extract phone numbers from chat elements
        for chat in chat_elements:
            chat_text = chat.text
            found_numbers = re.findall(r'\+\d{1,4}\s?\d{2,4}\s?\d{1,15}\s?\d{0,15}', chat_text)
            if found_numbers:
                for number in found_numbers:
                    if number not in phone_numbers:
                        phone_numbers.append(number)

        # Scroll down the archived chat pane by a fixed step (e.g., 1000 pixels)
        driver.execute_script("arguments[0].scrollTop += 500", archived_chat_pane)

        # Wait for 5 seconds to allow chats to load
        time.sleep(5)

        # Check if the scroll position has changed (to detect the end of the list)
        new_scroll_position = driver.execute_script("return arguments[0].scrollTop", archived_chat_pane)
        if new_scroll_position == last_scroll_position:
            # Break the loop if the scroll position does not change (end of chats)
            print("Reached the bottom of the chat list, no more chats to load.")
            break

        last_scroll_position = new_scroll_position

except Exception as e:
    print(f"Error loading chat elements: {e}")
# Close the browser
driver.quit()

print("Phone numbers extracted:", phone_numbers)
print("Length of array:", len(phone_numbers))

# Specify the desired directory path
directory = r"C:\Users\Mahmoud Mostafa\OneDrive\Desktop"  # Change this to your desired path

# Save the extracted phone numbers into a text file with today's date and time in the filename
now = datetime.now()
today_date = now.strftime('%d-%m-%Y')  # Get today's date in YYYY-MM-DD format
timestamp = now.strftime('%H-%M-%S')  # Get current time in HH-MM-SS format
filename = os.path.join(directory, f"Phone_numbers_{today_date}_{timestamp}.txt")

# Write the phone numbers to the file
with open(filename, 'w') as file:
    for number in phone_numbers:
        file.write(number + '\n')

print(f"Phone numbers saved to {filename}")

time.sleep(5)

# Read phone numbers from a text file
with open(f'{filename}', 'r') as file:
    phone_numbers = [line.strip().replace(" ", "") for line in file if line.strip()]  # Remove spaces and empty lines

# Debug: Print the number of phone numbers read
print(f"Number of phone numbers read: {len(phone_numbers)}")

# Create a VCF file from the phone numbers
with open('C:\\Users\\Mahmoud Mostafa\\OneDrive\\Desktop\\customers.vcf', 'w') as file:
    for i, number in enumerate(phone_numbers, start=1):
        customer_name = f"Customer {i}"
        file.write(f"BEGIN:VCARD\n")
        file.write(f"VERSION:3.0\n")
        file.write(f"N:{customer_name};;;\n")
        file.write(f"FN:{customer_name}\n")
        file.write(f"TEL;TYPE=CELL:{number}\n")
        file.write(f"END:VCARD\n")

print("VCF file has been created successfully!")

