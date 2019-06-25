# 框架介绍
基于pytest、allure、requests、jenkins，进行二次封装的接口自动化测试框架

设计思想：分层设计，结合关键字驱动和数据驱动

## 业务层（api）
1、通用业务的封装：比如接口sig加签

2、接口api的封装：主要是app这边调用的接口

## 数据层（config、data）
1、配置数据：config，通用配置

2、测试数据：data，需要用到的测试数据

## 输出层（log、allure-results）
1、日志：log，测试过程中用户写的日志

2、报告：allure-results，html可视化报告，使用开源报告工具allure

## 用例层（testcase）
1、测试用例：

## 工具层（utils）
1、文件读写：（目前都是读）ini、yaml、excel等

2、邮件发送：收件人信息，配置在ini文件中

3、Http请求：requests模块，

4、日志：

5、Jenkins：开放api，主要是报告内容的获取

# 使用姿势
## 用例编写（Hard Coding）
### 业务层：（api） -- 业务关键字
1、通用业务的封装

2、接口的封装
### 用例层：（testcase）
设计构想：用例均是由业务层接口的组装

1、命名规则：test_package、test_file、test_class、test_method、test_function都以"test_"开头

2、调用业务层的接口

3、基于数据驱动编写测试用例

4、精通pytest.fixture的使用

5、登陆token解决方案

## 关于报告
1、Allure开源测试报告的使用

2、Allure常用装饰器的作用：feature、step、attach等

3、Allure常用装饰器的使用
## 邮件通知
### 添加收件人列表
config/config.ini文件EMIAL（section）下的to（option）后添加邮箱，以英文分号";"分隔
## 本地构建
python run.py ${env} ${test_path} --alluredir allure-results

e.g. python run.py alpha testcase --alluredir allure-results
## 本地报告生成
allure generate allure-results -o allure-results/html --clean

直接用浏览器打开：allure-results/html/index.html