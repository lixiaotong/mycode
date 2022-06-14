# html meta标签 整理精炼

## 理论：
meta标签共有两个属性，分别是http-equiv属性和name属性

http-equiv属性

http-equiv顾名思义，相当于http的文件头作用。相当于HTTP的作用，比如说定义些HTTP参数啥的。

meta标签中http-equiv属性语法格式是：
`<meta http-equiv="参数" content="具体的描述">`
name属性格式： 
`<meta name="参数" content="具体的描述">`


## 关于网络
一般html页面中的a标签会自动启用dns提前解析来提升网站性能，但是在使用https协议的网站中失效了，所以要设置
`<meta http-equiv="x-dns-prefetch-control" content="on">`

## 用于渲染
说明：用于设定网页字符集，便于浏览器解析与渲染页面举例：

`<meta http-equiv="content-Type" content="text/html;charset=utf-8">` //旧的HTML，不推荐 

`<meta charset="utf-8">` HTML5设定网页字符集的方式推荐使用UTF-8 

X-UA-Compatible(浏览器采取何种版本渲染当前页面)
说明：用于告知浏览器以何种版本来渲染页面。（一般都设置为最新模式，在各大框架中这个设置也很常见。）举例： 

<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>//指定IE和Chrome使用最新版本渲染当前页面

refresh(自动刷新并指向某页面)
说明：网页将在设定的时间内，自动刷新并调向设定的网址。举例: -->
<meta http-equiv="refresh" content="2；URL=http://www.lxxyx.win/">//意思是2秒后跳转向我的博客
（注意后面的分号，分别在秒数的后面和网址的前面，URL可为空）
注意：其中的2是指停留2秒钟后自动刷新到URL网址。 

　　浏览器将在60秒后，自动转向到new.htm。你可以利用这个功能，制作一个封面，在若干时间后，自动带读者来到你的目录页。
　　如果URL项没有，浏览器就是刷新本页。这就实现了WWW聊天室定期刷新的特性。

<!-- 设置移动端窗口： -->
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- viewport：能优化移动浏览器的显示。如果不是响应式网站，不要使用initial-scale或者禁用缩放。
大部分4.7-5寸设备的viewport宽设为360px；5.5寸设备设为400px；iphone6设为375px；ipone6 plus设为414px。 -->

<meta name="viewport" content="width=device-width, initial-scale=1.0,maximum-scale=1.0, user-scalable=no"/>
<!-- `width=device-width` 会导致 iPhone 5 添加到主屏后以 WebApp 全屏模式打开页面时出现黑边  -->

<!-- width：宽度（数值 / device-width）（范围从200 到10,000，默认为980 像素）
height：高度（数值 / device-height）（范围从223 到10,000）
initial-scale：初始的缩放比例 （范围从>0 到10）
minimum-scale：允许用户缩放到的最小比例
maximum-scale：允许用户缩放到的最大比例
user-scalable：用户是否可以手动缩 (no,yes)
minimal-ui：可以在页面加载时最小化上下状态栏。（已弃用）

注意，很多人使用initial-scale=1到非响应式网站上，这会让网站以100%宽度渲染，用户需要手动移动页面或者缩放。如果和initial-scale=1同时使用user-scalable=no或maximum-scale=1，则用户将不能放大/缩小网页来看到全部的内容。 -->

<!-- renderer(双核浏览器渲染方式)

说明：renderer是为双核浏览器准备的，用于指定双核浏览器默认以何种方式渲染页面。比如说360浏览器。举例： -->

<meta name="renderer" content="webkit"> //默认webkit内核
<meta name="renderer" content="ie-comp"> //默认IE兼容模式
<meta name="renderer" content="ie-stand"> //默认IE标准模式




## 用于缓存
指导浏览器如何缓存某个响应以及缓存多长时间。
`<meta http-equiv="cache-control" content="no-cache">`
共有以下几种用法：
no-cache: 先发送请求，与服务器确认该资源是否被更改，如果未被更改，则使用缓存。
no-store: 不允许缓存，每次都要去服务器上，下载完整的响应。（安全措施）
public: 缓存所有响应，但并非必须。因为max-age也可以做到相同效果
private: 只为单个用户缓存，因此不允许任何中继进行缓存。（比如说CDN就不允许缓存private的响应）
maxage: 表示当前请求开始，该响应在多久内能被缓存和重用，而不去服务器重新请求。例如：max-age=60表示响应可以再缓存和重用 60 秒。 

expires(网页到期时间)HTM清除缓存  
说明:用于设定网页的到期时间，过期后网页必须到服务器上重新传输。注意：必须使用GMT的时间格式。举例： 
`<meta http-equiv="expires" content="Sunday 26 October 2016 01:00 GMT" />`
`<META HTTP-EQUIV=”expires” CONTENT=”Wed, 26 Feb 1997 08:21:57 GMT”>`
`<META HTTP-EQUIV=”expires” CONTENT=”0″>`

禁止缓存的实践角度就这三句： 
`<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />`
`<META http-equiv="Pragma" CONTENT="no-cache">`<!-- 禁止浏览器从本地计算机的缓存中访问页面内容，这样设定，访问者将无法脱机浏览。 -->
`<meta http-equiv="Expires" content="0" />`

Set-Cookie(cookie设定)
说明：如果网页过期。那么这个网页存在本地的cookies也会被自动删除。 -->
<meta http-equiv="Set-Cookie" content="name, date">//格式
<meta http-equiv="Set-Cookie" content="User=Lxxyx; path=/; expires=Sunday, 10-Jan-16 10:00:00 GMT"> //具体范例>

## 用于防护

禁止百度自动转码
说明：用于禁止当前页面在移动端浏览时，被百度自动转码。转码效果很多时候却不尽人意。所以可以在head中加入就能禁止转码了。举例： 
`<meta http-equiv="Cache-Control" content="no-siteapp"/>`
控制网页窗口 强制页面在当前窗口中以独立页面显示 防止网页被别人作为一个Frame调用。
`<meta http-equiv="window-target" content="_top">`



## 待测试
<meta http-equiv="Pics-label" content="">
网页等级评定，在IE的internet选项中有一项内容设置，可以防止浏览一些受限制的网站，而网站的限制级别就是通过meta属性来设置的； 
<meta http-equiv="Page-Enter" content="revealTrans（duration=10,transtion= 50）">
和<meta http-equiv="Page-Exit" content="revealTrans（duration=20，transtion=6）">
设定进入和离开页面时的特殊效果，这个功能即FrontPage中的"格式/网页过渡"，不过所加的页面不能够是一个frame页面。 




## 面向搜索引擎： 
<meta name="robots" content="none">
<meta name="google" content="index,follow" />
<meta name="googlebot" content="index,follow" />
<meta name="verify" content="index,follow" />
定义搜索引擎爬虫的索引方式
说明：robots用来告诉爬虫哪些页面需要索引，哪些页面不需要索引。
content的参数有all,none,index,noindex,follow,nofollow。

默认是all。  

具体参数如下：
1.none : 搜索引擎将忽略此网页，等价于noindex，nofollow。
2.noindex: 搜索引擎不索引此网页。
3.nofollow: 搜索引擎不继续通过此网页的链接索引搜索其它的网页。
4.all: 搜索引擎将索引此网页与继续通过此网页的链接索引，等价于index，follow。
5.index : 搜索引擎索引此网页。
6.follow : 搜索引擎继续通过此网页的链接索引搜索其它的网页。

<meta name="keywords" content="灵机, 网络, 网站, 程序"> 网页的关键字  
<meta name="description" content="编程工具网站">
网站内容描述（description）的设计要点：
①网页描述为自然语言而不是罗列关键词（与keywords设计正好相反）；
②尽可能准确地描述网页的核心内容，通常为网页内容的摘要信息，也就是希望搜索引擎在检索结果中展示的摘要信息；
③网页描述中含有有效关键词；
④网页描述内容与网页标题内容有高度相关性；
⑤网页描述内容与网页主体内容有高度相关性；
⑥网页描述的文字不必太多，一般不超过搜索引擎检索结果摘要信息的最多字数（通常在100中文字之内，不同搜索引擎略有差异）。
举例：<meta name="description" content="This page is about the meaning of science,education,culture."> 

<meta name="revisit-after" content="7 days" >
<!-- 设置一个爬虫的重访时间。如果重访时间过短，爬虫将按它们定义的默认时间来访问 -->



## 关于webapp
WebApp全屏模式：伪装app，离线应用。
<meta name="apple-mobile-web-app-capable" content="yes" /> <!-- 启用 WebApp 全屏模式 -->
隐藏状态栏/设置状态栏颜色：只有在开启WebApp全屏模式时才生效。content的值为default | black | black-translucent 。
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
添加到主屏后的标题
<meta name="apple-mobile-web-app-title" content="标题">
添加智能 App 广告条 Smart App Banner：告诉浏览器这个网站对应的app，并在页面上显示下载banner(如下图)。
<meta name="apple-itunes-app" content="app-id=myAppStoreID, affiliate-data=myAffiliateData, app-argument=myURL">


## 其他无功能性设置：

<!-- 用于标注网页作者举例： -->
<meta name="author" content="StephenLee, 276125681@qq.com">
<!-- 用于标注copyright(版权) -->
<meta name="copyright" content="StephenLee">

<!-- 针对手持设备优化，主要是针对一些老的不识别viewport的浏览器，比如黑莓 -->
<meta name="HandheldFriendly" content="true">
<!-- 微软的老式浏览器 -->
<meta name="MobileOptimized" content="320">
<!-- uc强制竖屏 -->
<meta name="screen-orientation" content="portrait">
<!-- QQ强制竖屏 -->
<meta name="x5-orientation" content="portrait">
<!-- UC强制全屏 -->
<meta name="full-screen" content="yes">
<!-- QQ强制全屏 -->
<meta name="x5-fullscreen" content="true">
<!-- UC应用模式 -->
<meta name="browsermode" content="application">
<!-- QQ应用模式 -->
<meta name="x5-page-mode" content="app">
<!-- windows phone 点击无高光 -->
<meta name="msapplication-tap-highlight" content="no">

<meta name="msapplication-TileColor" content="#000"/> <!-- Windows 8 磁贴颜色 -->
<meta name="msapplication-TileImage" content="icon.png"/> <!-- Windows 8 磁贴图标 -->

<!-- 忽略数字自动识别为电话号码 -->
<meta content="telephone=no" name="format-detection" />

<!-- 忽略识别邮箱 -->
<meta content="email=no" name="format-detection" />




