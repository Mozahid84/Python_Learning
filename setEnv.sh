# Oracle Settings
export TMP=/tmp
export TMPDIR=$TMP

export ORACLE_HOSTNAME=osboxes
export ORACLE_UNQNAME=ORCLCDB
export ORACLE_BASE=/opt/oracle
export ORACLE_HOME=$ORACLE_BASE/product/19c/dbhome_1
export ORA_INVENTORY=/opt/oracle/oraInventory
export ORACLE_SID=ORCLCDB
export PDB_NAME=ORCLPDB1
export DATA_DIR=/opt/oracle/oradata

export PATH=/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:/home/osboxes/.local/bin:/home/osboxes/bin
export PATH=$PATH:$ORACLE_HOME/bin

export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
export CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib
