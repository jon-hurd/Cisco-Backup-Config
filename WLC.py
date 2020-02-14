#code from https://www.semfionetworks.com/blog/python-how-to-connect-to-a-cisco-wlc-aireos
#!/usr/bin/env python

from netmiko import ConnectHandler

with ConnectHandler(ip = '192.168.20.2',
                        port = 22,
                        username = 'admin',
                        password = 'Cisco123!',
                        device_type = 'cisco_wlc_ssh') as ch:
    print(ch.send_command("show ap summary"))