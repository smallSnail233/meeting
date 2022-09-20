import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class test_case():
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    wd.get("https://weapp.teamsyun.com/")
# 登录
account = wd.find_element(By.XPATH, "//input[@type='text']").send_keys('17816062993')
password = wd.find_element(By.XPATH, "//input[@type='password']").send_keys('sq123!')
button = wd.find_element(By.XPATH, "//button[@weid='_mtgi04_6p6nql_pylpnk_3e2zi8_4euq0x_40m1j2']")
button.click()
sleep(5)

# #找到更多应用
# more = wd.find_element(By.XPATH,'//div[@class="e10header-trigger-blacklist e10header-menu-item e10header-menu-item-more "]')
# ActionChains(wd).move_to_element(more).perform()
# sleep(5)
#
# #找到会议管理
# wd.find_element(By.XPATH, '//a[@title="会议管理"]').click()

# 新建会议
# wd.find_element(By.XPATH,'//button[text()="新建会议"]').click()
# sleep(5)
# wd.find_element(By.XPATH,'//input[@groupid="757926934622355456"]').send_keys("新建会议01")
# sleep(5)
# #会议类型浏览按钮
# wd.find_element(By.XPATH,'(//*[name()="svg" and @class="ui-icon-xs ui-icon-svg Icon-add-to01" ])[2]').click()
# sleep(3)
# #鼠标悬浮
# # ActionChains(wd).move_to_element(mtTYpe).perform()
# # sleep(5)
# # mtTYpe.click()
# wd.find_element(By.XPATH,'//div[@id="associative-dropdown-list_list_0"]').click()
# sleep(3)
#
# wd.find_element(By.XPATH,'(//*[name()="svg" and @class="ui-icon-xs ui-icon-svg Icon-add-to01" ])[3]').click()
# sleep(3)
# wd.find_element(By.XPATH,'//div//span[text()="shiqian"]').click()
# wd.find_element(By.XPATH,'(//*[name()="svg" and @class="ui-icon-xs ui-icon-svg Icon-add-to01" ])[4]').click()
# sleep(3)
# wd.find_element(By.XPATH,'//div//span[text()="shiqian"]').click()


# 找到会议类型菜单
wd.find_element(By.XPATH, "//div[@id='meeting_setPage']").click()
sleep(3)
wd.find_element(By.XPATH, "//div[@weid='903dhc_dxm7ci_ym7z0m_8km5jp']//div[@id='typeSet']").click()
sleep(3)
# 新建会议类型
wd.find_element(By.XPATH, "//button[contains(@weid,'jij2o9_cxay0q')]").click()
sleep(3)
wd.find_element(By.XPATH,"//input[contains(@weid,'7lhf0u_98yaqr@0_htfv0m@name_nf78ld@name_zggflt')]").send_keys("自动化04")
sleep(3)
#所属机构浏览按钮
# ll= wd.find_element(By.XPATH,"//div[contains(@weid,'98yaqr@1_htfv0m@orgId_nf78ld@orgId_zggflt_btwvd6')]")
# ActionChains(wd).move_to_element(ll).perform()
# sleep(3)
# wd.find_element(By.XPATH,"//div[contains(@class,'orgIdFieldClass')]").click()
# sleep(3)
# wd.find_element(By.XPATH,"//div[contains(@weid,'htfv0m@orgId_nf78ld@orgId_zggflt_rotw1o_o05agw_bp6j7q_9r43ao@0')]").click()
# sleep(3)
#保存按钮


wd.find_element(By.XPATH,"//button[contains(@weid,'r2p6ih_sgokcy_zxrynl')]").click()
sleep(3)

print("=============success=================")



# type= wd.find_element(By.XPATH,'//div[@class="ui-browser is-empty is-single orgIdFieldClass meetingFieldCommonClass"]').click()
# ActionChains(wd
#         ).move_to_element().perform()
# sleep(3)
# wd.find_element(By.XPATH,'//div[@id="associative-dropdown-list_list_0"]').click()
# sleep(3)
# wd.find_element(By.XPATH, '//button[text()="保存"]').click()
# sleep(5)

wd.close()
