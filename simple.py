import sqlitedl
db = sqlitedl.sqlite('FILE.db')
create_db = db.create()
create_db.table('users', True, '**-id, &-username, #-balance, *-tab')