#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pyshark

path = 'C:\\Users\\wf\\Desktop\\sip_info.pcap'

def check_dtmf_method(key=None):
    """
    pyshark运行需要安装tshark，安装命令sudo apt-get install tshark
    解析DTMF方式
    :param path: 完整的抓包路径
    :param key: 关键字
    :return: sdp媒体行
    """
    #log = Logger()
    path = 'C:\\Users\\wf\\Desktop\\sip_info.pcap'
    try:
        cap = pyshark.FileCapture(path, display_filter='sip or rtpevent')
        result = []
        for pkt in cap:
            try:
                if key == 'rfc2833':
                    pass
                elif key == 'sip info':
                    cap = pyshark.FileCapture(path, display_filter='sip.Method == INFO')
                    try:
                        for pkt in cap:
                            if 'INFO sip' in pkt.sip.request_line:
                                msg_hdr = str(pkt.sip.msg_hdr).split('\\xd\\xa')
                                for item in msg_hdr:
                                    if 'Signal=' in item:
                                        cap.close()
                                        result.append(item)
                                        # print(result)
                        cap.close()
                    except:
                        continue

            except:
                continue
        return result
    except Exception as e:
        if 'TShark seems to have crashed (retcode: 2)' in str(e):
            cap.close()
            return None

check_dtmf_method(key='sip info')