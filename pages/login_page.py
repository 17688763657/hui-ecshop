from selenium import webdriver



class LoginPage():
    def __init__(self,driver):
        #self.driver = webdriver.Chrome()
        self.driver=driver
        self.driver.implicitly_wait(10)
        self.username=self.driver.find_element_by_css_selector('[name="username"]')
        self.password=self.driver.find_element_by_css_selector('[name="password"]')
        self.submit = self.driver.find_element_by_css_selector('[name="submit"]')

    def input_username(self,text):
        """输入用户名"""
        self.username.send_keys(text)

    def input_password(self,text):
        """输入密码"""
        self.password.send_keys(text)

    def submit_click(self):
        """点击登录按钮"""
        self.submit.click()

