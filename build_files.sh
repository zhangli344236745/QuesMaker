# build_files.sh
yum install sqlite-devel -y
./configure --enable-optimizations --enable-loadable-sqlite-extensions
make install
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
