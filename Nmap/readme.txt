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
   
