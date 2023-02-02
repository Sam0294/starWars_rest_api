from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    password = Column(String(250))


class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey("planet.id"))
    planet = relationship(Planet)
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
    vehicle = relationship(Vehicle)
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship(Character)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    diammeter = Column(String(250))
    gravity = Column(String(250))


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    Speed = Column(String(250))


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    Gender = Column(String(250))
    Age = Column(String(250))
    Eye_color = Column(String(250))

