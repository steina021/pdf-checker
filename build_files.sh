echo "BUILD START"

# Install pipenv if not available
pip install --upgrade pipenv

# Install dependencies from Pipfile.lock
pipenv install --deploy

# Run Django collectstatic
pipenv run python manage.py collectstatic --noinput

python3.10 -m pip install -r requirements.txt
python3.10 manage.py collectstatic --noinput --clear

echo "BUILD END"