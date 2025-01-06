# Import necessary libraries for Selenium, WebDriver management, data storage (pandas), and time delays
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# Configure Chrome driver service (replace with path to your chromedriver.exe) - This sets the path to the ChromeDriver executable
service = Service(executable_path="")  
driver = webdriver.Chrome(service=service)

# Open Cookie Clicker website and set user agent for better compatibility - This opens the Cookie Clicker website and sets a user agent string to mimic a real browser
driver.get("https://orteil.dashnet.org/cookieclicker/")

options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
options.add_experimental_option("detach", True)  # Keep browser window open after script execution - This keeps the browser window open after the script finishes running

# Define element IDs for easier reference later in the code - These variables store the IDs of specific elements on the Cookie Clicker website for easier reference
cookie_id = "bigCookie"
language_id = "langSelect-EN"
cookies_id = "cookies"  # This seems like a typo, it should probably be "cookie" to get the cookie count
product_price_prefix = "productPrice"
product_prefix = "product"

# Wait for language selection element to be present and click it (assuming it starts the game) - This waits for the language selection element to appear and then clicks it, assuming this starts the game
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, language_id))
)

language_select = driver.find_element(By.ID, language_id)
language_select.click()

# Wait for the cookie element to be present and then click it repeatedly - This waits for the cookie element to appear and then clicks it repeatedly in a loop
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)
while True:
    cookie.click()

    # Get cookie count, split text, remove commas, and convert to integer - This retrieves the cookie count element, extracts the text, removes commas, and converts it to an integer
    cookie_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]  # Fix typo, use "cookies_id" if intended
    cookie_count = int(cookie_count.replace(",", ""))

    # Loop through the first four products - This loop iterates through the first four products on the page
    for i in range(4):
        # Get product price element, remove commas, and convert to integer (handle non-digits) - This retrieves the price element for the current product, removes commas, and converts it to an integer, handling cases where the price is not a number
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        # Check if cookie count is enough and buy the product if so - This checks if the player has enough cookies to afford the product and clicks on it if they do
        if cookie_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break  # Exit the inner loop after buying a product

    # Introduce a sleep time (adjust as needed, might violate game rules) - This pauses the script for 10 seconds. You should adjust this sleep time as needed and be aware that using automated scripts might violate the game's rules