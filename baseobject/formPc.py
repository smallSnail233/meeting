from selenium.webdriver.common.by import By

from base.base_page import BasePage


class FormPC(BasePage):
    # 浏览按钮元素定位

    def browserFill(self):
        ll_loc = (By.XPATH, "//div[contains(@weid,'98yaqr@1_htfv0m@orgId_nf78ld@orgId_zggflt_btwvd6')]")
        plus_loc = (By.XPATH, "//div[contains(@class,'orgIdFieldClass')]")
        org_loc = (By.XPATH,
                   "//div[contains(@weid,'htfv0m@orgId_nf78ld@orgId_zggflt_rotw1o_o05agw_bp6j7q_9r43ao@0')]")
        self.ll_loc.click()
        self.moveto_element(plus_loc)
        org_loc.click()
