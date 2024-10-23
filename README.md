# Automated WhatsApp Business Chat Scraper & Contact Organizer

## Project Overview
This project is a Python-based automation tool that extracts customer phone numbers from archived chats in WhatsApp Business, removes duplicates, and saves them in a structured format. The extracted contacts are then converted into a vCard (VCF) file, allowing easy import of hundreds of contacts in just one click.

The automation leverages Selenium to access and scroll through the archived chats, ensuring all relevant data is gathered and saved without any manual intervention.

## Features
- Automates WhatsApp Web session for scraping archived chats.
- Extracts unsaved customer phone numbers from chats using regular expressions.
- Filters duplicates to ensure each contact is saved only once.
- Saves phone numbers into a text file for backup.
- Converts the text file into a vCard (.vcf) format for easy import to mobile contacts.

## Challenges Solved
1. **Session Persistence:** The script maintains the current session to avoid repeated QR code scanning every time it runs.
2. **Chat Filtering:** Extracts data only from archived chats, preventing it from mixing with the main chat.
3. **Chat Loading:** Handles dynamic loading of chats by scrolling through the chat list and fetching data incrementally.

## Prerequisites

### Libraries
- **Selenium** for browser automation: `pip install selenium`
- **OS** and **Datetime** (built-in Python libraries)

### Chrome Version
- **Google Chrome (for developers) v130.0.6723.69**
  Download link: [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)
  
- **ChromeDriver** version `130.0.6723.69`, compatible with the above Chrome version.

### Chrome Setup
Make sure to adjust the Chrome paths in the script:
- Path to **Chrome executable** (in the `Options` setup):
  ```
  chrome_options.binary_location = r'D:\chrome-win64\chrome-win64\chrome.exe'
  ```
- Path to **ChromeDriver**:
  ```
  chrome_service = Service(executable_path=r'D:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
  ```

## Setup Instructions

1. **Clone the repository** to your local machine:
   ```
   git clone https://github.com/yourusername/whatsapp-scraper.git
   ```

2. **Install the required dependencies**:
   ```bash
   pip install selenium
   ```

3. **Download and set up Chrome for Testing** (v130.0.6723.69) and ChromeDriver:
   - Ensure both are installed and paths are correctly set in the script.

4. **Run the script**:
   - Open the terminal and execute the Python script:
     ```bash
     python whatsapp_scraper.py
     ```

5. **WhatsApp Web Login**:
   - The script will open WhatsApp Web. You need to scan the QR code once. After that, the session will persist.

6. **Extract Contacts**:
   - The script will automatically scrape the archived chats, extract phone numbers, save them to a text file, and convert them into a vCard (.vcf) file.

7. **Import Contacts**:
   - Once the vCard is created, simply transfer it to your phone and import the contacts with a single click.

## Example Usage

After running the script:
- **Text file with phone numbers**: `Phone_numbers_dd-mm-yyyy_hh-mm-ss.txt`
- **VCF file**: `customers.vcf`

You can use this vCard file to bulk import contacts to your mobile device.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
