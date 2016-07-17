### Database Seed
- Create superuser (`python manage.py createsuperuser`)
- Add objects to database that should be instantiated with database (such as test tasks or test users)
- Run `python manage.py dumpdata auth.User [other models] --indent 4 > todo/fixtures/seed.json`
- Run `./reset.sh` to test