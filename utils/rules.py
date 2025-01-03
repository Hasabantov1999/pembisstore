# rules.py

rules = {
    "admin": ["users_create", "users_delete", "users_update", "users_view"],
    "editor": ["users_update", "users_view"],
    "viewer": ["users_view"],
}