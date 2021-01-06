## 吉林大学研究生每日打卡
* 本项目是在 [@Asucan/JLU-Daily-Attendance](https://github.com/Asucan/JLU-Daily-Attendance)的基础上修改
负责定时体温&签到打卡+微信消息推送

## 使用说明
使用Python 3，使用前确保第三方包requests、selenium已经安装  

脚本提供**显式&隐式**（是否显式调起浏览器）打卡  

第一次使用请务必 **`手动运行`** 代码，确保运行成功，之后可选择配置自动隐式运行。

请按需配置个人信息，**`因为没有正确配置造成的一切后果与程序作者无关。`**  

## 需要做的事情
* 配置chrome浏览器驱动（配置后需要重启）
  *  下载chrome driver, 将chrome diver放置在chrome浏览器安装文件夹下，并添加环境变量。参考[selenium 安装与 chromedriver安装](https://www.cnblogs.com/lfri/p/10542797.html)
  *  确定chrome 安装位置, 并复制至代码主函数（例如：C:\Program Files (x86)\Google\Chrome\Application）
  
* 配置个人信息
  * ~~个人信息参考 config文件~~
  * 不想写对应关系config文件了，示例代码给了部分对应关系，应该够用
  
* **（可选）** 微信消息提醒（请使用个人微信绑定的SCKEY）
  * server网址http://sc.ftqq.com/3.version

* Windows定时运行脚本。参考[Windows系统中设置Python程序定时运行](https://blog.csdn.net/xgxyxs/article/details/85045801)  
  *  方法一：使用pythonw.exe而不是python.exe, 程序就可以在Windows后台执行, 不显示命令提示符窗口
  *  方法二：是修改脚本的扩展名为".pyw"，双击即可后台运行，不需要修改任何代码


## 更新

* 使用webdriver时,chromedriver有DOS黑窗问题。[Selenium隐藏控制台解决办法](https://www.cnblogs.com/TurboWay/p/9300105.html)
* **`2020/11/09更新`** 更新打卡失败，等待五分钟后重新打卡，直到打卡成功
* **`2020/11/11更新`** 更新因打卡界面改版造成的问题，更新重复微信消息推送失败的问题
* **`2020/11/30更新`** 更新因打卡系统升级造成的问题

## 免责声明
本自动程序适用于 2020-2021 秋季学期吉林大学研究生每日健康打卡（测温&点名），不保证按时更新。 

**使用本程序自动提交打卡，你必须实际完成每日测温，在指定时间回到寝室，并在身体状况出现异常时立刻联系校医院和辅导员。**  

**如运行本程序，您理解并认可，本自动程序的一切操作均视为您本人进行、或由您授权的操作。本程序作者对您因使用此程序可能受到的损失、处罚以及造成的法律后果不负任何责任。**  
