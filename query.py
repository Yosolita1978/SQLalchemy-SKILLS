"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# It's an object of flask SQLAlchemy. Without finish the query with .all() or .first()
# the query isn't complete, so it's just an object in memory



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# The Association table is useful for relationships on many-to-many.
# It works when you don't have extra information about anything in that table, but you still need to manage the possibility of many to many relationships.
# The example of the book and genre was pretty good.
# A book can have many genres and vice-versa, so you will need to manage that relationship by itself in a different table.




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = db.session.query(Brand).filter(Brand.brand_id == 'ram').first()

# Get all models with the name "Corvette" and the brand_id "che."
q2 = db.session.query(Model).filter(Model.name == "Corvette", Model.brand_id == "che").all()

# Get all models that are older than 1960.
q3 = db.session.query(Model).filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
q4 = db.session.query(Brand).filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor."
q5 = db.session.query(Model).filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = db.session.query(Brand).filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = db.session.query(Brand).filter(Brand.discontinued.isnot(None)).all()

# Get any model whose brand_id is not "for."
q8 = db.session.query(Model).filter(Model.brand_id != "for").all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    models = db.session.query(Model).filter(Model.year == year).all()
    for model in models:
        print model.name, model.brand.name, model.brand.headquarters


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    brands = db.session.query(Brand.name, Model.name, Model.year).join(Model).all()
    for brand in brands:
        brand, model, year = brand
        print brand, model, year


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    mystr = mystr + "%"

    query = db.session.query(Brand).filter(Brand.name.like(mystr)).all()

    return query


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    query = db.session.query(Model).filter(Model.year >= start_year, Model.year < end_year).all()

    return query

