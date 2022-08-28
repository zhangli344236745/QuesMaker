# build_files.sh
hostnamectl
apt-get update && apt-get install libsqlite3-dev sqlite-devel
./configure --enable-loadable-sqlite-extensions && make && make install
pip install pysqlite
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
