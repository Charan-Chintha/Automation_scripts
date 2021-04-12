while [ 1 ]; do 
    if [ `mysql -uuser -ppass -hhost -e"show slave status \G;" | grep "Duplicate entry" | wc -l` -eq 2 ] ; then 
        mysql -uuser -ppass -hhost -e"stop slave; set global sql_slave_skip_counter=1; start slave;"; 
    fi; 
    sleep 1; 
    mysql -uuser -ppass -hhost -e"show slave status\G"; 
done