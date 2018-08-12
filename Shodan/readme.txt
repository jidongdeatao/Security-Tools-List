Shodan是互联网上最强大的一个搜索引擎工具。该工具不是在网上搜索网址，而是直接搜索服务器。
Shodan可以说是一款“黑暗”谷歌，一直不停的在寻找着所有和互联网连接的服务器、摄像头、打印机和路由器等。
每个月都会在大约5亿个服务器上日夜不停的搜集信息。下面将介绍Shodan工具的使用。

Shodan的官网网址是www.shodanhq.com。

如果要搜索一些东西时，在Shodan对应的文本框中输入搜索的内容。然后，单击Search按钮开始搜索。
    例如，用户想要搜索思科路由器，则在搜索框中输入Cisco，并单击Search按钮。
在使用Shodan搜索引擎中，可以使用过滤器通过缩小搜索范围快速的查询需要的东西。

在Shodan搜索时，需要注意一些过滤器命令的语法。常见的几种情况如下所示。

1. City和Country命令
使用City和Country命令可以缩小搜索的地理位置。如下所示。

    country:US表示从美国进行搜索。
    city:Memphis表示从孟斐斯城市搜索。

City和Country命令也可以结合使用。如下所示。

    country:US city:Memphis。

2. HOSTNAME命令
HOSTNAME命令通过指定主机名来扫描整个域名。

    hostname:google表示搜索google主机。

3. NET命令
使用NET命令扫描单个IP或一个网络范围。如下所示。

    net:192.168.1.10：扫描主机192.168.1.10。
    net:192.168.1.0/24：扫描192.168.1.0/24网络内所有主机。

4. Title命令
使用Title命令可以搜索项目。如下所示。

    title:“Server Room”表示搜索服务器机房信息。

5. 关键字搜索
Shodan使用一个关键字搜索是最受欢迎的方式。如果知道目标系统使用的服务器类型或嵌入式服务器名，来搜索一个Web页面是很容易的。如下所示。

    apache/2.2.8 200 ok：表示搜索所有Apache服务正在运行的2.2.8版本，并且仅搜索打开的站点。
    apache/2.2.8 -401 -302：表示跳过显示401的非法页或302删除页。

6．组合搜索
    IIS/7.0 hostname:YourCompany.com city:Boston表示搜索在波士顿所有正在运行IIS/7.0的Microsoft服务器。
    IIS/5.0 hostname:YourCompany.com country:FR表示搜索在法国所有运行IIS/5.0的系统。
    Title:camera hostname:YourCompany.com表示在某台主机中标题为camera的信息。
    geo:33.5,36.3 os:Linux表示使用坐标轴（经度33.5，纬度36.3）的形式搜索Linux操作系统。

7．其他搜索术语
    Port：通过端口号搜索。
    OS：通过操作系统搜索。
    After或Before：使用时间搜索服务。




