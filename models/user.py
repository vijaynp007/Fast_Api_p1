from sqlalchemy import Table,Column
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer,String

user = Table(
            'user',meta,
            Column('id',Integer , primary_key=True),
             Column('name',String(250)),
              Column('emil',String(250)),
               Column('password',String(250)),
)



