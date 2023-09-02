One CMS
=====

CMS base structure extend Django Flatpages with GrapeJs


Installation and usage
======================

Quick start
-----------

1. Add "cms" to your INSTALLED_APPS setting like this::

    ``` python
        DJANGO_APPS = [
            ...,
            "django.contrib.flatpages",
        ]

        THIRD_PARTY_APPS = [
           ...,
            "meta",
            "cms",
            "cms.pages",
        ]

    ```

2. Include meta/meta.html template in your templates

    ``` jinja2
        {% load meta %}
        <html>
        <head {% meta_namespaces %}>
            {% include "meta/meta.html" %}
        </head>
        <body>
        </body>
        </html>
    ```

3. Run `python manage.py migrate` to create the cms models.

4. Add the following to your project's apt_router.py file::

    ``` python
        from cms.pages.api.views import FlatPageViewSet
        from cms.ui.api.views import ThemeAPIView, TemplateAPIView
        from django.urls import path

        router.register("pages", FlatPageViewSet)

        urlpatterns += [
            path("themes/", ThemeAPIView.as_view(), name="themes"),
            path("templates/<int:pk>/", TemplateAPIView.as_view(), name="templates"),
        ]
    ```


How to contribute
=================

Please make sure to update tests as appropriate.

Getting Started
---------------

1. Clone the repository

    ``` bash
        # Run the following command in your terminal
        pre-commit install
        git update-index --assume-unchanged .idea/runConfigurations/* .idea/riso.iml
    ```


2. Prepare the environment, Create a virtual environment with Python 3.11 or higher and activate it. Then install the
   dependencies using pip:

    ``` bash
        # Run the following command in your terminal
        cd riso
        pip install -r requirements.txt
    ```

3. Update following files

    ```
        # .envs/.local/.django
        # .envs/.local/.postgres
    ```

4. Then using pycharm runConfiguration to start coding

Useful commands
---------------

- Run test with coverage

    ``` bash
        docker-compose -f riso/local.yml run --rm django pytest --cov --cov-report term-missing --cov-report html
    ```

Other information
=================

What's in this project?
-----------------------

This project is a Django project with a single app called "cms".
