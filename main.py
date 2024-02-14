from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import json

if __name__ == "__main__":
    print("Hello world")
    search_string = "https://archives.bso.org/Search.aspx?SearchType=Performance&startTime=08%2F01%2F2022&endTime=08%2F01%2F2023"
    driver = webdriver.Chrome()

    driver.get(search_string)

    delay = 12

    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "resultCount")))

    count = 1
    for request in driver.requests:
        if request.response:
            if request.url == "https://archives.bso.org/ArchiveWebService.asmx/GetEventDetails":

                raw_json = request.response.body

                clean_json = json.loads(raw_json)

                bso_info = json.loads(clean_json['d'])

                filename = "bso_out_" + str(count) + ".json"

                f = open(filename, "w")
                f.write(json.dumps(bso_info))
                f.close()

                count += 1


