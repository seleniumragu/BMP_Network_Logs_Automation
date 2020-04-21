import json
import pprint
import time

from browsermobproxy import Server
from selenium import webdriver


class ProxyManger:
    __BMP = "C:\\Python38-32\\libs\\browsermob-proxy-2.1.4-bin\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat"

    def __init__(self):
        self.__server = Server(ProxyManger.__BMP, options = {'port': 9999})

        self.__client = None

    def start_server(self):
        self.__server.start()
        return self.__server

    def start_client(self):
        self.__client = self.__server.create_proxy(params={"trustAllServers": "true"})
        return self.__client

    @property
    def client(self):
        return self.__client

    @property
    def server(self):
        return self.__server


if "__main__" == __name__:
    proxy = ProxyManger()
    server = proxy.start_server()
    client = proxy.start_client()
    client.new_har('req', options = {'captureHeaders': True, 'captureContent': True})

    options = webdriver.ChromeOptions()
    options.add_argument("--proxy-server={}".format(client.proxy))
    options.add_argument("--disable-web-security")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://client-rewards-backoffice.internal.iherbtest.io/rewards")
    driver.find_element_by_id('username').send_keys('rsekaran')
    driver.find_element_by_id('password').send_keys('Qwert12345%')
    driver.find_element_by_css_selector('div> button[class="btn btn-primary w100P"]').click()
    time.sleep(5)
    t = time.localtime()
    timestamp = time.strftime('%b-%d-%Y_%H_%M_%S', t)
    har_file = open('Rewards_har_file_'+timestamp+'.har', 'w')
    json.dump(client.har, har_file)
    # har_file.write(str(client.har))
    har_file.close()
    pprint.pprint(client.har)
    # driver.quit()
    server.stop()
