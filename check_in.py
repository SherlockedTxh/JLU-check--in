import time
import datetime
import os
import traceback
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class clock_in:
    def __init__(self, dic, chrome_driver_path, op=1):
        self.dic = dic
        self.dirver_path = chrome_driver_path
        self.op = op
        self.log = ''

    def start(self):
        self.browser = self.browser_start(self.dirver_path, op=self.op)
        self.login(self.dic)
        return self.log

    def login(self, dic):
        # 输入账号密码
        acc_input = self.browser.find_element_by_xpath('//*[@id="username"]')
        acc_input.clear()
        acc_input.send_keys(dic['username'])
        acc_input = self.browser.find_element_by_xpath('//*[@id="password"]')
        acc_input.clear()
        acc_input.send_keys(dic['passwd'])

        # 点击登录
        self.browser.find_element_by_xpath('//*[@id="login-submit"]').click()
        print(dic['username'] + ' log in...')
        self.log += dic['username'] + ' log in...\t'
        time.sleep(3)

        # 点击研究生打卡
        self.browser.find_element_by_xpath('//body/div[8]/a[4]/div[1]').click()
        time.sleep(2)

        # 点击我要办理
        self.browser.find_element_by_xpath('//body/div[4]/div[1]/button[1]').click()
        print('进入打卡页面...')
        self.log += '进入打卡页面...\t'
        time.sleep(8)

        handles = self.browser.window_handles
        self.browser.switch_to_window(handles[1])

        '''
        #判断打卡时间
        if hour == 7:
            # 7：00-8：00 体温状态
            browser.find_element_by_xpath('').click()
        elif hour == 11:
            #11：00-12：00 体温状态
            browser.find_element_by_xpath('//*[@id="V1_CTRL19"]').click()
        elif hour == 17:
            # 17：00-18：00 体温状态
            browser.find_element_by_xpath('//*[@id="V1_CTRL23"]').click()
        '''
        curr_time = datetime.datetime.now()
        hour = int(curr_time.hour)
        if 5 < hour < 12:
            # self.browser.find_element_by_xpath('//*[@id="V1_CTRL28"]').click()
            pass
        elif 19 < hour < 24:
            pass
        else:
            self.log += '打卡时间错误 '
        print('打卡时间 ' + curr_time.strftime('%Y-%m-%d %H:%M:%S') + '...')
        self.log += '打卡时间 ' + curr_time.strftime('%Y-%m-%d %H:%M:%S') + '...\t'

        # 输入专业
        zy = self.browser.find_element_by_xpath(
            '/html/body/div[4]/form/div/div[3]/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td[2]/div/input')
        zy.clear()
        zy.send_keys(dic['zy'])

        # 选择年级
        Select(self.browser.find_element_by_xpath(
            "/html/body/div[4]/form/div/div[3]/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td[4]/font/div/select")).select_by_value(
            dic['nj'])

        # 选择校区
        Select(self.browser.find_element_by_xpath(
            "/html/body/div[4]/form/div/div[3]/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td/div/table/tbody/tr[4]/td[4]/font/div/select")).select_by_value(
            dic['xq'])

        # 输入手机
        sj = self.browser.find_element_by_xpath(
            '/html[1]/body[1]/div[4]/form[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/table[1]/tbody[1]/tr[5]/td[2]/div[1]/input[1]')
        sj.clear()
        sj.send_keys(dic['sj'])

        # 研究生秘书
        ms = self.browser.find_element_by_xpath(
            '/html[1]/body[1]/div[4]/form[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/table[1]/tbody[1]/tr[5]/td[4]/font[1]/div[1]/div[1]/div[1]/div[1]/input[1]')
        ms.clear()
        ms.send_keys(dic['ms'])

        # 点击校内
        element = self.browser.find_element_by_xpath('//input[@id="V1_CTRL63"]')
        self.browser.execute_script("arguments[0].click();", element)

        # 输入位置
        Select(self.browser.find_element_by_xpath(
            "/html[1]/body[1]/div[4]/form[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/table[1]/tbody[1]/tr[6]/td[3]/font[1]/div[1]/select[1]")).select_by_value(
            dic['wz'])

        # 选择公寓
        Select(self.browser.find_element_by_xpath(
            "/html[1]/body[1]/div[4]/form[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/table[1]/tbody[1]/tr[7]/td[2]/div[1]/select[1]")).select_by_value(
            dic['gy'])

        # 填写寝室号
        qsh = self.browser.find_element_by_xpath(
            '/html[1]/body[1]/div[4]/form[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/table[1]/tbody[1]/tr[8]/td[2]/div[1]/input[1]')
        qsh.clear()
        qsh.send_keys(dic['qsh'])

        # 点击硕士
        # self.browser.find_element_by_xpath('//*[@id="V1_CTRL44"]').click()
        element = self.browser.find_element_by_xpath('//*[@id="V1_CTRL44"]')
        self.browser.execute_script("arguments[0].click();", element)
        print('填写基本信息...')
        self.log += '填写基本信息...\t'

        # 提交
        self.browser.find_element_by_xpath('/html[1]/body[1]/div[4]/form[1]/div[1]/div[3]/div[3]/div[2]/ul[1]/li[1]/a[1]').click()

        time.sleep(3)
        # 确认
        self.browser.find_element_by_xpath('/html[1]/body[1]/div[6]/div[1]/div[2]/button[1]').click()
        print('提交确认...')
        self.log += '提交确认...\t'
        time.sleep(3)
        if '办理成功' in self.browser.page_source:
            print('办理成功 !')
            self.log += '办理成功 !'

    def browser_start(self, path, op):
        chrome_driver_path = path
        os.environ["webdriver.ie.driver"] = chrome_driver_path
        if op == 0:
            # 隐式使用浏览器
            option = webdriver.ChromeOptions()
            option.add_experimental_option('excludeSwitches', ['enable-logging'])
            option.add_argument('headless')
            browser = webdriver.Chrome(options=option)
        elif op == 1:
            # 显式使用浏览器
            browser = webdriver.Chrome()
        browser.get("https://ehall.jlu.edu.cn/jlu_portal/")
        time.sleep(3)
        return browser


# 微信提醒打卡成功或失败
def notification(status, SCKEY):
    textPush = status
    urlPush = 'https://sc.ftqq.com/' + SCKEY + '.send'
    dataPush = {'text': textPush}
    requests.post(urlPush, data=dataPush, verify=False)


def process(dic, person, chrome_driver_path, op):
    clock = clock_in(dic[person], chrome_driver_path, op)
    try:
        text = clock.start()
        if dic[person]['wechat'] == 1:
            notification('打卡成功! 日志: ' + text, dic[person]['SCKEY'])
        # clock.browser.quit()
        return 1
    except Exception as e:
        traceback.print_exc()
        if dic[person]['wechat'] == 1:
            dic[person]['num'] += 1
            notification(
                '打卡失败' + str(dic[person]['num']) + '次 五分钟后重新打卡  日志: ' + clock.log + ' 错误提示：' + traceback.format_exc(),
                dic[person]['SCKEY'])
        # clock.browser.quit()
        return 0


if __name__ == "__main__":
    dic = dict()
    # ****************************需要个人填写的部分*************************
    # gy{'12':南苑8公寓,'10':'南苑6公寓'} xq{'1':中心校区} nj{'9':2018级}
    # 缩写 qsh:寝室号 zy:专业  wechat: 是否微信提醒：1：提醒，0：不提醒 (微信提醒需要配置SCKEY码，详情参考github-readme) flag:打卡标识 num：累计失败打卡次数
    # 新增: sj: 手机号 ms: 研究生秘书 wz: 在校原因
    dic['x1'] = {'username': 'zhangs18', 'passwd': '123', 'qsh': '111', 'gy': '12', 'zy': u"计算机", 'xq': '1',
                 'nj': '9', 'sj': '1234567890', 'ms': u'张三', 'wz': '3', 'flag': True, 'wechat': 0, 'num': 0}
    # dic['x2'] = {'username': 'x218', 'passwd': '...', 'qsh': '333', 'gy': '12', 'zy': u"搬砖技术", 'xq': '1','nj': '9','flag':True, 'wechat':0, 'num':0}
    chrome_driver_path = "/usr/local/bin"  # chrome driver 位置 不同主机可能不同
    dic['x1']['SCKEY'] = '...'
    # dic['x2']['SCKEY'] = '...'
    op = 0  # 是否显示调用浏览器：1：显式，0：隐式
    # ****************************需要个人填写的部分*************************

    while 1:
        judge = 0
        for person in dic:
            if dic[person]['flag'] == True:
                flag = process(dic, person, chrome_driver_path, op)
                if flag == 1:
                    dic[person]['flag'] = False
                judge += flag
            else:
                judge += 1
        if judge == len(dic):
            break
        else:
            break
