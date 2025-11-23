from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Setup Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Install and setup ChromeDriver
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path), options=options)

# Open Salesforce login page
driver.get("https://test.salesforce.com")
driver.maximize_window()

# Salesforce login credentials
USERNAME = "corbint@genentech.crm.sqa"
PASSWORD = "Gene2024!"

try:
    # Wait for the login page to load and locate the username and password fields
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))

    # Enter the login credentials and submit the form
    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)
    logging.info("Logged into Salesforce successfully")

    # Wait for the page to load after login
    wait = WebDriverWait(driver, 60)

    # Click on the navigation button (DAY 2)
    nav_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div/div/div[1]/div[1]/div/div[1]/runtime_mobilesapp-launch-pad-tile-list/lightning-card/article/div[2]/slot/div/lightning-layout/slot/lightning-layout-item[2]/slot/runtime_mobilesapp-launch-pad-tile/div/div/div/div[1]",
            )
        )
    )
    nav_button.click()
    logging.info("Navigation button clicked")

    # Wait for the search input to be clickable
    search_input = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/c-global-account-search/c-gas-header/div/div[1]/div/div[2]/div[2]/lightning-input[1]/lightning-primitive-input-simple/div/div/input",
            )
        )
    )

    # Enter search term
    search_term = "Nakia Abrams"
    search_input.send_keys(search_term)
    logging.info(f"Entered search term: {search_term}")

    # Wait for and click on the search button
    search_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/c-global-account-search/c-gas-header/div/div[1]/div/div[2]/div[2]/lightning-button/button",
            )
        )
    )
    search_button.click()
    logging.info("Search button clicked")

    # Wait for the search results and click on the first result
    first_result = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/c-global-account-search/div/lightning-layout/slot/lightning-layout-item[1]/slot/div/c-gas-datatable/div[2]/div/div/table/tbody/tr/th/lightning-primitive-cell-factory/span/div/lightning-primitive-custom-cell/lightning-layout/slot/lightning-layout-item[2]/slot/button",
            )
        )
    )
    first_result.click()
    logging.info("First search result clicked")

    # Wait for the page to load and then click on the "Record and Engagement" button
    record_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[3]/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-g-t_-person_-account_-commercial_-final___-account___-v-i-e-w/forcegenerated-flexipage_gt_person_account_commercial_final_account__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-left-sidebar-template-desktop2/div/div[1]/slot/flexipage-component2[1]/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_account___0125f000000ifiiaam___compact___view___recordlayout2/records-highlights2/div[1]/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[2]/runtime_platform_actions-action-renderer/runtime_platform_actions-executor-page-reference/slot/slot/lightning-button/button",
            )
        )
    )
    record_button.click()
    logging.info("Record and Engagement button clicked")

    # Set the channel to "In-person" using the provided XPath
    logging.info("Waiting for Channel dropdown")
    channel_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/span[1]/div/div/div/div/div[1]/span/span[1]/div/div/div/form/div/div[2]/span[1]/div/div/div/div[2]/div[3]/span/div[1]/div[2]")))
    channel_dropdown.click()
    in_person_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//lightning-base-combobox-item[@data-value='In-person']")))
    in_person_option.click()
    logging.info("Selected 'In-person' from the Channel dropdown")

    # Set the duration field to 30 mins using the provided XPath
    logging.info("Waiting for duration field")
    duration_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/span[1]/div/div/div/div/div[1]/span/span[1]/div/div/div/form/div/div[2]/span[1]/div/div/div/div[2]/div[2]/span/div[2]/div[2]")))
    duration_field.clear()
    duration_field.send_keys('30')
    logging.info("Set duration to 30 minutes")

except TimeoutException:
    logging.error("Could not find the element or took too long to load")

finally:
    # Optionally, you can close the driver after all operations
    # driver.quit()
    pass