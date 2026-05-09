from database import *
from tables import *

# Create the tables
def create_tables() :
    Base.metadata.create_all(bind=engine)

