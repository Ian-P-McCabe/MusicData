import traceback
from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from multiprocessing import Pool
import os
import json
import time
from random import randrange
import shutil
import logging

"""
Program steps
#For each url, open process to gather all JSON from the webpage. 
"""
def fetch_BSO_JSON(start_year, end_year, run_id):
    url = f'https://archives.bso.org/Search.aspx?SearchType=Performance&startTime=10%2F01%2F{start_year}&endTime=09%2F30%2F{end_year}'

    # Define webdriver, get url, and wait for delay seconds for the requisite element to appear
    driver = webdriver.Chrome()
    driver.get(url)
    # Capping this at a minute and a half, still getting some timeout exceptions at a minute
    delay = 90

    # pagedict = {'Error': "No error"}
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "resultCount")))
    except Exception as e:
        #pagedict['Error'] = {"Overview" : "ERROR WITH: " + str(start_year) + " to " + str(end_year)}
        #pagedict['Error']['Detailed'] = "An error occurred: " + traceback.format_exc()
        print("ERROR WITH: " + str(start_year) + " to " + str(end_year))
        print("An error occurred: ", traceback.format_exc())

    # TODO: Some years return multiple GetEventDetails (1967-1968 and 2003-2004)
    # TODO: Handle Bad Gateway error (if element doesn't appear then continue/note missed)
    count = 1
    for request in driver.requests:
        if request.response:
            if request.url == "https://archives.bso.org/ArchiveWebService.asmx/GetEventDetails":
                raw_json = request.response.body

                clean_json = json.loads(raw_json)

                bso_info = json.loads(clean_json['d'])

                filename = run_id + "/" + "BSO_" + str(start_year) + "_to_" + str(end_year) + "_" + str(count) + ".json"

                f = open(filename, "w")
                f.write(json.dumps(bso_info))
                f.close()

                count += 1

    driver.quit()
    rand_wait = randrange(2,7)
    #print("Done with " + str(start_year) + " to " + str(end_year) + ", waited " + str(rand_wait) + " seconds.")


def run_scraper(run_id, start_year, end_year):

    os.makedirs(run_id)

    #1881 to 2024 is how long the BSO has existed
    pool = Pool(processes=4)
    for i in range(start_year, end_year):
        pool.apply_async(fetch_BSO_JSON, args=(i, i+1, run_id,))
        time.sleep(2)

    pool.close()
    pool.join()


def fetch_missing():
    run_id = "Prod06_Missing_Years"

    os.mkdir(run_id)

    missing_years = [1891, 1955, 1925, 1958, 1902, 1966, 1936, 1967, 1968, 1915]

    pool = Pool(processes=4)
    # Broke at 1971 for some reason, what happens if we start there
    for year in missing_years:
        pool.apply_async(fetch_BSO_JSON, args=(year, year + 1, run_id,))
        time.sleep(2)

    pool.close()
    pool.join()


def combine_files():
    final_dir = "Complete_Years_1"

    os.mkdir(final_dir)

    dirs = ['Prod02_1971_2024', 'Prod04_1971_2024', 'Prod03_1971_2024', 'Prod06_Missing_Years', 'Prod01_1881_1970', 'Prod05_1971_2024']
    moved = []
    for d in dirs:
        files = os.listdir(d)
        for file in files:
            if file not in moved:
                filepath = d + "/" + file
                shutil.copy(filepath, final_dir)
                moved += [file]

        print("Completed files in " + d)


def check_performance_totals():
    # Place values in a dictionary
    fdict = {}
    for file in os.listdir('BSO_Data/Run_01/Complete_Years_1'):
        with open('BSO_Data/Run_01/Complete_Years_1/' + file) as f:
            d = json.load(f)
            l = len(d['Results'])
            fdict[file] = l

    keys = list(fdict.keys())
    values = list(fdict.values())
    import numpy as np
    sorted_value_index = np.argsort(values)
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

    return sorted_dict


if __name__ == "__main__":
    print("Running")
    #run_scraper("BSO_Data/Run_02/Test_06_2001_2024", 2001, 2024)

def combine_json_in_file():
    result_list = []
    dirs = ['Test_03_1881_1921',
            'Test_05_1961_2001',
            'Test_06_2001_2024',
            'Test_04_1921_1961']
    for d in dirs:
        files = os.listdir("BSO_Data/Run_02/" + d)
        for file in files:
            with open("BSO_Data/Run_02/" + d + "/" + file) as f:
                data = json.load(f)
                result_list += data['Results']

    with open("FullResults_01.json", "w") as f:
        json.dump(result_list, f, indent=4)



# filelist = os.listdir("Prod01_1881_1970")
# newlist = [x[12:16] for x in fileList]
# newlist = [x[12:16] for x in filelist]
# for i in range(1881, 1972):
#     if str(i) not in newlist:
#         print(i)

