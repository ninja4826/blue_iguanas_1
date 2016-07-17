rm -rf ./db.sqlite3
python ./manage.py migrate
# python ./manage.py loaddata seed

if [ -e ./todo/fixtures/seed.json ]; then
    python ./manage.py loaddata seed
fi