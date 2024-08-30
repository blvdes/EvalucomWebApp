Evalucom Web Application Submission


Prerequisites:
- python3
- Django
- requests


To run:
- Make sure working directory is /webproject and create Python virtual environment.
- 'python manage.py migrate' - Creates tables in database, unapplied migrations will cause project to not run.
- 'python manage.py runserver'


Features:
- Paged results of movies under the TMDB 'Now Playing' category.
- Search function using TMDB API queries.
- Review movies returned on pages or search result, saved in database table.
- Movie detail expansion on review page.
- View all previous reviews submitted.
