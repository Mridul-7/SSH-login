#!/usr/bin/python

import pexpect # allows to welcome all the processes in ssh login

PROMPT=['# ','>>> ','> ','\$ ']


def send_command(child,command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before) #print output of command we send to target system

def connect(user,host,password):
    ssh_newkey='Are you sure want to continue connecting'
    connStr='ssh ' +user+ '@' +host #ssh msfadmin@172.16.16.129
    child=pexpect.spawn(connStr)
    ret=child.expect([pexpect.TIMEOUT,ssh_newkey,'[P|p]assword:'])
    #if it returns 0 means we were not able to connect & if it returns 1 connection is successful
    if ret==0:
        print('[-] error connecting')
        return
    if ret==1:
        child.sendline('yes') #send yes string to ssh_newkey
        ret=child.expect([pexpect.TIMEOUT,'[P|p]assword'])
        if ret==0:
            print('[-] error connecting')
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child


def main():
    host=input('Enter host ip:')
    user=input('enter SSH username:')
    password=input('enter SSH password:')
    child=connect(user,host,password)
    send_command(child,'pwd')

main()

