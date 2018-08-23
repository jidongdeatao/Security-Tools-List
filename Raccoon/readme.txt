Raccoon是一款用于侦察和漏洞扫描的高性能攻击性安全工具
来源：
https://github.com/evyatarmeged/Raccoon

特性

    1. DNS详请
    2. 使用DNS dumpster实现DNS可视化映射
    3. WHOIS信息
    4. TLS数据 – 支持的密码，TLS版本，证书详情和SAN
    5. 端口扫描
    6. 服务和脚本扫描
    7. URL fuzzing以及 目录/文件 检测
    8. 子域名枚举 – 使用Google dorking，DNS dumpster查询，SAN发现和暴破
    9. Web应用程序数据检索：
          CMS检测；
          Web服务器信息和X-Powered-By；
          robots.txt和站点地图提取；
          Cookie检查；
          提取所有fuzz URL；
          发现HTML表单；
          检索所有电子邮件地址。
    10. 检测已知的WAF
    11. 支持通过Tor/Proxies进行匿名路由
    12. 使用asyncio来提高性能
    13. 将输出保存到文件 – 通过文件夹和文件来分离目标及模块

后续将支持
    1. 支持多个主机（从文件中读取）
    2. OWASP漏洞扫描（RFI，RCE，XSS，SQp等）
    3. SearchSploit查找结果
    4. IP范围支持
    5. CIDR notation支持
    6. 更多的输出格式支持

Raccoon是一款用于侦察和信息收集的工具。它将为我们完成从获取DNS记录，TLS数据，WHOIS信息检索，WAF存在检测以及目录爆破，子域枚举等所有操作。
每次扫描结果都将会输出保存到相应的文件中。
Raccoon的大部分扫描都是独立进行的，并且也不依赖于彼此间的结果，它主要利用的是Python的asyncio来异步执行大部分的扫描。
Raccoon支持通过Tor/Proxies进行匿名路由。另外，它使用的默认字典列表来自Secpsts存储库（用于URL fuzzing和子域发现），
但你也可以将其它列表作为参数传递给它。
安装
最新稳定版的安装：
pip install raccoon-scanner
或从GitHub存储库克隆安装：
git clone https://github.com/evyatarmeged/Raccoon.git
cd Raccoon
python raccoon_src/main.py

环境要求
Raccoon端口扫描会调用Nmap，以及会用到它的一些脚本和功能。因此在运行Raccoon之前，请务必先安装Nmap。
OpenSSL在TLS/SSL扫描时会用到，因此也应该提前安装好。
使用
Usage: raccoon [OPTIONS]

Options:
  --version                      显示版本信息并退出。
  -t, --target TEXT              扫描的目标[必需]
  -d, --dns-records TEXT         逗号分隔DNS记录以进行查询。
                                 默认为：A，MX，NS，CNAME，SOA，TXT
  --tor-routing                  通过Tor路由HTTP流量（使用端口
                                 9050）。这将明显减慢总运行时间。
  --proxy-pst TEXT              用于路由HTTP流量的代理列表文件的路径。
                                 对于每个请求，将随机选择列表中的代理。
                                 这将明显减慢总运行时间。
  --proxy TEXT                   用于路由HTTP流量的代理地址。
                                 这将明显减慢总运行时间。
  -w, --wordpst TEXT            用于URL Fuzzing的字典列表路径。
  -T, --threads INTEGER          用于URL Fuzzing/子域名枚举的线程数。默认为：25
  --ignored-response-codes TEXT  逗号分隔需要忽略的HTTP状态码列表。默认为:
                                 302,400,401,402,403,404,503,504
  --subdomain-pst TEXT          用于枚举的子域名列表文件路径。
  -S, --scripts                  使用-sC参数执行Nmap扫描。
  -s, --services                 使用-sV参数执行Nmap扫描。
  -f, --full-scan                使用-sV和-sC参数执行Nmap扫描。
  -p, --port TEXT                将此端口范围用于Nmap扫描替换默认值
  --tls-port INTEGER             使用此端口进行TLS查询。默认端口为：443
  --skip-health-check            不要测试目标主机可用性
  -fr, --follow-redirects        当fuzzing时遵循重定向。默认为：True
  --no-url-fuzzing               不要fuzz URLs
  --no-sub-enum                  不要爆破子域
  -q, --quiet                    不要输出到stdout
  -o, --outdir TEXT              扫描输出目录
  --help                         显示帮助信息并退出。
