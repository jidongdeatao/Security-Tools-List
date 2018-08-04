Sqlmap使用
  GitHub 官方地址：https://github.com/sqlmapproject/sqlmap

在已有python的基础上，下载，进入目录就可以使用



使用总结：
使用burpsuite抓取请求包
python sqlmap.py -l /Desktop/inject.txt
基本上扫描网站会被WAF拦截，如：
    [15:10:22] [WARNING] there is a possibility that the target (or WAF/IPS/IDS) is resetting 'suspicious' requests
    [15:10:23] [CRITICAL] WAF/IPS/IDS identified as 'Generic (Unknown)'
可以在后面加上参数 --level 3 来强制扫描
