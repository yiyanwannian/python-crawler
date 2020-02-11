# !/usr/bin/python3
import json
import pickle
import threading
import time

import threadpool

import utility.constants as constants
# import types as types1
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utility.logger import logger
from utility.threadhelper import ThreadHelper
from utility.httphelper import HttpHelper

class Hospital:
    def __init__(self):
        self.ID = None
        self.XZQH = None
        self.TJ_TYPE = None
        self.JGMC = None
        self.DETAIL_URL = None
        self.TJ_TYPE1 = None
        self.TJ_TYPE2 = None

class HospitalDetail:
    def __init__(self):
        self.ID = None
        self.JGMC = None
        self.Address = None
        self.Relationships = None
        self.PostCode = None
        self.HostUnit = None
        self.PhoneNumber = None
        self.EmployeesCount = None
        self.HealthTechnicians = None

class HospitalDetails:
    def __init__(self):
        self.Hospitals = []

class Crawler:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.hospitals = list()
        # self.threadpool = threadpool.ThreadPool(10)
        self.lock = threading.RLock()

        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": '''
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        '''})

    def __del__(self):
        self.driver.close()

    def get_hospitals(self):

        data = HttpHelper.get_in_json(constants.WJW_Host + "/list.json?_=1580362052641&MmEwMD=4tBgYFOa5TorLjul28il1RzvJopNieGO\
        cEbjSbHSkI7bwXImV7wISh.N79R1iSOKD3Lj.Ht.hM90xS0BMBChTkxbs6DY6eF1MHW2BlsEBelCgIPSOwEvgRxULbvvyM5IoxCQLFhgyd_bQkoVulWxkz\
        vrMDzMedg_8z2t9WW1Cc.FcokJoCIcJ46nQiUintnsTgfZT4H.VIH.3ZtnVVyWR_3HjDTg7AIMVW6haXacuYAmQ9LgCpqDhIwHgNWMjJaLM7IhaoRkiSv8\
        9hQt.BcA.SZc0HR_bHNCXiNd1_E5C45Bm_ZqS7e13PIFs6r.ws0cxraPLF1cqSamaX7pFxVQ1oT1Z16xQWuoI7IED40n.75k1xALy1\ORG1hcmTJjoIYXC\
        IJgSA1Qq7xG__YcpK5jtFJN0oHi4Lk3IZh24Um6FzmCbD6")

        logger.info("Get {0} hospitals data".format(len(data["data"])))

        for item in data["data"]:
            text = item["TEXT"]
            start = text.find('./') + 1
            end = text.find('l\' ') + 1
            url = constants.WJW_Host + text[start:end]

            hospital = Hospital()
            hospital.ID = item["ID"]
            hospital.XZQH = item["XZQH"]
            hospital.TJ_TYPE = item["TJ_TYPE"]
            hospital.JGMC = item["JGMC"]
            hospital.DETAIL_URL = url
            hospital.TJ_TYPE1 = item["TJ_TYPE1"]
            hospital.TJ_TYPE2 = item["TJ_TYPE2"]

            self.hospitals.append(hospital)

        # self.hospitals = self.hospitals[1000:]

    def get_hospital_details(self):
        step_size = 100
        total = len(self.hospitals)
        times = int(total / step_size)
        logger.info("Will save {0} files".format(times + 1))

        for index in range(10, times):
            self.get_hospital_details_zone(index * step_size, (index + 1) * step_size)

        self.get_hospital_details_zone(times * 100, total)

    def get_hospital_details_zone(self, start, end):
        logger.info("Get data from {0} to {1}".format(start, end))
        details = HospitalDetails()
        for hospital in self.hospitals[start:end]:
            self.get_hospital_detail(hospital, details)
        # task = threading.Thread(name=hospital.JGMC, target=self.get_hospital_detail, args=[hospital, details])
        # task.setDaemon(True)
        # task.start()
        # task.join()

        path = './data/hospital_detail{0}-{1}.json'.format(start, end)
        with open(path, 'w+') as f:
            json.dump(details, fp=f, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)
            logger.info("Saved {0} data to {1}".format(len(details.Hospitals), path))
        time.sleep(5)

    def get_hospital_detail(self, hospital: Hospital, details: HospitalDetails):
        logger.info("Get {0} {1}'s data from {2}".format(hospital.ID, hospital.JGMC, hospital.DETAIL_URL))
        self.lock.acquire()

        detail = HospitalDetail()
        self.driver.get(hospital.DETAIL_URL)
        detail.ID = hospital.ID
        detail.JGMC = self.driver.find_element_by_id("jgmc").text
        detail.Address = self.driver.find_element_by_id("s010301").text
        detail.Relationships = self.driver.find_element_by_id("tjSub").text
        detail.PostCode = self.driver.find_element_by_id("s010302").text
        detail.HostUnit = self.driver.find_element_by_id("tjOrgan").text
        detail.PhoneNumber = self.driver.find_element_by_id("s010303").text
        detail.EmployeesCount = self.driver.find_element_by_id("n31").text
        detail.HealthTechnicians = self.driver.find_element_by_id("n311").text

        details.Hospitals.append(detail)
        self.lock.release()


if __name__ == '__main__':
    crawler = Crawler()
    crawler.get_hospitals()
    crawler.get_hospital_details()
