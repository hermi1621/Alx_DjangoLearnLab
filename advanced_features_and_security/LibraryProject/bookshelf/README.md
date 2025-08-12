# LibraryProject

This Django project demonstrates advanced features including custom permissions, user roles, and group-based access control.

## Setup Instructions

- Install dependencies
- Run migrations
- Create user groups and assign permissions
- Start the server and test views with permission restrictions

## Permissions and Groups

- Custom permissions like `can_view`, `can_create`, `can_edit`, `can_delete` are defined in the models.
- Groups such as Editors, Viewers, and Admins have specific permissions.
- Views are protected by Django's `permission_required` decorator.


