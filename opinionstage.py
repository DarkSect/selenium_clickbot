#sundaysec--DarkSect 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# change url to your own
url = "https://www.opinionstage.com/api/v1/widgets/565535/iframe"
def vote():
    try:
        while True:
            times = 0
            times+=1
            print("Voting for {} times".format(times))
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("headless")
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
            candidate = driver.find_element_by_xpath('//*[@id="os-body"]/div[1]/div[3]/div/div[1]/div/div[4]/div/div/div[2]/div[1]')
            candidate.click()
            driver.close()
    except Exception as e:
        print("Possible error occured {}".format(e))
    except KeyboardInterrupt:
        print("\nExited cleanly")
vote()
