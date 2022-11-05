## 前情提要

腾讯云函数中事件函数相对特殊，只能在腾讯云服务中部署

这不，为了以后可以自行在本地部署曾经在腾讯云的服务

所以，搞了个这个

## 说明

`Flask.py`是启动文件，里头还有一大堆未引用的import，我个人对Flask不是很熟悉，届时会改

API的编写是模块化的，你可以任意在什么文件夹下编写或搬迁你的API，此处位于`Routes`

API注册可以在任何被执行的文件中注入，此处位于`index.py`如下所示:

```
from Controler.Plugin import Manager
Manager.register("Routes.debug")
Manager.register("Routes.err")
Manager.register("Routes.base64")
```

和import一致的调用方式，简单粗暴加载你的API

## 错误处理

在程序顶层会将所有错误进行拦截，当然你也可以在插件中拦截你的错误

顶层错误拦截log文件位于`.log/Router.log`貌似有些许问题，在修了

`.log/Plugin.log`是插件加载日志,检查是否正确加载了插件，正确不会有输出，可以自己改

## Lib

`Lib/log.py`简单的日志引入

`Lib/Network.py`简单的去SNI访问工具，SNI前置，这不就是用来直连EX，啊不，EH，啊不，Pixiv的吗

温习提示：虽然说SNI能访问了，但是请确保你的访问稳定且快速，不然体验可不好
