Nmap使用：

  Nmap GitHub上就可以下载：https://github.com/nmap/nmap
  安装过程也比较简单：
    对于MAC/LInux使用编译安装：
        ./configure
        make
        make install
        
        
  Nmap的常用命令规则：
 用法：nmap [扫描类型] [选项] {目标}
目标：
  可以传递主机名，IP地址，网络等。
  例如：scanme.nmap.org，microsoft.com / 24,192.168.0.1; 10.0.0-255.1-254
  -iL <inputfilename>：从主机/网络列表输入
  -iR <num hosts>：选择随机目标
  --exclude <host1 [，host2] [，host3]，...>：排除主机/网络
  --excludefile <exclude_file>：从文件中排除列表
主机发现：
  -sL：列表扫描 - 只列出要扫描的目标
  -sn：Ping扫描 - 禁用端口扫描
  -Pn：将所有主机视为在线 - 跳过主机发现
  -PS / PA / PU / PY [端口列表]：TCP SYN / ACK，UDP或SCTP发现到给定端口
  -PE / PP / PM：ICMP回送，时间戳和网络掩码请求发现探测
  -PO [协议列表]：IP协议Ping
  -n / -R：从不进行DNS解析/始终解析[默认：有时]
  --dns-servers <serv1 [，serv2]，...>：指定自定义DNS服务器
  --system-dns：使用OS的DNS解析器
  --traceroute：每个主机的跟踪跳转路径
扫描技术：
  -sS / sT / sA / sW / sM：TCP SYN / Connect（）/ ACK / Window / Maimon扫描
  -sU：UDP扫描
  -sN / sF / sX：TCP Null，FIN和Xmas扫描
  --scanflags <flags>：自定义TCP扫描标志
  -sI <zombie host [：probeport]>：空闲扫描
  -sY / sZ：SCTP INIT / COOKIE-ECHO扫描
  -sO：IP协议扫描
  -b <FTP中继主机>：FTP反弹扫描
端口扫描命令：
  -p <端口范围>：仅扫描指定的端口
    例如：-p22; -p1-65535; -p U：53,111,137，T：21-25,80,139,8080，S：9
  -F：快速模式 - 扫描比默认扫描更少的端口
  -r：连续扫描端口 - 不要随机化
  --top-ports <number>：扫描<number>最常见的端口
  --port-ratio <ratio>：扫描端口比<ratio>更常见
服务/版本检测：
  -sV：探测开放端口以确定服务/版本信息
  --version-intensity <level>：从0（亮）到9（尝试所有探针）设置
  --version-light：限制最可能的探针（强度2）
  --version-all：尝试每一个探针（强度9）
  --version-trace：显示详细的版本扫描活动（用于调试）
脚本扫描：
  -sC：相当于--script = default
  --script = <Lua scripts>：<Lua scripts>是逗号分隔的列表
           目录，脚本文件或脚本类别
  --script-args = <n1 = v1，[n2 = v2，...]>：为脚本提供参数
  --script-trace：显示发送和接收的所有数据
  --script-updatedb：更新脚本数据库。
操作系统检测：
  -O：启用OS检测
  --osscan-limit：将OS检测限制为有希望的目标
  --osscan-guess：更积极地猜测操作系统
时间和性能：
  采用<time>的选项以秒为单位，或追加'ms'（毫秒），
  该值的's'（秒），'m'（分钟）或'h'（小时）（例如30m）。
  -T <0-5>：设置时序模板（越高越快）
  --min-hostgroup / max-hostgroup <size>：并行主机扫描组大小
  --min-parallelism / max-parallelism <numprobes>：探测并行化
  --min-rtt-timeout / max-rtt-timeout / initial-rtt-timeout <time>：指定
      探测往返时间。
  --max-retries <tries>：端口扫描探测重新传输的上限数量。
  --host-timeout <time>：在此之后放弃目标
  --scan-delay /  -  max-scan-delay <time>：调整探针之间的延迟
  --min-rate <number>：发送数据包的速度不低于每秒<number>
  --max-rate <number>：发送数据包的速度不超过每秒<number>
防火墙/ IDS逃脱和防御：
  -F; --mtu <val>：分段数据包（可选地，具有给定的MTU）
  -D <decoy1，decoy2 [，ME]，...>：用诱饵披露扫描
  -S <IP_Address>：欺骗源地址
  -e <iface>：使用指定的接口
  -g /  -  source-port <portnum>：使用给定的端口号
  --data-length <num>：将随机数据附加到已发送的数据包
  --ip-options <options>：发送带有指定ip选项的数据包
  --ttl <val>：设置IP生存时间字段
  --spoof-mac <mac地址/前缀/供应商名称>：欺骗你的MAC地址
  --badsum：使用伪TCP / UDP / SCTP校验和发送数据包
OUTPUT：
  -oN / -oX / -oS / -oG <file>：正常输出扫描，XML，s | <rIpt kIddi3，
     和Grepable格式，分别为给定的文件名。
  -oA <basename>：一次输出三种主要格式
  -v：增加详细级别（使用-vv或更高级别以获得更好的效果）
  -d：提高调试级别（使用-dd或更多以获得更好的效果）
  --reason：显示端口处于特定状态的原因
  --open：仅显示打开（或可能打开）的端口
  --packet-trace：显示发送和接收的所有数据包
  --iflist：打印主机接口和路由（用于调试）
  --log-errors：将错误/警告记录到普通格式的输出文件中
  --append-output：追加而不是clobber指定的输出文件
  --resume <filename>：恢复中止扫描
  --stylesheet <path / URL>：用于将XML输出转换为HTML的XSL样式表
  --webxml：来自Nmap.Org的参考样式表，用于更多可移植的XML
  --no-stylesheet：防止与XML输出相关联的XSL样式表
MISC：
  -6：启用IPv6扫描
  -A：启用操作系统检测，版本检测，脚本扫描和跟踪路由
  --datadir <dirname>：指定自定义Nmap数据文件位置
  --send-eth /  -  send-ip：使用原始以太网帧或IP数据包发送
  --privileged：假设用户具有完全特权
  --unprivileged：假设用户缺少原始套接字权限
  -V：打印版本号
  -h：打印此帮助摘要页面。
例子：
  nmap -v -A scanme.nmap.org
  nmap -v -sn 192.168.0.0/16 10.0.0.0/8
  nmap -v -iR 10000 -Pn -p 80
有关更多选项和示例，请参阅MAN PAGE（http://nmap.org/book/man.html）
Nmap提供了许多选项。由于本节涉及端口扫描，因此我们将重点介绍执行此任务所需的命令。重要的是要注意所使用的命令主要取决于被扫描的主机的时间和数量。您执行此任务所需的主机越多或时间越少，我们查询主机的次数就越少。随着我们继续讨论各种选择，这将变得明显。

根据要评估的IP集，您需要扫描1到65535范围内的TCP和UDP端口。将使用的命令如下： 
nmap -A -PN -sU -sS -T2 -v -p 1-65535 <客户端IP范围> / <CIDR>或<掩码> -oA NMap_FULL_ <客户端IP范围>
nmap -A -PN -sU -sS -T2 -v -p 1-65535 client.com -oA NMap_FULL_client

在东部夏令时间2011-04-22 22:27启动Nmap 5.51（http://nmap.org）

NSE：加载了57个用于扫描的脚本。
启动1个主机的并行DNS解析。在22:27
已完成1台主机的并行DNS解析。在22：27,0.10s过去了
在22:27启动SYN Stealth Scan
正在扫描client.com（74.117.116.73）[65535端口]
在74.117.116.73上发现了开放端口80 / tcp
在大型IP集上，超过100个IP地址的IP集不指定端口范围。将使用的命令如下：
nmap -A -O -PN <客户端IP范围> / <CIDR>或<掩码> -oA NMap_ <客户端IP范围>
nmap -A -O -PN client.com -oA NMap_client

在东部夏令时间2011-04-22 22:37开始Nmap 5.51（http://nmap.org）

client.com的Nmap扫描报告（74.117.116.73）
主机启动（延迟0.13秒）。
rDNS记录为74.117.116.73：74-117-116-73.parked.com
未显示：999个过滤端口
港口国服务版
80 / tcp打开http http http http 2.2.3（（CentOS））
| http-robots.txt：2个不允许的条目
| _ / click.php /ud.php
| _http-title：client.com
| _http-methods：OPTIONS响应中没有Allow或Public标头（状态代码200）
| _http-favicon：Parked.com域名停放
警告：OSScan结果可能不可靠，因为我们找不到至少1 o
笔和1个封闭的端口
设备类型：通用
运行（JUST GUESSING）：Linux 2.6.X（92％），OpenBSD 4.X（88％），FreeBSD 6.X（88％）
应该注意的是，Nmap对IPv6的选择有限。这些包括TCP连接（-sT），Ping扫描（-sn），列表扫描（-sL）和版本检测。

nmap -6 -sT -P0 fe80 :: 80a5：26f2：8db7：5d04％12

在东部夏令时间2011-04-22 22:42启动Nmap 5.51（http://nmap.org）

lancelot的Nmap扫描报告（fe80 :: 80a5：26f2：8db7：5d04）
主机启动（延迟1.0秒）。
未显示：988个已关闭的端口
港口国服务
135 / tcp打开msrpc
445 / tcp open microsoft-ds
554 / tcp open rtsp
2869 / tcp open icslap
3389 / tcp打开ms-term-serv
5000 / tcp打开upnp
5001 / tcp打开commplex-link
5002 / tcp打开rfe
5003 / tcp打开filemaker
5004 / tcp打开avt-profile-1
5357 / tcp打开wsdapi
10243 / tcp打开未知

完成Nmap：在287.05秒内扫描1个IP地址（1个主机）
   


Nmap的不同选项和-s标志组成了不同的扫描类型，比如：一个Ping-scan命令就是"-sP"。在确定了目标主机和网络之后，即可进行扫描。如果以root来运行Nmap，Nmap的功能会大大的增强，因为超级用户可以创建便于Nmap利用的定制数据包。 
在目标机上，Nmap运行灵活。使用Nmap进行单机扫描或是整个网络的扫描很简单，只要将带有"/mask"的目标地址指定给Nmap即可。地址是"victim/24"， 则目标是c类网络，地址是"victim/16"， 则目标是B类网络。 
另外,Nmap允许你使用各类指定的网络地址，比如 192.168.7.*,是指192.168.7.0/24, 或 192.168.7.1,4,8-12，对所选子网下的主机进行扫描。 

Ping扫描(Ping Sweeping) 

入侵者使用Nmap扫描整个网络寻找目标。通过使用" -sP"命令，进行ping扫描。缺省情况下，Nmap给每个扫描到的主机发送一个ICMP echo和一个TCP ACK, 主机对任何一种的响应都会被Nmap得到。 
举例：扫描192.168.7.0网络： 
# nmap -sP 192.168.7.0/24 
Starting nmap V. 2.12 by Fyodor (fyodor@dhp.com, www.insecure.org/nmap/) 
Host (192.168.7.11) appears to be up. 
Host (192.168.7.12) appears to be up. 
Host (192.168.7.76) appears to be up. 
Nmap run completed -- 256 IP addresses (3 hosts up) scanned in 1 second 
如果不发送ICMP echo请求，但要检查系统的可用性，这种扫描可能得不到一些站点的响应。在这种情况下，一个TCP"ping"就可用于扫描目标网络。 
一个TCP"ping"将发送一个ACK到目标网络上的每个主机。网络上的主机如果在线，则会返回一个TCP RST响应。使用带有ping扫描的TCP ping选项，也就是"PT"选项可以对网络上指定端口进行扫描(本文例子中指的缺省端口是80（http）号端口)，它将可能通过目标边界路由器甚至是防火墙。注意，被探测的主机上的目标端口无须打开，关键取决于是否在网络上。 
# nmap -sP -PT80 192.168.7.0/24 
TCP probe port is 80 
Starting nmap V. 2.12 by Fyodor (fyodor@dhp.com, www.insecure.org/nmap/) 
Host (192.168.7.11) appears to be up. 
Host (192.168.7.12) appears to be up. 
Host (192.168.7.76) appears to be up. 
Nmap run completed -- 256 IP addresses (3 hosts up) scanned in 1 second 
当潜在入侵者发现了在目标网络上运行的主机，下一步是进行端口扫描。 
Nmap支持不同类别的端口扫描TCP连接, TCP SYN, Stealth FIN, Xmas Tree,Null和UDP扫描。

端口扫描(Port Scanning) 

一个攻击者使用TCP连接扫描很容易被发现，因为Nmap将使用connect()系统调用打开目标机上相关端口的连接，并完成三次TCP握手。黑客登录到主机将显示开放的端口。一个tcp连接扫描使用"-sT"命令如下。 
# nmap -sT 192.168.7.12 
Starting nmap V. 2.12 by Fyodor (fyodor@dhp.com, www.insecure.org/nmap/) 
Interesting ports on (192.168.7.12): 
Port State Protocol Service 
7 open tcp echo 
9 open tcp discard 
13 open tcp daytime 
19 open tcp chargen 
21 open tcp ftp 
... 
Nmap run completed -- 1 IP address (1 host up) scanned in 3 seconds 

隐蔽扫描(Stealth Scanning) 

如果一个攻击者不愿在扫描时使其信息被记录在目标系统日志上，TCP SYN扫描可帮你的忙，它很少会在目标机上留下记录，三次握手的过程从来都不会完全实现。通过发送一个SYN包（是TCP协议中的第一个包）开始一次 SYN的扫描。任何开放的端口都将有一个SYN|ACK响应。然而，攻击者发送一个RST替代ACK，连接中止。三次握手得不到实现，也就很少有站点能记录这样的探测。如果是关闭的端口，对最初的SYN信号的响应也会是RST，让NMAP知道该端口不在监听。"-sS"命令将发送一个SYN扫描探测主机或网络： 

# nmap -sS 192.168.7.7 

Starting nmap V. 2.12 by Fyodor (fyodor@dhp.com, www.insecure.org/nmap/) 
Interesting ports on saturnlink.nac.net (192.168.7.7): 
Port State Protocol Service 
21 open tcp ftp 
25 open tcp smtp 
53 open tcp domain 
80 open tcp http 
... 
Nmap run completed -- 1 IP address (1 host up) scanned in 1 second 

虽然SYN扫描可能不被注意，但他们仍会被一些入侵检测系统捕捉。Stealth FIN，Xmas树和Null scans可用于躲避包过滤和可检测进入受限制端口的SYN包。这三个扫描器对关闭的端口返回RST，对开放的端口将吸收包。一个 FIN "-sF"扫描将发送一个FIN包到每个端口。 
然而Xmas扫描"-sX"打开FIN, URG和PUSH的标志位，一个Null scans "-sN"关闭所有的标志位。因为微软不支持TCP标准，所以FIN, Xmas Tree和Null scans在非微软公司的操作系统下才有效。 

UDP扫描(UDP Scanning) 

如果一个攻击者寻找一个流行的UDP漏洞，比如 rpcbind漏洞或cDc Back orifice。为了查出哪些端口在监听，则进行UDP扫描，即可知哪些端口对UDP是开放的。Nmap将发送一个O字节的UDP包到每个端口。如果主机返回端口不可达，则表示端口是关闭的。但这种方法受到时间的限制，因为大多数的UNIX主机限制ICMP错误速率。幸运的是，Nmap本身检测这种速率并自身减速，也就不会产生溢出主机的情况。 
# nmap -sU 192.168.7.7 
WARNING: -sU is now UDP scan -- for TCP FIN scan use -sF 
Starting nmap V. 2.12 by Fyodor (fyodor@dhp.com, www.insecure.org/nmap/) 
Interesting ports on saturnlink.nac.net (192.168.7.7): 
Port State Protocol Service 
53 open udp domain 
111 open udp sunrpc 
123 open udp ntp 
137 open udp netbios-ns 
138 open udp netbios-dgm 
177 open udp xdmcp 
1024 open udp unknown 
Nmap run completed -- 1 IP address (1 host up) scanned in 2 seconds 

操作系统识别(OS Fingerprinting) 

通常一个入侵者可能对某个操作系统的漏洞很熟悉，能很轻易地进入此操作系统的机器。一个常见的选项是TCP/IP上的指纹，带有"-O"选项决定远程操作系统的类型。这可以和一个端口扫描结合使用，但不能和ping扫描结合使用。Nmap通过向主机发送不同类型的探测信号，缩小查找的操作系统系统的范围。指纹验证TCP包括使用FIN探测技术发现目标机的响应类型。BOGUS的标志探测，发现远程主机对发送的带有SYN包的不明标志的反应，TCP 初始序列号(ISN)取样发现ISN数值的样式，也可以用另外的方式决定远程操作系统。有一篇权威的关于指纹（fingertprinting）的文章, 作者：Fyodor，也是namp的作者，参见地址：http://www.insecure.org/nmap/nmap-fingerprinting-article.html 

Nmap's操作系统的检测是很准确也是很有效的，举例：使用系统Solaris 2.7带有SYN扫描的指纹验证堆栈。 
# nmap -sS -O 192.168.7.12 

Starting nmap V. 2.12 by Fyodor (fyodor@dhp.com, www.insecure.org/nmap/) 
Interesting ports on comet (192.168.7.12): 
Port State Protocol Service 
7 open tcp echo 
9 open tcp discard 
13 open tcp daytime 
19 open tcp chargen 
21 open tcp ftp 
... 
TCP Sequence Prediction: Class=random positive increments 
Difficulty=17818 (Worthy challenge) 
Remote operating system guess: Solaris 2.6 - 2.7 
Nmap run completed -- 1 IP address (1 host up) scanned in 5 seconds 

Ident扫描（Ident Scanning） 

一个攻击者常常寻找一台对于某些进程存在漏洞的电脑。比如,一个以root运行的WEB服务器。如果目标机运行了identd,一个攻击者使用Nmap通过 "-I"选项的TCP连接,就可以发现哪个用户拥有http守护进程。我们将扫描一个Linux WEB服务器为例： 

# nmap -sT -p 80 -I -O www.yourserver.com 

Starting nmap V. 2.12 by Fyodor (fyodor@dhp.com, www.insecure.org/nmap/) 
Interesting ports on www.yourserver.com (xxx.xxx.xxx.xxx): 
Port
State Protocol Service Owner 
80 open tcp http root 
TCP Sequence Prediction: Class=random positive increments 
Difficulty=1140492 (Good luck!) 
Remote operating system guess: Linux 2.1.122 - 2.1.132; 2.2.0-pre1 - 2.2.2 
Nmap run completed -- 1 IP address (1 host up) scanned in 1 second 
如果你的WEB服务器是错误的配置并以root来运行，象上例一样，它将是黎明前的黑暗。 
Apache 运行在root下，是不安全的实践，你可以通过把/etc/indeed.conf中的auth服务注销来阻止ident请求，并重新启动ident。另外也可用使用ipchains或你的最常用的防火墙，在网络边界上执行防火墙规则来终止ident请求，这可以阻止来路不明的人探测你的网站用户拥有哪些进程。 

选项(Options) 

除了以上这些扫描，Nmap还提供了无数选项。有一个是"-PT",，我们已经介绍过了。在目标机或网络上常见的未经过滤的端口，进行TCP "ping"扫描。 
另一个选项是"-P0"。在缺省设置下试图扫描一个端口之前，Nmap将用TCP ping" 和 ICMP echo命令ping一个目标机，如果ICMP 和TCP的探测扫描得不到响应，目标主机或网络就不会被扫描，即使他们是运行着的。而"-P0"选项允许在扫描之前不进行ping，即可进行扫描。 
你应该习惯使用"-v"命令，它详细列出所有信息，能和所有的扫描选项一起使用。你能反复地使用这个选项，获得有关目标机的更多信息。 
使用"-p "选项，可以指定扫描端口。比如 ，攻击者想探测你的web服务器的ftp（port 21），telnet (port 23), dns (port 53), http (port 80),想知道你所使用的操作系统，它将使用SYN扫描。 
# nmap -sS -p 21,23,53,80 -O -v www.yourserver.com 

小结： 
使用什么样的方法来抵制一个黑客使用Nmap，这样的工具是有的，比如 Scanlogd, Courtney, and Shadow;，然而使用这样的工具并不能代替网络安全管理员。因为扫描只是攻击的前期准备，站点使用它只可以进行严密的监视。 
使用Nmap监视自己的站点，系统和网络管理员能发现潜在入侵者对你的系统的探测。
