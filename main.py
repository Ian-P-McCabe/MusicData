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

"""
Program steps
#For each url, open process to gather all JSON from the webpage. 
"""
def fetch_BSO_JSON(start_year, end_year, run_id):

    url = f'https://archives.bso.org/Search.aspx?SearchType=Performance&startTime=10%2F01%2F{start_year}&endTime=09%2F30%2F{end_year}'

    # Define webdriver, get url, and wait for delay seconds for the requisite element to appear
    driver = webdriver.Chrome()
    driver.get(url)
    # TODO: This is not enough time lol, will a minute be enough time?
    delay = 60
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "resultCount")))
    except Exception as e:
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

                # print(bso_info)
                print(count)
                print(len(bso_info['Results']))

                #TODO: Turn writing to file back on once done with testing

                filename = run_id + "/" + "BSO_" + str(start_year) + "_to_" + str(end_year) + "_" + str(count) + ".json"

                f = open(filename, "w")
                f.write(json.dumps(bso_info))
                f.close()

                count += 1

    driver.quit()
    #print("Done with " + str(start_year) + " to " + str(end_year) + ", waited " + str(rand_wait) + " seconds.")


def run_scraper(run_id):

    #TODO: Re enable this later
    #os.mkdir(run_id)

    current_start = 1881
    count = 0
    start_year = 1881
    end_year = 2024

    pool = Pool(processes=4)
    # Broke at 1971 for some reason, what happens if we start there
    for i in range(1967, 1968):
        pool.apply_async(fetch_BSO_JSON, args=(i, i+1, run_id,))
        time.sleep(2)

    pool.close()
    pool.join()

    # TODO: Need 1902 to 1903, not sure why it failed, it is in Test03
    # TODO: Also just missing many years?
    # TODO: For some reason 1980 just kills this program


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
    run_scraper("BSO_Data/Run_02")



# filelist = os.listdir("Prod01_1881_1970")
# newlist = [x[12:16] for x in fileList]
# newlist = [x[12:16] for x in filelist]
# for i in range(1881, 1972):
#     if str(i) not in newlist:
#         print(i)

