项目描述:
		使用selenium操作浏览器进行网站截图

项目依赖：
		由于依赖于浏览器，需要在服务器上安装Chrome以及驱动
		同时需要安装其他依赖，才可以安装selemium

> 查看服务器版本

`cat /etc/redhat-release`

```shell
CentOS Linux release 7.8.2003 (Core)
```

可以看到现在的版本是centos7.8

> 安装Chrome

[下载链接](https://www.chrome64bit.com/index.php/google-chrome-64-bit-for-linux)

![image-20201226135803684](/Users/wangodong/Library/Application Support/typora-user-images/image-20201226135803684.png)

`下载完成之后，上传到服务器`

`安装`

```shell
yum install -y google-chrome-stable_current_x86_64.rpm

# 安装其他依赖库
yum install -y mesa-libOSMesa-devel gnu-free-sans-fonts wqy-zenhei-fonts
```

`查看安装后的版本`

```shell
google-chrome --version
Google Chrome 87.0.4280.88
```

> 安装浏览器驱动

[下载链接(淘宝源)](https://npm.taobao.org/mirrors/chromedriver)

找到对应的版本，我的是`Google Chrome 87.0.4280`

![image-20201226141722824](/Users/wangodong/Library/Application Support/typora-user-images/image-20201226141722824.png)

`同样将文件上传到服务器并且进行解压，解压之后将文件复制或者是移动到/usr/bin目录下`

```shell
unzip chromedriver_linux64.zip
cp chromedriver /usr/bin
```

> 安装selenium

```python
pip3 install selenium
```

> 测试是否可以使用

```python
from selenium import webdriver

option = webdriver.ChromeOptions()
# 无头模式
option.add_argument('headless')
# 沙盒模式运行
option.add_argument('no-sandbox')
# 大量渲染时候写入/tmp而非/dev/shm
option.add_argument('disable-dev-shm-usage')
# 指定驱动路径
browser = webdriver.Chrome('/usr/bin/chromedriver',options=option)
# 访问百度
browser.get('http://www.baidu.com/')
# 打印标题
print(browser.title)
# 关闭浏览器
browser.quit()
```

`当看到打印百度一下，你就知道的时候，就是安装成功了`


