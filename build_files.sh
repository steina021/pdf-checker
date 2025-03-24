echo "BUILD START"

# Install pipenv if not available
pip install --upgrade pipenv

# Install dependencies from Pipfile.lock (using pipenv)
pipenv install --deploy --ignore-pipfile

# Activate the virtual environment and collect static files
pipenv run python manage.py collectstatic --noinput

echo "BUILD END"
