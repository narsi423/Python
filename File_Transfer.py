import pysftp as sftp

def push_file_to_server():
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    s = sftp.Connection(host = '192.168.209.128',username = 'narsi',password = 'Narasimha143@',cnopts = cnopts)
    remotepath = '/home/narsi/Info1.txt'
    localpath = 'Info.txt'

    s.put(localpath, remotepath)
    s.close()

push_file_to_server()
