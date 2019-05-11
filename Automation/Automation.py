import os
import pexpect
import sys

if __name__ == "__main__":
    process = pexpect.spawn('sh ./script_os.sh')
    #                     events={
    # 'Please enter your OpenStack Password for project unimelb-comp90024-group-35 as user haoyu.zhang@student.unimelb.edu.au:': 'YTljYzQzZTM1OTkwNjY4\n',
    # 'BECOME password:': '9588\n'
    # }, logfile=sys.stdout.buffer)
    process.logfile_read = sys.stdout.buffer
    process.expect(
        'Please enter your OpenStack Password for project unimelb-comp90024-group-35 as user haoyu.zhang@student.unimelb.edu.au:')
    process.sendline('YTljYzQzZTM1OTkwNjY4')
    i = process.expect('BECOME password:')
    process.sendline('9588')
    process.expect(pexpect.EOF)
    # pattern = "\n(\S+).*?([0-9]+)%"
    # filesystem_list = []

    # for dummy in range(0, 100):
    #     try:
    #         i = process.expect('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    #         if i == 0:
    #             f = open("hosts", "a+")
    #             # print(process.match.group(0))
    #             string = str(process.match.group(0), encoding="utf-8")
    #             f.write(string)
    #             f.close()
    #     except:
    #         break

    pexpect.run

