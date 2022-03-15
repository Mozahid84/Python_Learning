#!/usr/bin/python

# Plan Old Backup script written in Python
# 
# Filename: backup by: Mozahid Hossain
# Timesamp: 2020-12-30  19:15

import os
from sys import exit
import subprocess
import time
from ConfigParser import SafeConfigParser


conf_file = '../config/config.ini'

currentdate = time.strftime("%Y-%m-%d_%H%M%S")
bkplog = os.path.realpath('../logs/backup_' + currentdate + '.log')
logfile = os.path.realpath('../logs/rman_' + currentdate + '.log')

print('Log files for current session can be found at: ' + bkplog + ' and ' + logfile)





def backup_db(log):
	sid =config.get('db', 'sid')
	cmdfile =config.get('db', 'pob_script')

	log.write('Oracle backup settings: - SID: ' + sid + ' - cmdFile: ' + cmdfile + '\n')

	rmanCMD = 'rman cmdfile="' + cmdfile + '" log="' + logfile + '" target "sys/oracle@orclcdb"'

	os.putenv('NLS_DATE_FORMAT', 'DD-MM-YYYY HH24:MI:SS')
	os.putenv('ORACLE_SID', sid)

	output = subprocess.check_output(rmanCMD, shell=True)

	log.write(output)




# end

if __name__ == "__main__":
	with open(bkplog, 'w') as log:
		if not os.path.exists(conf_file):
			log.write('The config file (' + conf_file + ') does not exist...\n')
			log.write('Backup process was abandoned.\n')
			exit(0)
		config = SafeConfigParser()
		config.read(conf_file)
		backup_db(log)
