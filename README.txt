# Security-Tools-List
被动情报收集工具：Shodan、Google Hacking、ZoomEye、whois、nslookup、DNSDomain(这三个通过站长工具查询)
主动情报收集工具：Nmap、Netcat
漏洞扫描器：Nessus、OpenVAS、Nexpose
ARP毒化工具：Arpspoof
网络流量分析工具：Wireshark、tcpdump
破解密码工具：Medusa、THC-hydra、Hashcat、
WEB安全扫描工具：AppScan、W3af、AWVS、Webscanner
目录遍历工具；DirBuster
Fuzz模糊测试工具：Peach
WEB渗透工具：Burpsuite
XSS漏洞检测工具：BruteXSS、XSSer
二进制/源码静态扫描工具：Checkmarx、Woodpecker、codeDEX
漏洞靶场：DVWA
无线渗透工具：Aircrack-ng
渗透后利用工具：Metasploit

渗透流程：
1.被动情报收集: 
  这步还不会直接对被测⽬目标进⾏行行扫描，应当先从⽹网络上搜索⼀一些相关信息，包括 Google Hacking， Whois查询， DNS等信息(如果考虑进⾏行行社会⼯工程学的话，这⾥里里 还可以相应从邮件列列表/新闻组中获取⽬目标系统中⼀一些边缘信息如内部员⼯工帐号组 成，⾝身份识别⽅方式，邮件联系 地址等)。
    1.使⽤用whois查询⽬目标域名的DNS服务器 2.nslookup
    >set type=all ><domain>
    >server <ns server> >set q=all
    >ls -d <domain>
    涉及的⼯工具包 括:Google,Demon,webhosting。info,Apollo,Athena,GHDB.XML,netcraft,seologs  除此之外，我想特别提醒⼀一下使⽤用Googlebot/2.1绕过⼀一些⽂文件的获取限制。

    Google hacking 中常⽤用的⼀一些语法描述 
    ⽬目标系统信息收集: 通过上⾯面⼀一步，我们应当可以简单的描绘出⽬目标系统的⽹网络结构，如公司⽹网络所在区 域，⼦子公司IP地址分布，VPN接入地址等。这⾥里里特别要注意⼀一些比较偏⻔门的 HOST名称地址，如⼀一些backup开头或者temp开关的域名很可能就是⼀一台备份服务器，其安全性很可能做的不够。 从获取的地址列列表中进⾏行行系统判断，了解其组织架构及操作系统使⽤用情况。最常⽤用的方法的是目标所有IP⽹网段扫描。
    
2.主动情报收集：端⼝口/服务信息收集: 这⼀一部分已经可以开始直接的扫描操作，涉及的⼯工具包括:nmap,thc-amap
    1.我最常使⽤用的参数
    nmap -sS -p1-10000 -n -P0 -oX filename.xml --open -T5 <ip address>
      应⽤用信息收集:httprint，SIPSCAN，smap 这⾥里里有必要将SNMP拿出来单独说⼀一下，因为⽬目前许多运营商、⼤大型企业内部⽹网络的
    维护台通过SNMP进⾏行行数据传输，⼤大部分情况是使⽤用了了默认⼝口令的
    
3.漏洞扫描
漏洞扫描器：Nessus、OpenVAS、Nexpose
有时候，通过服务/应⽤用扫描后，我们可以跳过漏洞洞扫描部分，直接到漏洞洞利利⽤用。因为很多 情况下我们根据⽬目标服务/应⽤用的版本就可以到⼀一些安全⽹网站上获取针对该⽬目标系统的漏洞利⽤用代码，如milw0rm, securityfocus,packetstormsecurity等网站，上⾯面都对应有搜索模块。实在没有，我们也可以尝试在GOOGLE上搜索“应⽤用名称 exploit”、“应⽤用名称 vulnerability”等关键字。
当然，⼤大部分情况下你都可以不这么⿇麻烦，网络中有⼀一些⼯工具可供我们使⽤用，最著名的当属metasploit了了，它是⼀一个开源免费的漏洞洞利利⽤用攻击平台。其他的多说⽆无益，您就看它从榜上⽆无名到冲进前五(top 100)这⼀一点来说，也能⼤大概了了解到它的威⼒力力了了。除此之外，如果您 (您们公司)有⾜足够的moeny⽤用于购买商⽤用软件的话，CORE IMPACT是相当值得考虑的， 虽然说价格很⾼高，但是它却是被业界公认在渗透测试⽅方⾯面的泰⼭山北⽃斗，基本上测试全⾃自动。 如果您觉得还是接受不了了，那么您可以去购买CANVAS，据说有不少0DAY，不过它跟 metasploit⼀一样，是需要⼿手动进⾏行行测试的。最后还有⼀一个需要提及⼀一下的 Exploitation_Framework，它相当于⼀一个漏洞洞利利⽤用代码管理理⼯工具，⽅便进⾏行不同语⾔言不同平台的利利⽤用代码收集，把它也放在这⾥里里是因为它本⾝身也维护了了⼀一个exploit库，⼤大家参考着也能使用。

上⾯面提到的是针对系统进行的，
在针对WEB⽅面，注入⼯工具有NBSI, OWASP SQLiX, SQL Power Injector, sqlDumper, sqlninja, sqlmap, Sqlbftools, priamos, ISR-sqlget***等等。
在针对数据库⽅方⾯面的⼯工具有:
    Oracle(1521端口): 目前主要存在以下⽅面的安全问题:
        1、TNS监听程序攻击(sid信息泄露,停⽌止服务等) 
        2、默认账号(default password list)
        3、SQL INJECTION(这个与传统 的意思还不太⼀一样) 
        4、缓冲区溢出，现在比较少了了。
          漏洞利用工具：thc-orakel, tnscmd, oscanner, Getsids, TNSLSNR, l snrcheck, OAT, Checkpwd, orabf        
    MS Sql Server(1433、1434端⼝口 )
    Mysql(3306端⼝口)
    DB2(523、50000、50001、5000 2、50003端⼝口)
      利用工具：db2utils
 
在针对Web服务器⽅方⾯面的⼯工具有:

  IIS：IISPUTSCANNER
  Tomcat：想起/admin和/manager管理理⽬录了吗?另外，目录列列表也是Tomcat服务器中最常⻅的问题。比如5.*版本中的
http://127.0.0.1/;index.jsp http://www.example.com/foo/"../ma nager/html http://www.example.com:8080/exa mples/servlets/servlet/CookieExam ple?cookiename=HAHA&cookievalu
   e=%5C%22FOO%3B+Expires%3D Thu%2C+1+Jan+2009+00%3A00%
  3A01+UTC%3B+Path%3D%2F%3 B http://www.example.com:8080/servl
   ets-examples/servlet/CookieExample?cookiename=BLOCKER&cookiev alue=%5C%22A%3D%27%3B+Expires%3DThu%2C+1+Jan+2009+00%3A00%3A01+UTC%3B+Path%3 D%2Fservlets-examples%2Fservlet+%3B
JBOSS：jboss的漏洞洞很少，老版本中8083端口有%符号的漏洞洞:
    GET %. HTTP/1.0可以获取物理理路路径 信息，
    GET %server.policy HTTP/1.0可以获 取安全策略略配置⽂文档。 你也可以直接访问GET %org/xxx/lib. class来获取编译好的java程序，再使 ⽤用⼀一些反编译⼯工具还原源代码。
 Apache
 Resin
http://victim/C:%5C/
http://victim/resin-doc/viewfile/?file=
 index.jsp
http://victim/resin-doc/viewfile/?con textpath=/otherwebapp&servletpath =&file=WEB-INF/web.xml http://victim/resin-doc/viewfile/?con textpath=/&servletpath=&file=WEB-I NF/classes/com/webapp/app/target .class http://victim/[path]/[device].[extensio n]
http://victim/%20.."web-inf
http://victim/%20
http://victim/[path]/%20.xtp
 WebLogic
Web安全测试主要围绕⼏几块进⾏行行:
  Information Gathering:也就是⼀一般的信息泄漏，包括异常情况下的路径泄漏、⽂件归档查找等
  Business logic testing:业务逻辑处理理攻击，很多情况下⽤用于⾏行行业务绕过或者欺骗 等等
  Authentication Testing:有⽆无验证码、有⽆无次数限制等，总之就是看能不能暴暴⼒力力破解 或者说容不容易易通过认证，比较直接的就是“默认⼝口令”或者弱⼝口令了了
  Session Management Testing:会话管理理攻击在COOKIE携带认证信息时最有效 Data Validation Testing:数据验证最好理理解了了，就是SQL Injection和Cross Site Script等等
⽬目前⽹网上能够找到许多能够⽤用于进⾏行行Web测试的⼯工具，根据不同的功能分主要有:
1. 枚举(Enumeration): DirBuster, http-dir-enum, wget
2. 基于代理理测试类⼯工具:paros, webscarab, Burp Suite
针对WebService测试的部分有⼀一些尚不是很成熟的⼯工具， 如:wsbang，wschess，wsmap，wsdigger，wsfuzzer
这⼀一部分值得⼀一提的是，很多渗透测试团队都有着⾃自⼰己的测试⼯工具甚⾄至是0DAY代码，最常 ⻅见的是SQL注入⼯工具，现⽹网开发的注入⼯工具(如NBSI等) ⽬目前都是针对中⼩小企业或者是个 ⼈人站点/数据库进⾏行行的，针对⼤大型⽬目标系统使⽤用的⼀一些相对比较偏⻔门的数据库系统(如 INFORMIX，DB2)等，基本上还不 涉及或者说还不够深入。这时各渗透测试团队就开发了了 满⾜足⾃自⾝身使⽤用习惯的测试⼯工具。
在针对⽆无线环境的攻击有:WifiZoo 
4、权限提升
在前⾯面的⼀一些⼯工作中，你或许已经得到了了⼀一些控制权限，但是对于进⼀一步攻击来说却还是不 够。例例如:你可能很容易易的能够获取Oracle数据库的访问权 限，或者是得到了了 UNIX(AIX,HP-UX,SUNOS)的⼀一个基本账号权限，但是当你想进⾏行行进⼀一步的渗透测试的时候 问题就来了了。你发现你没有⾜足够的 权限打开⼀一些密码存储⽂文件、你没有办法安装⼀一个 SNIFFER、你甚⾄至没有权限执⾏行行⼀一些很基本的命令。这时候你⾃自然⽽而然的就会想到权限提升 这个途径了了。
⽬目前⼀一些企业对于补丁管理理是存在很⼤大⼀一部分问题的，他们可能压根就没有想过对⼀一些服务 器或者应⽤用进⾏行行补丁更更新，或者是延时更更新。这时候就是渗透测试⼈人员的好机会了了。经验之 谈:有⼀一般权限的Oracle账号或者AIX账号基本上等于root，因为这就是现实⽣生活。
5、密码破解
有时候，⽬目标系统任何⽅方⾯面的配置都是⽆无懈可击的，但是并不是说就完全没办法进入。最简 单的说，⼀一个缺少密码完全策略略的论证系统就等于你安装了了⼀一个不 能关闭的防盗⻔门。很多 情况下，⼀一些安全技术研究⼈人员对此不屑⼀一顾，但是⽆无数次的安全事故结果证明，往往破坏 ⼒力力最⼤大的攻击起源于最⼩小的弱点，例例如弱⼝口令、⽬目 录列列表、SQL注入绕过论证等等。所以 说，对于⼀一些专⻔门的安全技术研究⼈人员来说，这⼀一块意义不⼤大，但是对于⼀一个ethical hacker来说，这⼀一步骤是有必要⽽而且绝⼤大部分情况下是必须的。;)
⽬目前比较好的⽹网络密码暴暴⼒力力破解⼯工具有:thc-hydra，brutus
⽬目前⽹网络中有⼀一种资源被利利⽤用的很⼴广泛，那就是rainbow table技术，说⽩白了了也就是⼀一个 HASH对应表，有⼀一些⽹网站提供了了该种服务，对外宣称存储空间⼤大于多少G，像
>hydra.exe -L users.txt -P passwords.txt -o test.txt -s 2121 www.nosec.org ftp
rainbowcrack更更是对外宣称其数据量量已经⼤大于1.3T。 针对此种⽅方式对外提供在线服务的有:
     rainbowcrack
   ⾥里里⾯面对应了了多种加密算法的HASH。
     http://gdataonline.com/seekhash
    .php
   http://www.milw0rm.com/cracker
      /info.php
   http://www.hashchecker.com/?_s
      ls=search_hash
      http://bokehman.com/cracker/
       http://passcracking.ru/
          http://md5.neeao.com/
  国内⼈人员提供的在线MD5检查平台，据说已集成了了⼀一 些其他⽹网站的HASH结果。
   http://www.cmd5.com/
有些单机破解软件还是必不可少的:Ophcrack，rainbowcrack(国⼈人开发，赞⼀一 个)，cain，L0phtCrack(破解Windows密码)，John the Ripper(破解UNIX/LINUX)密 码，当然，还少不了了⼀一个FindPass...
针对⽹网络设备的⼀一些默认帐号，
  你可以查询http://www.routerpasswords.com/
  http://www.phenoelit-us.org/dpl/dpl.html
在渗透测试过程中，⼀一旦有机会接触⼀一些OFFICE⽂文档，且被加了了密的话，那么，rixler是您 ⻢马上要去的地⽅方，他们提供的OFFICE密码套件能在瞬间打开OFFICE⽂文档(2007中我没有 试过，⼤大家有机会测试的话请给我发⼀一份测试结果说明，谢谢)。看来微软有理理由来个补丁 什什么的了了。对于企业来说，您可以考虑使⽤用铁卷或者RMS了了。
6、⽇日志清除
It is not necessary actually.
7、进⼀一步渗透
攻入了了DMZ区⼀一般情况下我们也不会获取多少⽤用价值的信息。为了了进⼀一步巩固战果，我们需 要进⾏行行进⼀一步的内⽹网渗透。到这⼀一步就真的算是⽆无所不⽤用其及。 最常⽤用且最有效的⽅方式就 是Sniff抓包(可以加上ARP欺骗)。当然，最简单的你可以翻翻已入侵机器上的⼀一些⽂文件， 很可能就包含了了你需要的⼀一些连接帐 号。比如说你入侵了了⼀一台Web服务器，那么绝⼤大部分 情况下你可以在⻚页⾯面的代码或者某个配置⽂文件中找到连接数据库的帐号。你也可以打开⼀一些 ⽇日志⽂文件看⼀一看。
除此之外，你可以直接回到第⼆二步漏洞洞扫描来进⾏行行。
四、⽣成报告
报告中应当包含:
1. 薄弱点列列表清单(按照严重等级排序) 2. 薄弱点详细描述(利利⽤用⽅方法)
3. 解决⽅方法建议
4. 参与⼈人员/测试时间/内⽹网/外⽹网
五、测试过程中的⻛风险及规避
在测试过程中⽆无可避免的可能会发⽣生很多可预⻅见和不可预⻅见的⻛风险，测试⽅方必须提供规避措 施以免对系统造成重⼤大的影响。以下⼀一些可供参考:
1. 不执行任何可能引起业务中断的攻击(包括资源耗竭型DoS，畸形报文攻击，数据破 坏)。
2. 测试验证时间放在业务量最小的时间进行。
3. 测试执行前确保相关数据进行备份。
4. 所有测试在执行前和维护人员进行沟通确认。
5. 在测试过程中出现异常情况时立即停止测试并及时恢复系统。
6. 对原始业务系统进行一个完全的镜像环境，在镜像环境上进行渗透测试



参考使用Kali Linux进行渗透的流程：
GitHub：https://github.com/sysorem/Kali-Linux-Pentest-Basic
  Phase1 Reconnaissance
    1、Website & Server Info acquiring
      -Server :
      whois\host\fierce(DNS Rev)\dig\DNS transfer
      -Server/OS fingerprint
      port scan\Banner\p0f\Xprobe2\nmap
      -Waf detected
      wafw00f
    2、Search  Engine
      -Google Advanced
      -Shodan
      -Zoomeye
    3、Google Hacking(GHDB)
      -intext\allintext\intitle\cache\intitile\define\filetype\info\inurl\allinurl\+_*.""
    4、Social Media Network
      -Maltego
    5、Undisclosed Data(Social Engine Database)
      -QQGroup
  Phase2 Scanning
    1、Network traffic
      -tcp\udp\icmp
    2、Nmap
      -OS detected\TCP scan\SYN scan\ACK scan\UDP scan\Timming tpl
      -Port scan\IP scan\output
    3、Hping3
      -SYN Flood Attack(Denial of Service)
    4、Nessus
    5、whatweb
      -Gather info of Website
    6、DirBuster
      -scan the exists directories or files
    7、joomscan
      -Joomla based sites tests
    8、WPScan
      -Wordpress based sites tests
  Phase3 Gaining Access
    1、Metasploit Framework
      -Experiment:Hack Windows XP SP3 by MS08_067
      -Get shell/Remote Desktop/Remote control
    2、Sqlmap
      -SQLi Experiment:Hack a CMS Site
      -Get shell/dump database/Remote control
    3、rdesktop  + hydra
      -Forcely Brute WinXP Administrator Password
    4、Arpspoof
      -Experiment:Arp spoof Attack on LAN
      -Session Injection
    5、tcpdump + ferret + hamster
      -Experiment:Session Injection
    6、Ettercap
      -Experiment:DNS Spoof(Fishing)
    7、SET
      -With Meterpreter
  Phase4 Maintaining Access
    1、Netcat
      -Experiment:Reverse CMDshell(cmd.exe)
    2、Crytpcat
    3、weevely
      -Generated Shellcode Bypassed Anti-Virus  
      -Experiment:Break through Interception by SafetyDog
    4、cymothoa
      -Process Injection
  Phase5 Pentest Report
    1、Magictree
    2、dradis


