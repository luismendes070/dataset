# https://docs.sqlalchemy.org/en/14/orm/session_basics.html#what-does-the-session-do
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# an Engine, which the Session will use for connection
# resources
engine = create_engine("postgresql://scott:tiger@localhost/")

# create session and add objects
with Session(engine) as session:
    session.add(some_object)
    session.add(some_other_object)
    session.commit()