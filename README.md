# drf_advanced

API
    /api/users : List/Create
    /api/users/{pk}: Detail/Update/Delete
    /api/cards: List/Create
    /api/cards{pk}: Detail/Update/Delete
- UserSerializer: contain nested list of cards' detail
- CardSerializer: contain user's primary key 
- test code (CRUD)
- Auth(is_authentication)
- Update/Delete: Owner Only(Permission)
- Global CursorPagination with -id ordering
- cache
- throttling
- login : assign token when logging in 
- logout : delete token when logging out
- card admin : report action
