__author__ = 'tian'

import os
import platform
import subprocess
import telnetlib

from Connection import Connection


class OpenVPNException(Exception):
    def __ini__(self, msg):
        super().__init__(msg)


class OpenVPNConnection(Connection):
    def __init__(self, **kwargs):
        super().__init__()

        for key, value in kwargs:
            setattr(self, key, value)

    def connect(self):
        if platform.system() == 'Darwin':
            # OS X

            """
            openvpn \
            --daemon \
            --cd "$config_dir" \
            --config "$config_dir/$config_file" \
            --cd "$config_dir" \
            --auth-user-pass "$config_dir/$auth_file" \
            --management 127.0.0.1 1337 \
            --management-query-passwords \
            --management-hold \
            --script-security \
            2 \
            --up \
            "'$updown_dir/client.up.tunnelblick.sh' -d -f -m -w -ptADGNWradsgnw" \
            --down \
            "$updown_dir/client.down.tunnelblick.sh -d -f -m -w -ptADGNWradsgnw"
            """

            # set up

            call_line = [
                'openvpn',
                '--daemon',
                '--cd', self.cd,
                '--config', self.config,
                '--cd', self.cd,
                '--auth-user-pass', self.auth,
                '--management', '127.0.0.1', self.management_port,
                '--management-query-password',
                '--management-hold',
                '--script-security',
                '--up', self.up_script,
                '--down', self.down_script,
            ]

            try:
                subprocess.check_call(call_line)
            except subprocess.CalledProcessError:
                raise OpenVPNException

            port = self.management_port
            # delete the following line
            port = 1337
            telnet_talk = telnetlib.Telnet()
            telnet_talk.open('127.0.0.1', port)
            telnet_talk.write(b'hold release\r\n')
            telnet_talk.write(b'state on\r\n')
            telnet_talk.read_until(b'CONNECTED,SUCCESS')
            rest = telnet_talk.read_until(b'\r\n')
            telnet_talk.close()

        else:
            # platform not supported
            raise NotImplemented

        pass

    def close(self):
        port = self.management_port
        port = 1337
        telnet_talk = telnetlib.Telnet()
        telnet_talk.open('127.0.0.1', port)
        telnet_talk.write(b'signal SIGTERM\r\n')
        telnet_talk.read_all()
        telnet_talk.close()
