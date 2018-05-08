# selenium_test

## 功能

* 使用python的selenium库在UI层进行自动化测试solval
* tmp文件夹下为简化的功能个实现
* 具体实现使用POM模式(Page Object Model)进行设计完成

### case文件夹下编写各测试用例

    test.py

### common文件夹下为通用方法

* CommonConfiguration.py

        baseUrl
        getCurrentTime
        timeDiff

* LogUtility.py

        CreateLoggerFile
        Log

* ResultFolder.py

        GetRunDirectory

* TestCaseInfo.py

        TestCaseInfo

### page文件夹下为各个页面对应的page class

    由于页面较多且构成该页面的元素较多,目前只完成了少部分
* browser.py

        基础登录页面及组成元素

* Configuration.py

        discover node
        delete node

* Network.py

        create service

### 其他

    webAutomation.py用于读取testcases.txt中写入的测试用例文件名
    按顺序进行多个测试的执行并生成测试用例报告
