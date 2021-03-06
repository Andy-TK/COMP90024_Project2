import os
import pexpect
import sys
import time
import logging

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                        level=logging.INFO)
    logging.info('Start to build Openstack instance:')

    process = pexpect.spawn('sh ./script_os.sh')
    process.logfile_read = sys.stdout.buffer
    process.expect(
        'Please enter your OpenStack Password for project unimelb-comp90024-group-35 as user haoyu.zhang@student.unimelb.edu.au:')
    process.sendline('YTljYzQzZTM1OTkwNjY4')
    i = process.expect('BECOME password:')
    process.sendline('9588')
    process.expect(pexpect.EOF, timeout=300)

    # pexpect.run('sh ./script_os.sh', events={
    #     'Please enter your OpenStack Password for project unimelb-comp90024-group-35 as user haoyu.zhang@student.unimelb.edu.au:': 'YTljYzQzZTM1OTkwNjY4\n',
    #     'BECOME password:':'9588\n'
    # }, logfile=sys.stdout.buffer)

    logging.info('Waiting for setting up instance for 3 minutes:')
    time.sleep(180)

    for name in ['WebServer', 'CouchDB', 'Harvest','DataAnalysis']:
        logging.info('Start to build ' + name +':')
        pexpect.run('ansible-playbook -i hosts -u ubuntu --key-file=CCC.pem Automation_'+ name +'.yml',
                    events={'Are you sure you want to continue connecting (yes/no)?': 'yes\n'},
                    logfile=sys.stdout.buffer, timeout=600)



    # pexpect.run('sh ./script_os.sh', events={
    #     'Please enter your OpenStack Password for project unimelb-comp90024-group-35 as user haoyu.zhang@student.unimelb.edu.au:': 'YTljYzQzZTM1OTkwNjY4\n',
    #     'BECOME password:':'9588\n'
    # }, logfile=sys.stdout.buffer)

