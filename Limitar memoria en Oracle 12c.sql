[oracle@oracle12c ~]$ sqlplus /nolog

SQL*Plus: Release 12.1.0.2.0 Production on Tue Apr 2 11:43:04 2019

Copyright (c) 1982, 2014, Oracle.  All rights reserved.

SQL> connect / as sysdba
Connected.

SQL> alter system set memory_max_target=24G scope=spfile; 

System altered.


SQL> 

SQL> COLUMN name FORMAT A30
SQL> COLUMN value FORMAT A10
SQL> 
 SELECT name, value
 FROM   v$parameter
 WHERE  name IN ('pga_aggregate_target', 'sga_target')
  UNION
 SELECT 'maximum PGA allocated' AS name, TO_CHAR(value) AS value
  FROM   v$pgastat
  WHERE  name = 'maximum PGA allocated';

-- Calculate MEMORY_TARGET
SELECT sga.value + GREATEST(pga.value, max_pga.value) AS memory_target
FROM (SELECT TO_NUMBER(value) AS value FROM v$parameter WHERE name = 'sga_target') sga,

NAME                           VALUE
------------------------------ ----------
maximum PGA allocated          180789248
pga_aggregate_target           824180736
sga_target                     2483027968    <---- 


     (SELECT TO_NUMBER(value) AS value FROM v$parameter WHERE name = 'pga_aggregate_target') pga,
        (SELECT value FROM v$pgastat WHERE name = 'maximum PGA allocated') max_pga;

MEMORY_TARGET
-------------
   3307208704

SQL> shutdown immediate;
Database closed.
Database dismounted.
ORACLE instance shut down.
SQL> startup
ORACLE instance started.

Total System Global Area 2.5770E+10 bytes
Fixed Size                  2938792 bytes
Variable Size            2.4025E+10 bytes
Database Buffers         1677721600 bytes
Redo Buffers               64167936 bytes
Database mounted.
Database opened.
SQL> 
SQL> -- Individual values.
SQL> COLUMN name FORMAT A30
SQL> COLUMN value FORMAT A10
SQL> 
SELECT name, value
 FROM   v$parameter
 WHERE  name IN ('pga_aggregate_target', 'sga_target')
UNION
  SELECT 'maximum PGA allocated' AS name, TO_CHAR(value) AS value
 FROM   v$pgastat
 WHERE  name = 'maximum PGA allocated';

NAME                           VALUE
------------------------------ ----------
maximum PGA allocated          92451840
pga_aggregate_target           824180736
sga_target                     2483027968   <---- 

SQL> 
SQL> -- Calculate MEMORY_TARGET
SQL> SELECT sga.value + GREATEST(pga.value, max_pga.value) AS memory_target
  2  FROM (SELECT TO_NUMBER(value) AS value FROM v$parameter WHERE name = 'sga_target') sga,
  3       (SELECT TO_NUMBER(value) AS value FROM v$parameter WHERE name = 'pga_aggregate_target') pga,
  4       (SELECT value FROM v$pgastat WHERE name = 'maximum PGA allocated') max_pga;

MEMORY_TARGET
-------------
   3307208704

SQL>
 SELECT sga.value + GREATEST(pga.value, max_pga.value) AS memory_target
 FROM (SELECT TO_NUMBER(value) AS value FROM v$parameter WHERE name = 'sga_target') sga,(SELECT TO_NUMBER(value) AS value FROM v$parameter WHERE name = 'pga_aggregate_target') pga,(SELECT value FROM v$pgastat WHERE name = 'maximum PGA allocated') max_pga;

MEMORY_TARGET
-------------
   3307208704

SQL> shutdown immediate
Database closed.
Database dismounted.
ORACLE instance shut down.
SQL> startup
ORACLE instance started.

Total System Global Area 2.5770E+10 bytes
Fixed Size                  2938792 bytes
Variable Size            2.4025E+10 bytes
Database Buffers         1677721600 bytes
Redo Buffers               64167936 bytes
Database mounted.
Database opened.
SQL> 


++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++


[root@oracle12c ~]# echo 2 > /proc/sys/vm/drop_caches
[root@oracle12c ~]# echo 1 > /proc/sys/vm/drop_caches
[root@oracle12c ~]# echo 2 > /proc/sys/vm/drop_cache
[root@oracle12c ~]# echo 3 > /proc/sys/vm/drop_caches


SQL> alter system set memory_max_target=24G scope=spfile; 

System altered.

SQL> create pfile from spfile;

File created.

SQL> shutdown immediate;
Database closed.
Database dismounted.
ORACLE instance shut down.
SQL> startup
ORACLE instance started.

Total System Global Area 2.5770E+10 bytes
Fixed Size                  2938792 bytes
Variable Size            2.4025E+10 bytes
Database Buffers         1677721600 bytes
Redo Buffers               64167936 bytes
Database mounted.
Database opened.
----------------------------------------------------------------------------
 SELECT name, value
    FROM   v$parameter
     WHERE  name IN ('pga_aggregate_target', 'sga_target')
   UNION
     SELECT 'maximum PGA allocated' AS name, TO_CHAR(value) AS value
    FROM   v$pgastat
   WHERE  name = 'maximum PGA allocated';
----------------------------------------------------------------------------

NAME                           VALUE
------------------------------ ----------
maximum PGA allocated          69583872
pga_aggregate_target           824180736
sga_target                     2483027968

SQL>