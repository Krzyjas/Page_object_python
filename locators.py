from selenium.webdriver.common.by import By


class PageLocators:
    logo_text = (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/section/div/hgroup/h2')
    HTTP_Methods_bar = (By.XPATH, '//*[@id="operations-tag-HTTP_Methods"]')
    HTTP_Methods_DELETE_bar = (By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/section/div/div[1]/div/div[1]/div[1]')
    HTTP_Methods_DELETE_TRYitOUT_button = (By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/section/div/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]')