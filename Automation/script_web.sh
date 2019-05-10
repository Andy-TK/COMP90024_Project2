#! /bin/bash

. ./OpenStack.sh; ansible-playbook -i hosts -u ubuntu --key-file=CCC.pem Automation_WebServer.yml