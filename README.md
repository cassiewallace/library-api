# Library API

Library API enables users to manage a set of books.

## Documentation
- [Postman Workspace](https://www.postman.com/cassiewallace/workspace/library-api)

## Requirements
- Python: `3.10.8`
- Django: `2.2.4`

## Running the API locally

1. Install the requirements with `pip install -r requirements.txt`
2. Make sure you're using the development settings `export DJANGO_SETTINGS_MODULE=api.settings_dev`
3. Run the application with `python manage.py runserver`

## Deploying to Heroku

This repository is set up to deploy automatically via [Heroku](https://dashboard.heroku.com/apps/library-api-cw).

If needed, run `git push heroku master` to create a new release on **library-api-cw** on Heroku.
