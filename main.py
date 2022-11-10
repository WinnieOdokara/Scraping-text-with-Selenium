# Install Selenium

# Open the "replit.nix" file on hiden files. 
  # On line 4 add: pkgs.chromium
  # On line 5 add: pkgs.cromedriver

from selenium import webdriver

def get_driver():
  # Ste options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage") # avoid issue when running in Linux
  options.add_argument("no-sandbox") # Disable sandbox in the webpage
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled") #

  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/")
  return driver


def main():
  driver = get_driver()
  element = driver.find_element(by="xpath",
                                value="/html/body/div[1]/div/h1[1]")
  return element.text


print(main())