import pysftp as sftp

def get_file_from_server():
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    s = sftp.Connection(host = '192.168.209.128',username = 'narsi',password = 'Narasimha143@',cnopts = cnopts)
    remotepath = '/home/narsi/Info1.txt'
    localpath = 'Test.txt'

    s.get(remotepath,localpath)
    s.close()

get_file_from_server()