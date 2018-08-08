# Security-Tools-List
被动情报收集工具：Google Hacking、ZoomEye、whois、nslookup、DNSDomain(这三个通过站长工具查询)
主动情报收集工具：Nmap、Netcat
漏洞扫描器：Nessus、OpenVAS、Nexpose
渗透后利用工具：Meterpreter
ARP毒化工具：Arpspoof
网络流量分析工具：Wireshark、tcpdump
暴力破解工具：Medusa、THC-hydra、
WEB安全扫描工具：AppScan
WEB渗透工具：Burpsuite
XSS漏洞检测工具：BruteXSS、XSSer
二进制/源码静态扫描工具：Checkmarx、Woodpecker、codeDEX


渗透流程：
1.被动情报收集: 
  这步还不会直接对被测⽬目标进⾏行行扫描，应当先从⽹网络上搜索⼀一些相关信息，包括 Google Hacking， Whois查询， DNS等信息(如果考虑进⾏行行社会⼯工程学的话，这⾥里里 还可以相应从邮件列列表/新闻组中获取⽬目标系统中⼀一些边缘信息如内部员⼯工帐号组 成，⾝身份识别⽅方式，邮件联系 地址等)。
 
    1.使⽤用whois查询⽬目标域名的DNS服务器 2.nslookup
    >set type=all ><domain>
    >server <ns server> >set q=all
    >ls -d <domain>
    涉及的⼯工具包 括:Google,
    Demon,
    webhosting。info,Apollo,Athena,GHDB.XML,
    netcraft,
    seologs  除此之外，我想特别提醒⼀一下使⽤用Googlebot/2.1绕过⼀一些⽂文件的获取限制。

    Google hacking 中常⽤用的⼀一些语法描述 
    ⽬目标系统信息收集: 通过上⾯面⼀一步，我们应当可以简单的描绘出⽬目标系统的⽹网络结构，如公司⽹网络所在区 域，⼦子公司IP地址分布，VPN接入地址等。这⾥里里特别要注意⼀一些比较偏⻔门的 HOST名称地址，如⼀一些backup开头或者temp开关的域名很可能就是⼀一台备份服务器，其安全性很可能做的不够。 从获取的地址列列表中进⾏行行系统判断，了解其组织架构及操作系统使⽤用情况。最常⽤用的方法的是目标所有IP⽹网段扫描。
    
2.主动情报收集：端⼝口/服务信息收集: 这⼀一部分已经可以开始直接的扫描操作，涉及的⼯工具包括:nmap,thc-amap

    1.我最常使⽤用的参数
    nmap -sS -p1-10000 -n -P0 -oX filename.xml --open -T5 <ip address>
      应⽤用信息收集:httprint，SIPSCAN，smap 这⾥里里有必要将SNMP拿出来单独说⼀一下，因为⽬目前许多运营商、⼤大型企业内部⽹网络的
    维护台通过SNMP进⾏行行数据传输，⼤大部分情况是使⽤用了了默认⼝口令的
    
    
3.漏洞扫描
