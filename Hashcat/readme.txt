
Hashcat密码破解工具

    hashcat号称世界上最快的密码破解，世界上第一个和唯一的基于GPGPU规则引擎，免费多GPU（高达128个GPU），多哈希，多操作系统（Linux和Windows本地二进制文件），多平台（OpenCL和CUDA支持），多算法，资源利用率低，基于字典攻击，支持分布式破解等等，目前最新版本为4.01，下载地址https://hashcat.net/files/hashcat-4.1.0.7z，hashcat目前支持各类公开算法高达247类，市面上面公开的密码加密算法基本都支持！
    hashcat系列软件在硬件上支持使用CPU、NVIDIA GPU、ATI GPU来进行密码破解。在操作系统上支持Windows、Linux平台，并且需要安装官方指定版本的显卡驱动程序，如果驱动程序版本不对，可能导致程序无法运行。NVIDIA users  GPU破解驱动需要ForceWare 331.67以及更高版本(http://www.geforce.cn/drivers)，AMD 用户则需要Catalyst 14.9以及更高版本，可以通过Catalyst 自动侦测和下载检测工具来检测系统应该下载那个版本，下载地址：http://support.amd.com/en-us/download/auto-detect-tool，选择合适的版本安装即可。其官方github 网站地址为：https://github.com/hashcat/hashcat。
    
1.准备工作
（1）kali linux操作系统或者虚拟机
（2）windows7操作系统或者虚拟机
（3）准备字典，可以自己生成字典工具，也可以从互联网获取字典，推荐二个字典下载网站：
  http://contest-2010.korelogic.com/wordlists.html
  https://wiki.skullsecurity.org/Passwords
（4）在windows7中新增一个用户antian365，密码为password。
  在单击“开始”-“运行”中输入“cmd”并按“Shift+Ctrl+Enter”组合键，输入命令“ netuser antian365 password /add”。
  或者以管理员权限启动“cmd.exe”程序也可，测试完毕后可以通过命令删除该帐号“net user antian365 /del”
（5）下载saminside
官方网站目前已经停止saminside软件的开发了，可以到华军软件园下载：http://gwbnsh.onlinedown.net/down2/saminside.v2.6.1.0.chs.rar
（6）字典合并及排序处理
  cat *.dic >file.txt
  
Linux下使用
 sort –u file.txt>password.lst
 
2.HashCat软件使用参数
    2.1 hashcat使用参数
    直接运行hashcat（分为32和64位版本）会提示使用参数：
    Usage:hashcat64 [options]… hash|hashfile|hccapxfile [dictionary|mask|directory]…
    也即hashcat [选项] 破解的哈希值或hash文件、hccapx文件 [字典|掩码|目录] …
    Hccapxfile对应无线包，其对应破解哈希类型为“-m 2500 = WPA/WPA2”。
    2.2 查看帮助
    使用hashcat –help命令可以获取详细的帮助信息，可以使用hashcat –help>help.txt来参考具体的参数使用帮助。
    2.3 选项
    （1）普通
    -m, —hash-type=NUM           哈希类别，其NUM值参考其帮助信息下面的哈希类别值，其值为数字。如果不指定m值则默认指md5，例如-m 1800是sha512 Linux加密。
    -a, –attack-mode=NUM         攻击模式，其值参考后面对参数。“-a 0”字典攻击，“-a 1” 组合攻击；“-a 3”掩码攻击。
    -V, —version                            版本信息
    -h, –help                                   帮助信息。
    –quiet                                       安静的模式, 抑制输出
    （2）基准测试
    -b, –benchmark                       测试计算机破解速度和显示硬件相关信息
    （3）杂项
    –hex-salt                         salt值是用十六进制给出的
    –hex-charset                  设定字符集是十六进制给出
    –runtime=NUM              运行数秒（NUM值）后的中止会话
    –status                            启用状态屏幕的自动更新
    –status-timer=NUM       状态屏幕更新秒值
    –status-automat             以机器可读的格式显示状态视图
    –session                         后跟会话名称，主要用于中止任务后的恢复破解。
    （4）文件
    -o,  –outfile=FILE                   定义哈希文件恢复输出文件
    –outfile-format=NUM            定义哈希文件输出格式，见下面的参考资料
    –outfile-autohex-disable       禁止使用十六进制输出明文
    -p,  –separator=CHAR         为哈希列表/输出文件定义分隔符字符
    –show                                     仅仅显示已经破解的密码
    –left                                         仅仅显示未破解的密码
    –username                            忽略hash表中的用户名，对linux文件直接进行破解，不需要进行整理。
    –remove                                移除破解成功的hash，当hash是从文本中读取时有用，避免自己手工移除已经破解的hash
    –stdout                                  控制台模式
    –potfile-disable                    不写入pot文件
    –debug-mode=NUM           定义调试模式（仅通过使用规则进行混合），参见下面的参考资料
    –debug-file=FILE                调试规则的输出文件（请参阅调试模式）
    -e, –salt-file=FILE                定义加盐文件列表
    –logfile-disable                    禁止logfile
    （4） 资源
    -c, –segment-size=NUM       字典文件缓存大小（M）
    -n, –threads=NUM                 线程数
    -s,  –words-skip=NUM          跳过单词数
    -l, –words-limit=NUM            限制单词数(分布式)
    （5）规则
      -r, –rules-file=FILE             使用规则文件: -r 1.rule，
     -g,  –generate-rules=NUM       随机生成规则
    –generate-rules-func-min= 每个随机规则最小值
    –generate-rules-func-max=每个随机规则最大值
    –generate-rules-seed=NUM  强制RNG种子数
    （6）自定义字符集
    -1,  –custom-charset1=CS  用户定义的字符集
    -2, –custom-charset2=CS  例如:
    -3, –custom-charset3=CS –custom-charset1=?dabcdef : 设置?1 为0123456789abcdef
    -4, –custom-charset4=CS   -2mycharset.hcchr : 设置 ?2 包含在mycharset.hcchr
    文件
    （7）攻击模式
    大小写转换攻击:
    –toggle-min=NUM              在字典中字母的最小值
    –toggle-max=NUM              在字典中字母的最大值
    * 使用掩码攻击模式:
    –increment                   使用增强模式
    –increment-min=NUM          增强模式开始值
    –increment-max=NUM          增强模式结束值
    * 排列攻击模式
    –perm-min=NUM                过滤比NUM数小的单词
    –perm-max=NUM               过滤比NUM数大的单词
    * 查找表攻击模式:
      -t, –table-file=FILE             表文件
           –table-min=NUM               在字典中的最小字符值
           –table-max=NUM               在字典中的最大字符值
    * 打印攻击模式:
    –pw-min=NUM                  如果长度大于NUM，则打印候选字符 
    –pw-max=NUM                 如果长度小于NUM，则打印候选字符
    –elem-cnt-min=NUM            每个链的最小元素数
    –elem-cnt-max=NUM            每个链的最大元素数
    –wl-dist-len                从字典表中计算输出长度分布
    –wl-max=NUM             从字典文件中加载NUM个单词，设置0禁止加载。
    –case-permute             在字典中对每一个单词进行反转
    （8）参考
    输出文件格式:
    1 = hash[:salt]
    2 = plain 明文
    3 = hash[:salt]:plain
    4 = hex_plain
    5 = hash[:salt]:hex_plain
    6 = plain:hex_plain
    7 = hash[:salt]:plain:hex_plain
    8 = crackpos
    9 = hash[:salt]:crackpos
    10 = plain:crackpos
    11 = hash[:salt]:plain:crackpos
    12 = hex_plain:crackpos
    13 = hash[:salt]:hex_plain:crackpos
    14 = plain:hex_plain:crackpos
    15 = hash[:salt]:plain:hex_plain:crackpos
    * 调试模式输出文件 (for hybrid mode only, by using rules):
    1 = save finding rule 
    2 = save original word
    3 = save original word and finding rule
    4 = save original word, finding rule andmodified plain
    * 内置的字符集:
    ?l = abcdefghijklmnopqrstuvwxyz 代表小写字母
    ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ 代表大写字母
    ?d = 0123456789 代表数字
    ?s = !”#$%&’()*+,-./:;<=>?@[\]^_`{|}~  代表特殊字符
    ?a = ?l?u?d?s 大小写数字及特殊字符的组合
    ?b = 0×00 – 0xff
    攻击模式
    0 = Straight （字典破解）
    1 = Combination （组合破解）
    2 = Toggle-Case （大小写转换）
    3 = Brute-force（掩码暴力破解）
    4 = Permutation（序列破解）
    5 = Table-Lookup（查表破解）
    6 = Hybrid dict + mask 字典加掩码破解
    7 = Hybrid mask + dict 掩码+字典破解
    8 = Prince（王子破解）
    * 哈希类型
    有关哈希具体值示例可以参考https://hashcat.net/wiki/doku.php?id=example_hashes
      0 = MD5
      10 = md5($pass.$salt)
      20 = md5($salt.$pass)
      30 = md5(unicode($pass).$salt)
      40 = md5($salt.unicode($pass))
      50 = HMAC-MD5 (key = $pass)
      60 = HMAC-MD5 (key = $salt)
      100 = SHA1
      110 = sha1($pass.$salt)
      120 = sha1($salt.$pass)
      130 = sha1(unicode($pass).$salt)
      140 = sha1($salt.unicode($pass))
      150 = HMAC-SHA1 (key = $pass)
      160 = HMAC-SHA1 (key = $salt)
      200 = MySQL323
      300 = MySQL4.1/MySQL5
      400 = phpass, MD5(WordPress), MD5(phpBB3),MD5(Joomla)
      500 = md5crypt, MD5(Unix), FreeBSD MD5,Cisco-IOS MD5
      900 = MD4
      1000 = NTLM
      1100 = Domain Cached Credentials (DCC), MSCache
      1400 = SHA256
      1410 = sha256($pass.$salt)
      1420 = sha256($salt.$pass)
      1430 = sha256(unicode($pass).$salt)
      1431 = base64(sha256(unicode($pass)))
      1440 = sha256($salt.unicode($pass))
      1450 = HMAC-SHA256 (key = $pass)
      1460 = HMAC-SHA256 (key = $salt)
      1600 = md5apr1, MD5(APR), Apache MD5
      1700 = SHA512
      1710 = sha512($pass.$salt)
      1720 = sha512($salt.$pass)
      1730 = sha512(unicode($pass).$salt)
      1740 = sha512($salt.unicode($pass))
      1750 = HMAC-SHA512 (key = $pass)
      1760 = HMAC-SHA512 (key = $salt)
      1800 = SHA-512(Unix)
      2400 = Cisco-PIX MD5
      2410 = Cisco-ASA MD5
      2500 = WPA/WPA2
      2600 = Double MD5
      3200 = bcrypt, Blowfish(OpenBSD)
      3300 = MD5(Sun)
      3500 = md5(md5(md5($pass)))
      3610 = md5(md5($salt).$pass)
      3710 = md5($salt.md5($pass))
      3720 = md5($pass.md5($salt))
      3800 = md5($salt.$pass.$salt)
      3910 = md5(md5($pass).md5($salt))
      4010 = md5($salt.md5($salt.$pass))
      4110 = md5($salt.md5($pass.$salt))
      4210 = md5($username.0.$pass)
      4300 = md5(strtoupper(md5($pass)))
      4400 = md5(sha1($pass))
      4500 = Double SHA1
      4600 = sha1(sha1(sha1($pass)))
      4700 = sha1(md5($pass))
      4800 = MD5(Chap), iSCSI CHAP authentication
      4900 = sha1($salt.$pass.$salt)
      5000 = SHA-3(Keccak)
      5100 = Half MD5
      5200 = Password Safe SHA-256
      5300 = IKE-PSK MD5
      5400 = IKE-PSK SHA1
      5500 = NetNTLMv1-VANILLA / NetNTLMv1-ESS
      5600 = NetNTLMv2
      5700 = Cisco-IOS SHA256
      5800 = Android PIN
      6300 = AIX {smd5}
      6400 = AIX {ssha256}
      6500 = AIX {ssha512}
      6700 = AIX {ssha1}
      6900 = GOST, GOST R 34.11-94
      7000 = Fortigate (FortiOS)
      7100 = OS X v10.8+
      7200 = GRUB 2
      7300 = IPMI2 RAKP HMAC-SHA1
      7400 = sha256crypt, SHA256(Unix)
      7900 = Drupal7
      8400 = WBB3, Woltlab Burning Board 3
      8900 = scrypt
      9200 = Cisco $8$
      9300 = Cisco $9$
      9800 = Radmin2
     10000 = Django (PBKDF2-SHA256)
     10200 = Cram MD5
     10300 = SAP CODVN H (PWDSALTEDHASH) iSSHA-1
     11000 = PrestaShop
     11100 = PostgreSQL Challenge-ResponseAuthentication (MD5)
     11200 = MySQL Challenge-Response Authentication(SHA1)
     11400 = SIP digest authentication (MD5)
     99999 = Plaintext
    特殊哈希类型
       11 = Joomla < 2.5.18
       12 = PostgreSQL
       21 = osCommerce, xt:Commerce
       23 = Skype
      101 = nsldap, SHA-1(Base64), Netscape LDAPSHA
      111 = nsldaps, SSHA-1(Base64), Netscape LDAPSSHA
      112 = Oracle S: Type (Oracle 11+)
      121 = SMF > v1.1
      122 = OS X v10.4, v10.5, v10.6
      123 = EPi
      124 = Django (SHA-1)
      131 = MSSQL(2000)
      132 = MSSQL(2005)
      133 = PeopleSoft
      141 = EPiServer 6.x < v4
     1421 = hMailServer
     1441 = EPiServer 6.x > v4
     1711 = SSHA-512(Base64), LDAP {SSHA512}
     1722 = OS X v10.7
     1731 = MSSQL(2012 & 2014)
     2611 = vBulletin < v3.8.5
     2612 = PHPS
     2711 = vBulletin > v3.8.5
     2811 = IPB2+, MyBB1.2+
     3711 = Mediawiki B type
     3721 = WebEdition CMS
     7600 = Redmine Project Management Web App
     
3.密码破解推荐原则
    3.1 密码破解推荐原则
    破解时采取先易后难的原则，建议如下：
    （1）利用收集的公开字典进行破解
    （2）使用1-8位数字进行破解。
    （3）使用1-8位小写字母进行破解
    （4）使用1-8位大写字母进行破解
    （5）使用1-8位混合大小写+数字+特殊字符进行破解
    3.2 hashcat破解规则
    （1）字典攻击
     -a 0 password.lst
    （2）1到8为数字掩码攻击
     -a 3 --increment --increment-min 1--increment-max 8 ?d?d?d?d?d?d?d?d –O
    ?d代表数字，可以换成小写字母?l，大写字母?u，特殊字符?s，大小写字母+特殊字符?a，–O表示最优化破解模式，可以加该参数，也可以不加该参数。
    （3）8为数字攻击
     -a 3 ?d?d?d?d?d?d?d?d 
    同理可以根据位数设置为字母大写、小写、特殊字符等模式。
    （4）自定义字符
    现在纯数字或者纯字母的密码是比较少见的，根据密码专家对泄漏密码的分析，90%的个人密码是字母和数字的组合，可以是自定义字符了来进行暴力破解，Hashcat支持4个自定义字符集，分别是 -1 -2 -3 -4。定义时只需要这样-2  ?l?d ，然后就可以在后面指定?2，?2表示小写字母和数字。这时候要破解一个8位混合的小写字母加数字：
    Hashcat.exe -a 3 –force -2 ?l?d  hassh值或者hash文件  ?2?2?2?2?2?2?2?2
    例如破解dz小写字母+数字混合8位密码破解：
    Hashcat -m 2611  -a 3 -2 ?l?d  dz.hash    ?2?2?2?2?2?2?2?2
    （5）字典+掩码暴力破解
    Hashcat还支持一种字典加暴力的破解方法，就是在字典前后再加上暴力的字符序列，比如在字典后面加上3为数字，这种密码是很常见的。使用第六种攻击模式：
        a-6 (Hybrid dict + mask)
    如果是在字典前面加则使用第7中攻击模式也即( a-7 = Hybridmask + dict)，下面对字典文件加数字123进行破解：
     H.exe -a 6 ffe1cb31eb084cd7a8dd1228c23617c8  password.lst ?d?d?d
    假如ffe1cb31eb084cd7a8dd1228c23617c8的密码为password123，则只要password.lst包含123即可。
     （6）掩码+字典暴力破解
     H.exe -a 7  ffe1cb31eb084cd7a8dd1228c23617c8  password.lst ?d?d?d
    假如ffe1cb31eb084cd7a8dd1228c23617c8的密码为123password，则只要password.lst包含password即可。
    （7）大小写转换攻击，对password.lst中的单词进行大小写转换攻击
     H.exe-a 2  ffe1cb31eb084cd7a8dd1228c23617c8  password.lst
     
     
4.获取并整理密码hashes值
4.1 windows哈希值获取及整理 
（1）获取Windows操作系统hash值
获取Windows7操作系统的hash值有多个软件，比如wce，mimikatz，cain以及saminside等，在windows vista以及以上版本都会有UAC权限控制机制。UAC（User Account Control，用户帐户控制）是微软为提高系统安全而在Windows Vista中引入的新技术，它要求用户在执行可能会影响计算机运行的操作或执行更改影响其他用户的设置的操作之前，提供权限或管理员‌密码。通过在这些操作启动前对其进行验证，UAC 可以帮助防止恶意软件和间谍软件在未经许可的情况下在计算机上进行安装或对计算机进行更改。因此获取密码的工具都需要以管理员身份运行，选择saminside.exe程序，右键单击在弹出的菜单中选择“以管理员身份运行”，然后在saminside程序主界面中从左往右选择第三个图标，下来菜单第二个选项（Import local user using Scheduler）来获取密码，如图1所示，即可获取本机所有帐号的密码hash值等信息。
 
图1获取密码hash值
（2）整理hash值
在saminside中可以导出所有帐号的hash值，也可以复制单个帐号的hash值。单击“File”菜单中的“导出用户到pwdump文件”即可导出获取的hash值，也可以选择hash，右键单击“复制”-“NT hash”获取NT hash值。对于Windows Vista以上操作系统即使是普通的密码也以“AAD3B”开头的一串字符，这个值目前在“ophcrack”等工具中无法进行破解，在saminside中会显示为一串“0”字符，将NT hash值整理到一个文件中，并命名为win2.hash，如图2所示。
图2整理需要破解的hash值
4.2 linux哈希值整理
在linux下使用cat /ect/shadow>myshadow.txt
可以对myshadow.txt进行整理仅仅保留加密部分值，例如：
 $1$H4EQc23T$jseelsIklWRjQMiY8sNdf1
也可以保留用户名部分，root:$1$KsRJO8kG$M9co4G7T6.5KcITsSCRNS/:15225:0:99999:7:::，如果带用户名，则在破解是需要加–username参数。
3.其它哈希值整理
一般来说一类密码哈希值单独保存为一个文件，有的密码带salt，因此需要完整的哈希值，例如discuz!论坛的密码值为：
 ffe1cb31eb084cd7a8dd1228c23617c8:f56463
前段值类似md5加密，后段值为salt，如果没有salt值，其破解结果就相差甚远了。
对某些特殊的哈希加密，还需要借助一些工具软件来进行，例如office加密文档，就需要从http://www.openwall.com/john/j/john-1.8.0-jumbo-1.tar.gz里面需要对应的python文件进行hash计算。例如office密码哈希计算机工具文件office2john.py，使用office2john.py 1.doc即可计算其文档加密值。
5.破解Windows下hash值

5.1 hashcat破解
将准备好的字典password.lst、需要破解的hash值文件win.hash复制到hashcat程序所在文件夹下，执行一下命令进行破解：
 hashcat-m 1000 -a 0 -o winpassok.txt win.hash password.lst --username
参数说明：
“-m 1000” 表示破解密码类型为“NTLM”；
“-a 0”表示采用字典破解；
“-o”将破解后的结果输出到winpassok.txt；
“–remove win.hash”表示从win.hash移除破解成功的hash，带username不能跟remove同时使用，也就可以对单一密码值进行整理，然后使用该参数。
“password.lst”为密码字典文件。
 破解过程会显示“[s]tatus[p]ause [r]esume [b]ypass [q]uit =>”，键盘输入“s”显示破解状态，输入“p”暂停破解，输入“r”继续破解，输入“b”表示忽略破解，输入“q”表示退出，所有成功破解的结果都会自动保存在 “hashcat.pot” 文件中。破解结束会显示如图3所示的信息。
图3显示破解信息
5.2 查看破解结果
（1）使用“type winpassok.txt”命令查看破解结果，如图4所示，显示该帐号的密码为“password”。
图4查看密码破解结果
（2）“–show”命令查看。如果在破击参数中没有“-o winpassok.txt”则可以通过命令后加入“–show”进行查看：
hashcat-m 1000 -a 0  win.hash password.lst–username –show
（3）hashcat.potfile查看结果。到hashcat程序目录直接打开hashcat.potfile文件来查看已经成功破解的密码。
6.linux操作系统密码破解

6.1 针对不同加密类型进行破解
（1）linux sha512crypt $6$, SHA512 (Unix)加密方式： 
 hashcat  -m 1800 sha512linux.txt p.txt
 （2）linux sha256crypt $5$, SHA256 (Unix)加密方式：
 hashcat  -m 7400 sha256linux.txt p.txt
（3）linux下md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)加密方式：
 hashcat   -m 500  linuxmd5.txt p.txt
（4）inux下bcrypt $2*$, Blowfish加密方式：
 hashcat   -m 3200  linuxmd5.txt p.txt
6.2 破解示例
如图5所示，执行命令进行破解：hashcat -m 500 passwd1_hash.txt password.lst
在破解过程中如果有成功的密码，则会直接显示，按s键可以查看破解的状态信息，p键暂停，s键继续破解，q键退出破解。
  
图5破解linux md5密码
hashcat.pot中会自动保存破解成功的哈希密码及其破解后的明文密码。
7.破解office文档

7.1 计算office加密文档的hash值
下载http://www.openwall.com/john/j/john-1.8.0-jumbo-1.tar.gz，从其压缩包中获取 office2john.py文件，然后执行
 office2john.pyDocOld2010.doc
即可获取DocOld2010.doc文档的加密值，如图6所示。

            
                
DocOld2010.doc:$oldoffice$1*d6aabb63363188b9b73a88efb9c9152e*afbbb9254764273f8f4fad9a5d82981f*6f09fd2eafc4ade522b5f2bee0eaf66d:::1:

            
                
  ocOld2010.doc

        
            

    
        
 
图6计算office哈希值
去掉前后的DocOld2010.doc和对应的“：”，其真正的哈希值为：
 $oldoffice$1*d6aabb63363188b9b73a88efb9c9152e*afbbb9254764273f8f4fad9a5d82981f*6f09fd2eafc4ade522b5f2bee0eaf66d
将其保存为hash文件。
7.2 破解Office加密Offcie版本对应哈希类型

            
                
Office97-03(MD5+RC4,oldoffice$0,oldoffice$1):   -m 9700  

            
                
Office97-03($0/$1, MD5 + RC4, collider #1):   -m 9710 

            
                
Office97-03($0/$1, MD5 + RC4, collider #2):   -m 9720 

            
                
Office97-03($3/$4, SHA1 + RC4):   -m 9800 

            
                
Office97-03($3, SHA1 + RC4, collider #1):   -m 9810 

            
                
Office97-03($3, SHA1 + RC4, collider #2):   -m 9820 

            
                
Office2007:   -m 9400  

            
                
Office2010:  -m 9500 

            
                
Office2013:   -m 9600

        
            

    
        
7.3 破解示例
（1）8位数字破解
 Hashcat64-m 9700 hash -a 3 ?d?d?d?d?d?d?d?d -w 3 –O
(2)1-8位数字破解
 Hashcat-m 9700 hash -a 3 --increment --increment-min 1--increment-max 8 ?d?d?d?d?d?d?d?d
(3)1到8位小写字母破解
 Hashcat-m 9700 hash -a 3 --increment --increment-min 1--increment-max 8 ?l?l?l?l?l?l?l?l
（4）8位小写字母破解
 Hashcat-m 9700 hash -a 3 ?l?l?l?l?l?l?l?l -w 3 –O
（5）1-8位大写字母破解
 Hashcat-m 9700 hash -a 3 --increment --increment-min 1--increment-max 8 ?u?u?u?u?u?u?u?u
（6）8位大写字母破解
 Hashcat-m 9700 hash -a 3 ?u?u?u?u?u?u?u?u -w 3 –O
（7）5位小写+ 大写+数字+特殊字符破解
 Hashcat-m 9700 hash -a 3 ?b?b?b?b?b -w 3
（8）使用字典进行破解
使用password.lst字典进行暴力破解，-w 3参数是指定电力消耗
 Hashcat  -m 9700 -a 0 -w 3 hash  password.lst
如图7所示，对hash文件通过数字破解完成后，继续进行1-8位小写字母的破解，在该图中会显示掩码值，破解进度，破解开始时间，破解预计耗费时间，以及破解显卡或者CPU的温度，一般设置到90摄氏度就自动终止，以免烧坏计算机。
 
图7开始破解 
7.4 查看破解结果
在执行破解成功后，hashcat会自动终止破解，并显示破解状态为Cracked，Recvoered中也会显示是否破解成功，如图8所示，经过34分钟的破解，成功将某一个加密文档破解。
 
图8破解word文件成功
还可以通过查看hashcat.potfile以及执行破解命令后加“–show”命令查看，也即：
 Hashcat64-m 9700 hash -a 3 --increment --increment-min 1 --increment-max 8?l?l?l?l?l?l?l?l –show
如图9，图10所示，该word文件密码为shirley。
 
图9通过查看hashcat.potfile文件查看破解结果
 
图10执行命令查看破解结果
8.暴力破解ssh的known_hosts中的IP地址

8.1 破解known_hosts中的IP地址
经过研究发现known_hosts中会对连接的IP地址进行HMAC SHA1加密，可以通过hexhosts攻击进行转换，然后通过hashcat进行暴力破解，其密码类型为160（HMAC-SHA1 (key = $salt)）。
（1）计算HMAC SHA1值
 gitclonehttps://github.com/persona5/hexhosts.git
cdhexhosts
gcchexhosts.c -lresolv -w -o hexhosts
./hexhosts
获取known_hosts的HMAC SHA1加密值：
 a7453898831af52ada58c964832f6a36f04b9927:2be1fc63b56a3f49c6c25e61beeb0887bf5c4e9d
注意：known_hosts值一定要正确，可以将known_hosts文件复制到hexhosts文件目录。
（2）组合攻击暴力破解
 hashcat-a 1 -m 160 known_hosts.hash ips_left.txt ips_right.txt --hex-salt
组合攻击是将ips_left.txt和ips_right.txt进行组合，形成完整的IP地址进行暴力破解。
ips_left.txt和ips_right.txt文件可以用以下代码进行生成：
 ip-gen.sh：

#!/bin/bash

for a in `seq 0 255`

do

  for b in `seq0 255`

  do

  echo"$a.$b." >> ips_left.txt

  echo"$a.$b" >> ips_right.txt

  done

done
（3）使用掩码进行攻击
 hashcat  -a 3 -m 160 known_hosts.hash ipv4.hcmask--hex-salt
ipv4.hcmask文件内容可去https://pastebin.com/4HQ6C8gG下载。
 
图11破解known_hosts中加密的IP地址
8.2 破解md5加密的IP地址
在CDN等网络或者配置中往往会对IP地址进行MD5加密，由于其位数3×4+3（xxx.xxx.xxx.xxx）=17位，通过正常的密码破解其时间耗费非常长，但通过分析其IP地址的规律，发现其地址XXX均为数字，因此可以通过hashcat的组合和掩码进行攻击。

            
                
hashcat-a 1 –m 0 ip.md5.txt ips_left.txt ips_right.txt 

            
                
hashcat  -a1 -m 0 ip.md5.txt ipv4.hcmask

        
            

    
        
另外在F5的cookie中会对其IP地址进行加密，可以参考的破解代码如下：

            
                
>>>import struct

            
                
>>>cookie = "1005421066.20736.0000"

            
                
>>>(ip,port,end)=cookie.split(".")

            
                
>>>(a,b,c,d)=[ord(i) for i in struct.pack("i",int(ip))]

            
                
>>>print "Decoded IP: %s %s %s %s" % (a,b,c,d)

            
                
Decoded IP: 10.130.237.59
      
9.破解总结及技巧

9.1 GPU破解模式使用自动优化
在使用GPU模式进行破解时，可以使用-O参数自动进行优化
9.2 暴力破解一条md5值
（1）9位数字破解
 Hashcat64.exe-a 3 --force d98d28ca88f9966cb3aaefebbfc8196f ?d?d?d?d?d?d?d?d?d
单独破解一条md5值需要加force参数
（2）9位字母破解
 Hashcat64.exe-a 3 --force d98d28ca88f9966cb3aaefebbfc8196f ?l?l?l?l?l?l?l?l?l
9.3 破解带盐discuz密码
（1）数字破解
7位数字，7秒时间破解完成任务。
 Hashcat64.exe-a 3 --force -m 2611 ffe1cb31eb084cd7a8dd1228c23617c8:f56463 ?d?d?d?d?d?d?d 
8位数字破解，9秒时间破解完成任务。：
 Hashcat64.exe-a 3 --force -m 2611 ffe1cb31eb084cd7a8dd1228c23617c8:f56463 ?d?d?d?d?d?d?d?d 
9位数字破解，9秒时间破解完成任务。
 Hashcat64.exe-a 3 --force -m 2611 ffe1cb31eb084cd7a8dd1228c23617c8:f56463 ?d?d?d?d?d?d?d?d?d
9.4 字母破解
（1）6位小写字母
 Hashcat64.exe-a 3 --force -m 2611 ffe1cb31eb084cd7a8dd1228c23617c8:f56463 ?l?l?l?l?l?l 
（2）7位小写字母
 Hashcat64.exe-a 3 --force -m 2611 ffe1cb31eb084cd7a8dd1228c23617c8:f56463 ?l?l?l?l?l?l?l 
（3）8位小写字母
 Hashcat64.exe-a 3 --force -m 2611 ffe1cb31eb084cd7a8dd1228c23617c8:f56463 ?l?l?l?l?l?l?l?l 9分钟左右完成破解任务
（4）9位小写字母
 Hashcat64.exe-a 3 --force -m 2611 ffe1cb31eb084cd7a8dd1228c23617c8:f56463 ?l?l?l?l?l?l?l?l?l-O
9.5 字母加数字
 Hashcat64.exe-a 3 --force -m 2611 -2 ?d?l ffe1cb31eb084cd7a8dd1228c23617c8:f56463?2?2?2?2?2?2?2
（3）7位大写字母
 Hashcat64.exe-a 3 –force –m 2611 ffe1cb31eb084cd7a8dd1228c23617c8:f56463 ?u?u?u?u?u?u?u
（4）6到8位数字破解
 Hashcat64.exe-a 3 –force –m 2611 ffe1cb31eb084cd7a8dd1228c23617c8:f56463--increment --increment-min 6 --increment-max 8 ?l?l?l?l?l?l?l?l 
9.6 使用自定义破解
（1）使用数字加字母混合6位进行破解
 Hashcat64.exe-a 3 --force -m 2611 -2 ?d?l ffe1cb31eb084cd7a8dd1228c23617c8:f56463?2?2?2?2?2?2 -O
（2）使用数字加字母混合7位进行破解，破解时间4分16秒
 Hashcat64.exe-a 3 --force -m 2611 -2 ?d?l ffe1cb31eb084cd7a8dd1228c23617c8:f56463?2?2?2?2?2?2?2 –O
（3）使用数字加字母混合8位进行破解
 Hashcat64.exe-a 3 --force -m 2611 -2 ?d?l ffe1cb31eb084cd7a8dd1228c23617c8:f56463?2?2?2?2?2?2?2?2 -O
9.7 字典破解模式
 Hashcat64.exe-a 0 --force -m 2611 ffe1cb31eb084cd7a8dd1228c23617c8:f56463 password.lst
使用字典文件夹下的字典进行破解:
 Hashcat32.exe-m 300 mysqlhashes.txt –remove -o mysql-cracked.txt ..\dictionaries\*
9.8 会话保存及恢复破解
（1）使用mask文件规则来破解密码
 hashcat-m 2611 -a 3 --session mydz dz.hash masks/rockyou-7-2592000.hcmask
（2）恢复会话
 hashcat--session mydz --restore
9.9 掩码破解
mask规则文件位于masks下，例如D:\PentestBox\hashcat-4.1.0\masks，执行破解设置为：
 masks/8char-1l-1u-1d-1s-compliant.hcmask
masks/8char-1l-1u-1d-1s-noncompliant.hcmask
masks/rockyou-1-60.hcmask
masks/rockyou-2-1800.hcmask
masks/rockyou-3-3600.hcmask
masks/rockyou-4-43200.hcmask
masks/rockyou-5-86400.hcmask
masks/rockyou-6-864000.hcmask
masks/rockyou-7-2592000.hcmask
9.10 运用规则文件进行破解
               
Hashcat -m 300 mysqlhashes.txt–remove -o mysql-cracked.txt ..\dictionaries\* -r rules\best64.rule
              
hashcat -m 2611 -a 0 dz.hashpassword.lst  -r rules\best64.rule  -O

9.11 分享几个大字典下载地址
https://crackstation.net/buy-crackstation-wordlist-password-cracking-dictionary.htm
https://weakpass.com/download
