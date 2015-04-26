__author__ = 'tian'

import os
import platform
import subprocess
import telnetlib

from Connection import Connection


class OpenVPNException(Exception):
    pass


class OpenVPNConnection(Connection):
    def __init__(self, **kwargs):
        super().__init__()
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.connected = False

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
            if hasattr(self, 'auth'):
                call_line = ' '.join([
                    'openvpn',
                    '--daemon',
                    '--cd', self.cd,
                    '--config', self.config,
                    '--cd', self.cd,
                    '--auth-user-pass', self.auth,
                    '--management', '127.0.0.1', str(self.management_port),
                    '--management-query-passwords',
                    '--management-hold',
                    '--script-security', '2'
                    '--up', self.up_script,
                    '--down', self.down_script,
                ])
            else:
                call_line = ' '.join([
                    'openvpn',
                    '--daemon',
                    '--cd', self.cd,
                    '--config', self.config,
                    '--cd', self.cd,
                    '--management', '127.0.0.1', str(self.management_port),
                    '--management-query-passwords',
                    '--management-hold',
                    '--script-security', '2'
                    '--up', self.up_script,
                    '--down', self.down_script,
                ])

            #print('Run VPN: call_line:')
            #print(call_line)
            #print('END')
            try:
                subprocess.check_call(call_line, shell=True)
            except subprocess.CalledProcessError as e:
                print(e.cmd)
                print(e.returncode)
                print(e.output)
                raise OpenVPNException('Failed to run VPN', e.cmd, e.output)

            port = self.management_port
            # port = 1337
            telnet_talk = telnetlib.Telnet()

            try:
                # initial connection to release the hold
                telnet_talk.open('127.0.0.1', port)
                telnet_talk.write(b'hold release\r\n')
                telnet_talk.write(b'state on\r\n')
                msg = telnet_talk.read_until(b'CONNECTED,SUCCESS')
                telnet_talk.close()
                # second connection to make sure we fully connected
                telnet_talk.open('127.0.0.1', port)
                telnet_talk.write(b'state\r\n')
                msg = telnet_talk.read_until(b'CONNECTED,SUCCESS')
                telnet_talk.close()
                self.connected = True

            except ConnectionRefusedError:
                self.connected = False

            except ConnectionResetError:
                self.connected = False

            if not self.connected:
                raise OpenVPNException('Cannot connect')


        else:
            # platform not supported
            raise NotImplemented

        pass

    def close(self):
        if not self.connected:
            return
        port = self.management_port
        telnet_talk = telnetlib.Telnet()
        try:
            telnet_talk.open('127.0.0.1', port)
            telnet_talk.write(b'signal SIGTERM\r\n')
            telnet_talk.read_all()
            telnet_talk.close()
        except ConnectionRefusedError:
            raise OpenVPNException('Cannot connect to management')
