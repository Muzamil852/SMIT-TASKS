from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import csv
import time

url = "https://tiedex.co.uk/collections/all-products"

options = webdriver.ChromeOptions()
# options.add_argument("--headless")             
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(0)

all_products_data = []
product_path = "//div[contains(@class,'grid-item') and contains(@class,'grid-product')]"
for i in range(1):
    print(f"-------Page: {i+1}-------")
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, product_path)))
    except:
        pass
    
    all_products = driver.find_elements(By.XPATH, product_path)
    
    if not all_products:
        print("No products found on this page. Check your product_path XPath.")
        break

    for p in all_products:
        try:
            title = p.find_element(By.XPATH,".//span[contains(@class,'element-text--body-md')]").text
        except NoSuchElementException:
            title = "N/A"
            
        try:
            price = p.find_element(By.XPATH,".//span[contains(@class,'money')]").text        
        except NoSuchElementException:
            price = "N/A"
            
        try:
            description = driver.find_element(By.XPATH,"//div[contains(@class,'product-single__description') or contains(@class,'product__description') or @data-product-description] | //div[@itemprop='description']").text
        except NoSuchElementException:
            description = "N/A"
            
        try:
            availability = driver.find_element(By.XPATH,"//span[contains(@class,'inventory') or contains(@class,'availability')]").text
        except NoSuchElementException:
            try:
                driver.find_element(By.XPATH,"//button[contains(.,'Add to cart') or contains(.,'Add to Cart')]")
                availability = "In Stock"
            except NoSuchElementException:
                availability = "Out of Stock"
                
            all_products_data.append([title, price, description, availability])

    try:
        next_button = driver.find_element(By.XPATH, "//a[contains(@class,'element-button') and contains(@aria-label,'Next')]")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(2) 
    except NoSuchElementException:
        print("No more pages found. Ending extraction.")
        break

with open("All_products.csv", 'w', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator='\n')
    # Write the header row first
    writer.writerow(['Title', 'Price', 'Description', 'Availability'])
    # Write all the product data
    writer.writerows(all_products_data)

print(f"Extraction complete! Scraped {len(all_products_data)} products.")

time.sleep(3)
driver.quit()