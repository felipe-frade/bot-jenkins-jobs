"""
    Pegar os repositórios do github
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep, time

import env
import sql

log = True

options = webdriver.ChromeOptions()
options.add_argument("--disable-popup-blocking")
options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wait_120 = WebDriverWait(driver, 120)
wait_60 = WebDriverWait(driver, 60)
wait_30 = WebDriverWait(driver, 30)
wait_20 = WebDriverWait(driver, 20)
wait_10 = WebDriverWait(driver, 10)
inicio = time()

if __name__ == '__main__':
    def main():
        driver.get(env.URL_LOGIN_JENKINS)
        wait_120.until(EC.visibility_of_element_located((By.ID, 'j_username')))
        
        driver.find_element_by_id('j_username').send_keys(env.USER_JENKINS)
        driver.find_element_by_css_selector('[name="j_password"]').send_keys(env.PASS_JENKINS)
        driver.find_element_by_css_selector('[type="submit"]').click()

        wait_30.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table#projectstatus')))

        jobs = driver.find_elements_by_css_selector('table tr td:nth-child(3) a')

        all_jobs = f"""SELECT j.id_job FROM ctrl_jenkins_jobs j 
        WHERE j.jenkins = {env.ID_JENKINS} and j.nome_job not in ("""

        for index, job in enumerate(jobs):
            nome_job = job.text
            link_job = job.get_attribute("href")
            
            db_job = sql.get_job_db(nome_job)

            if len(db_job) == 0:
                print(sql.insert_repo_db(nome_job))
            else:
                print(f"""Job "{nome_job}" ja existe""")
            
            all_jobs = all_jobs + F"""'{nome_job}',"""

        all_jobs = all_jobs + F"""'{jobs[-1].text}')"""
        old_jobs = sql.query(all_jobs)

        if len(old_jobs) > 0:
            for job in old_jobs:
                sql.desable_job(job[0])
        else: return True

    main()
driver.close()
print('Finalizando')
exit()
