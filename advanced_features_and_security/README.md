# Permissions and Groups Setup

## Overview

This document outlines the access control system implemented for the `bookshelf` application. We use Django’s built-in Group and Permission system to ensure that users can only perform actions authorized by their assigned roles.

## Custom Permissions

The `Book` model has been updated with the following custom permissions defined in its `Meta` class:

- `can_view`: Allows a user to see the list of books.
- `can_create`: Allows a user to add new book entries.
- `can_edit`: Allows a user to modify existing book details.
- `can_delete`: Allows a user to remove a book from the database.

## Groups and Role Mapping

We have established three primary groups to manage user access:

| Group Name  | Permissions Assigned                               |
| :---------- | :------------------------------------------------- |
| **Viewers** | `can_view`                                         |
| **Editors** | `can_view`, `can_create`, `can_edit`               |
| **Admins**  | `can_view`, `can_create`, `can_edit`, `can_delete` |

## Enforcement

These permissions are enforced at the view level using the `@permission_required` decorator. If a user attempts to access a view without the required permission, Django will raise a `403 Forbidden` error.

### Example View Protection

```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    # Logic for editing a book
```
