## Database backup and restore -- POSTGRESQL

### Database backup to file
using pg_dump
```bash
$ docker-compose exec postgres pg_dump -U postgres cpo > db_backup/dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
OR -- must investigate further!!! --
$ docker-compose run --rm postgres pg_dumpall -c -U postgres cpo> dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
```

### Database restore from file
copy the dump to the container. [see ref](https://blog.dcycle.com/blog/ae67284c/docker-compose-cp)
```bash
$ docker cp db_backup/dump_date_xx_yy_zz.sql "$(docker-compose ps -q postgres)":/dump.sql
```

using pql. pg_restore (as an alternative requires a .dump file. i.e. `pg_dump -Fc cpo > dump_blah.dump`)
```bash
$ docker-compose exec postgres dropdb -U postgres cpo
AND
$ docker-compose exec postgres psql -U postgres -d cpo -f dump.sql
```

### Database backup to file
```bash
$ docker-compose run --rm postgres pg_dumpall -c -U postgres cpo> dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
OR
$ docker-compose run --rm postgres pg_dump --username postgres --password postgres cpo > pg_dump.sql
```
