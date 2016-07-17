rm -rf ./db.sqlite3
python ./manage.py migrate
if [ -e ./todo/fixtures/seed.json ]; then
    python ./manage.py loaddata seed
fi