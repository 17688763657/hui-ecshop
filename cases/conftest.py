from selenium import webdriver
import pytest,xlrd
from common.get_excel_data import GetExcelData


#定义一个fixture,打开浏览器,并最大化
@pytest.fixture(name="driver")
def browser():
    driver=webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--host",action="store",default="test",help="evn"
    )

@pytest.fixture(name="base_url")
def base_url(pytestconfig):
    _base_url=pytestconfig.getoption("--host")
    if _base_url=="test":
        return "http://test/ecshop"
    elif _base_url=="uat":
        return "http://uat/ecshop"
    elif _base_url=="sit":
        return "http://sit/ecshop"
    else:
        return "http://test/ecshop"


#定义一个fixture得到获取excel数据的实例
@pytest.fixture(name="excel")
def excel_data():
    file_path=r"C:\Users\11314\Desktop\web自动化2023-2-1\ecshop\cases\test-data.xls"
    sheet_name="login"
    getexceldata = GetExcelData()
    data_list = getexceldata.get_data(file_path, sheet_name)
    yield data_list






