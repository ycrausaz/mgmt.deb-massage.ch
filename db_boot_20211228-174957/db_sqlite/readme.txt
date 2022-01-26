cat ../Contacts_deb-massage-ch.csv | sed -e 's/NULL//g' > Contacts_deb-massage-ch_NO-NULL.csv
sqlite3 ../../DebMassageCh/db.sqlite3
.read db_script.txt
.quit
