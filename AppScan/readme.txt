AppScan使用教程

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
