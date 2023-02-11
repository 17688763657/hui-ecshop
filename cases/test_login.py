from pages.login_page import LoginPage
import allure,pytest,json
from common.get_excel_data import GetExcelData

file_path = r"C:\Users\11314\Desktop\web自动化2023-2-1\ecshop\cases\test-data.xls"
sheet_name = "login"
getexceldata = GetExcelData()
data_list = getexceldata.get_data(file_path, sheet_name)



@allure.epic("ecshop")
@allure.feature("登录模块")
class TestLogin():
    @pytest.mark.parametrize("data",data_list)
    @allure.title("")
    def test_login_success(self,driver,base_url,data):
        allure.dynamic.title(data["用例标题"])
        self.url = base_url + "/user.php"
        self.driver=driver
        with allure.step("打开登录页面"):
            self.driver.get(self.url)
        self.loginpage=LoginPage( self.driver)
        with allure.step("输入用户名"):
            self.loginpage.input_username(json.loads(data["测试数据"])["username"])
        with allure.step("输入密码"):
            self.loginpage.input_password(json.loads(data["测试数据"])["password"])
        with allure.step("点击登录按钮"):
            self.loginpage.submit_click()
        assert 2 == data["预期结果"]




