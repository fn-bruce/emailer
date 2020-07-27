=====
Emailer
=====

Emailer is a django app that sends messages to multiple email.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "emailer" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'emailer',
    ]

2. Include the emailer URLconf in your project urls.py like this::

    from django.urls import include
    path('emailer/', include('emailer.urls')),

3. Run ``python manage.py migrate`` to create the email models.

4. Create a ``.env`` file in the root of your project.

5. Within the ``.env`` file, create two variables for email and password:
   
   ``EMAIL=youremailhere@gmail.com``
   ``PASSWORD=yourpasswordhere``

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to create emails (you'll need the Admin app enabled).

7. Visit http://127.0.0.1:8000/emailer/ to start sending emails.
