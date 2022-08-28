# build_files.sh
which python3.9
ls
cd /Python-*/
yum install sqlite-devel -y
./configure --enable-optimizations --enable-loadable-sqlite-extensions
make && make altinstall
cd ~
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
