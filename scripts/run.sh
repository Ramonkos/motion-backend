
gunicorn -w 4 -b 0.0.0.0:8000 app/project/wsgi.py:app --reload