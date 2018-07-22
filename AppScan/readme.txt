AppScan使用教程
  1.安装与破解 
   IBM官方下载;http://download2.boulder.ibm.com ... 2-AppScan_Setup.exe
    本连接为7.8 简体中文版本的
   破解补丁；http://www.vdisk.cn/down/index/4760606A4753
     破解补丁中有相应的注册机与破解步骤，生成注册码做一下替换就OK了，这里不细说
   这个版本还是偏老
  2.简单的图文教程：参照这篇博文：http://www.cnblogs.com/fnng/archive/2012/10/09/2717568.html
  总体来说，AppScan的使用比较傻瓜式
  
AppScan的工作原理：
 1）通过探索（爬行）发现整个Web应用结构
 2）根据分析，发送修改的Http Request进行攻击尝试（扫描规则库）
 3）通过对于Response的分析验证是否存在安全漏洞。
 
  主要来讲下如何分析AppScan的扫描结果，毕竟大部分扫描的结果均是误报的情况比较多

 1.先看【推理】，了解判断该处为漏洞的原理，方便研究问题是否误报，问题如何解决
 2.再看【差异】，差异中描述的是AppScan对原始的request做了哪些改动，帮助理解其推理过程。
    这时显示的某些参数是经URL编码的，可以用【工具】-【powertools】-【encode/decode】工具解码后查看
 3.结合原始request、测试request、【推理】、【差异】，分析测试request中造成AppScan判定该漏洞的原因。
    再结合产品实际响应规则，判断是否存在所报漏洞。
 4.如果实际分析过程中想要实时测试并查看request和response内容，帮助理解，可以设置通信代理用fiddler来
   查看中间交互的数据。
    操作：1）打开【配置】->【通信和代理】->【使用定向代理】为127.0.0.1 端口8888
         2）打开fiddler的tools选项卡，选择tools option，配置connections中的port为8888.
            若被测试产品采用https连接，则配置https选项卡勾选decrypt https traffic，并确定。
            在fiddler界面上单击decode按钮，就可以实时重测分析来。
