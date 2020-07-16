苏宁开放平台Python-SDK，beta版

参考了淘宝sdk的设计结构。

关于平台地址以及appkey和appsecret等的配置可以修改suning.api.config.py 文件

使用方法见test包中的test.py等测试代码

以上是原版`suning-sdk-python`的`README.md`，苏宁的`python sdk`支持`python2.7`及以上

原版下载地址：[SDK下载](http://open.suning.com/ospos/apipage/downLoadSDK.do?sdkType=python)

---

## 创建轮子的原因：

由于自己的其他项目需要，觉得建一个轮子的方式比丢进自己的代码里更好，然而`pip`里竟然没有！所以建了这个轮子。

## 关于包的安装：

```
pip install suning-sdk
或
pip3 install suning-sdk
```

## 关于包的引用及示例

我们以调用[suning.netalliance.recommendcommodity.query](https://open.suning.com/ospos/apipage/toApiMethodDetailMenuNew.do?interCode=suning.netalliance.recommendcommodity.query)为例

```
import suning.api as api
try:
	client = api.RecommendcommodityQueryRequest()
	client.setDomainInfo("openpre.cnsuning.com", "80")
	client.setAppInfo('你申请到的appKey', '你申请到的secretKey')
	client.couponMark = '1'
	resp = client.getResponse()
except Exception as e:
	print(e)
```

更多示例请参考官方的SDK下的`test`目录或直接查看：[https://github.com/why2ly/suning-sdk/test](https://github.com/why2ly/suning-sdk/tree/master/test)

接口的具体说明请查看：[苏宁开放平台API文档](https://open.suning.com/ospos/apipage/toApiMethodDetailMenuNew.do)

## 关于更新：

如果版本落后苏宁官网，请主动前往：[项目github](https://github.com/why2ly/suning-sdk/)提`issue`或`PR`

没`issue`或`PR`就不更新了

## 关于版本

| 版本号 | 苏宁官方sdk下载日期 | 
| -------- | -------------- | 
| 0.1.0 | 2020-07-15 | 

 