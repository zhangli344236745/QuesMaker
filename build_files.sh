# build_files.sh
yum update -y
yum install sqlite-devel -y
./configure --enable-optimizations --enable-loadable-sqlite-extensions
make install
pip install pysqlite
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
