import os
import pexpect
import sys
import time

if __name__ == "__main__":
    process = pexpect.spawn('sh ./script_os.sh')
    process.logfile_read = sys.stdout.buffer
    process.expect(
        'Please enter your OpenStack Password for project unimelb-comp90024-group-35 as user haoyu.zhang@student.unimelb.edu.au:')
    process.sendline('YTljYzQzZTM1OTkwNjY4')
    i = process.expect('BECOME password:')
    process.sendline('9588')
    process.expect(pexpect.EOF)


    time.sleep(300)

    pexpect.run('sh ./script_web.sh', logfile=sys.stdout.buffer)



    # pexpect.run('sh ./script_os.sh', events={
    #     'Please enter your OpenStack Password for project unimelb-comp90024-group-35 as user haoyu.zhang@student.unimelb.edu.au:': 'YTljYzQzZTM1OTkwNjY4\n',
    #     'BECOME password:':'9588\n'
    # }, logfile=sys.stdout.buffer)

