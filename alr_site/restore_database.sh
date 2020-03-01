#this resets the database assuming fixures/restore_db.json exists
#to make restore_db.json run python manage.py dumpdata >> restore_db.json
# then make a fixtures folder and move it there

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete 
rm sqlite3_default.db
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/restore_db.json