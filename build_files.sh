# build_files.sh
which python3.9
pwd
cd /vercel/path0/
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
