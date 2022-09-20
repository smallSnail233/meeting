import unittest
from time import sleep

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


from baseobject.login_page import LoginPage


class TestLogin(unittest.TestCase):
    def test_01_login(self):
        lp = LoginPage()
        lp.login()

class NewMeetingtype(unittest.TestCase)
    def add_meetingtype(self):


webdriver.find_element(By.XPATH, "//div[@id='meeting_setPage']").click()
sleep(3)
webdriver.find_element(By.XPATH, "//div[@weid='903dhc_dxm7ci_ym7z0m_8km5jp']//div[@id='typeSet']").click()
sleep(3)
# 新建会议类型
webdriver.find_element(By.XPATH, "//button[contains(@weid,'jij2o9_cxay0q')]").click()
sleep(3)
webdriver.find_element(By.XPATH, "//input[contains(@weid,'7lhf0u_98yaqr@0_htfv0m@name_nf78ld@name_zggflt')]").send_keys(
    "自动化04")
sleep(3)
# 所属机构浏览按钮
ll = webdriver.find_element(By.XPATH, "//div[contains(@weid,'98yaqr@1_htfv0m@orgId_nf78ld@orgId_zggflt_btwvd6')]")
ActionChains(webdriver).move_to_element(ll).perform()
sleep(3)
webdriver.find_element(By.XPATH, "//div[contains(@class,'orgIdFieldClass')]").click()
sleep(3)
webdriver.find_element(By.XPATH,
                "//div[contains(@weid,'htfv0m@orgId_nf78ld@orgId_zggflt_rotw1o_o05agw_bp6j7q_9r43ao@0')]").click()
sleep(3)
# 保存按钮


webdriver.find_element(By.XPATH, "//button[contains(@weid,'r2p6ih_sgokcy_zxrynl')]").click()
sleep(3)

print("=============success=================")
