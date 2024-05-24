from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (here using Chrome)
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("https://jqueryui.com/droppable/")
    
    # Wait until the iframe is available and switch to it
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, ".demo-frame")))

    # Locate the source and target elements for the drag and drop operation
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    
    # Perform the drag and drop action
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()

    # Optional: Print a success message
    print("Drag and drop operation completed successfully.")
    
finally:
    # Close the WebDriver
    driver.quit()
