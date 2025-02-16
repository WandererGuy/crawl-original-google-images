from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import json
from tqdm import tqdm 
import random
import shutil
import urllib



import io

from PIL import Image  # https://pillow.readthedocs.io/en/4.3.x/
import requests  # http://docs.python-requests.org/en/master/


# example image url: https://m.media-amazon.com/images/S/aplus-media/vc/6a9569ab-cb8e-46d9-8aea-a7022e58c74a.jpg
def download_image(url, image_file_path):
    r = requests.get(url, timeout=4.0)
    time.sleep(2)
    if r.status_code != requests.codes.ok:
        assert False, 'Status code error: {}.'.format(r.status_code)

    with Image.open(io.BytesIO(r.content)) as im:
        im.save(image_file_path)

    print('Image downloaded from url: {} and saved to: {}.'.format(url, image_file_path))


service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
DRIVER= webdriver.Chrome(service=service, options=options)

def find_max_int(filepath):
    ls = []
    for filename in os.listdir(filepath):
        ls.append(int(filename.split('.')[0]))
    return max(ls)



# kw_dict = {"fishing boat asia": "fishing_boat_asia"}
kw_search = "tau van tai trung quoc"
kw_search_value = "_".join(kw_search.split(' '))
kw_dict = {kw_search: kw_search_value}


search_keyword = next(iter(kw_dict))
folder_keyword = kw_dict[search_keyword]

if __name__ == "__main__":
    DRIVER.get("https://www.google.com/search?q=tau+danh+ca&sca_esv=1b49f95c0843824b&sxsrf=AHTn8zrKvTKdY8FTaY_XW8q0Zt7eIbrxSg:1739683765517&source=hp&biw=956&bih=945&ei=tXexZ-bgHKXe2roP19uZoAU&iflsig=ACkRmUkAAAAAZ7GFxUDIi9PDgr7U1S2AFrd8S-csH7Ut&oq=&gs_lp=EgNpbWciACoCCAAyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gJI64gYUABYAHACeACQAQCYAQCgAQCqAQC4AQHIAQCKAgtnd3Mtd2l6LWltZ5gCAqACGqgCCpgDEZIHATKgBwA&sclient=img&udm=2")
    xpath = "/html/body/div[2]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div[2]/textarea"
    input_area = DRIVER.find_element(By.XPATH, xpath)  
    os.makedirs(f"urls/{folder_keyword}", exist_ok=True)
    os.makedirs(f"images/{folder_keyword}", exist_ok=True)

    fail_src_url = "data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="

    # URL = "https://www.google.com/search?sca_esv=719323f8b4394607&q=tau+danh+ca&udm=2&fbs=ABzOT_AfCikcO6SgGMxZXxAG9tmS8rx53CbgOCSVg3O9Xo5xAK_RXi3VFy8QcDJV9F46BNX0kZcBdv2qiG8279sznoGvwXYVfqXi5AxPvDXkJ-MkwThOeWf1fl0-vP_stZw2-wiFo2_fcg96rRhBCMfKN9fd7eIVFeeEix-moWmSapYEMEksBbaReod_JR2StsZ_J6rZI-OtKz6sLewu_ahkl0bzIipJiM2sgx0UvR4EsxPbUSRk_Cs&sa=X&ved=2ahUKEwi01vqv7cKLAxUirlYBHR0DM84QtKgLegQIGRAB&biw=1920&bih=945"
    # DRIVER.get(URL) 

    # Open Google

    # Find the input area (Google search bar)


    # Clear any pre-filled text (if any)
    input_area.clear()

    # Type the text you want to search
    text_to_search = search_keyword
    input_area.send_keys(text_to_search)

    # Simulate pressing the 'Enter' key to start the search
    input_area.send_keys(Keys.RETURN)
    # max_num = find_max_int(filepath = f"images/{folder_keyword}")
    time.sleep(3)
    for n in range(1, 150):
        if n % 10 == 0: 
            DRIVER.execute_script("window.scrollBy(0, 1000);") # scroll down
            time.sleep(2)
        print (f"________process image {n}__________")
        xpath = f"/html/body/div[3]/div/div[14]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[{n}]/div[2]/h3/a/div/div/div/g-img/img"
        try:
            image_area = DRIVER.find_element(By.XPATH, xpath)
        except:
            continue 
        image_src = image_area.get_attribute("src")
        if image_src != fail_src_url:
            urllib.request.urlretrieve(image_src, f"images/{folder_keyword}/{n}.png")
        else: 
            print ("source url corrupted", n)
    DRIVER.close()