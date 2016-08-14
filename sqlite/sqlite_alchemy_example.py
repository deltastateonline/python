# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 19:13:07 2016

@author: developer
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlite_alchemy import Address, Base, Person,Contact

engine = create_engine("sqlite:////home/developer/python/sqlite/data/person.sqlite")


DBSession = sessionmaker(bind = engine)

session = DBSession()

new_person = Person(name="Dextada Daps")
session.add(new_person)
session.commit()

new_address = Address(post_code="QLD 4509",person= new_person)
session.add(new_address)
session.commit()

new_contact = Contact(detail_type="email",
                      detail_value="dex@yahoo.co.uk",person= new_person)
                      
new_contact1 = Contact(detail_type="email",
                      detail_value="brazil@hotmail.com.au",person= new_person)
                      
session.add(new_contact)
session.add(new_contact1)
session.commit()                      
