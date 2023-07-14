import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    is_active= Column(Boolean(), unique=False, nullable=False) 
    favorites = relationship("Favorites", backref="user", lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False, unique=True)
    climate = Column(String, nullable=False)
    created = Column(String, nullable=False)
    diameter = Column(String, nullable=False)
    films = Column(String, nullable=False)
    gravity = Column(String, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    surface_water = Column(Integer, nullable=False)
    terrain = Column(String, nullable=False)
    favorites = relationship("Favorites", backref="planet", lazy=True)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    cargo_capacity = Column(Integer, nullable=False)
    created = Column(String, nullable=False)
    crew = Column(Integer, nullable=False)
    length = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    model = Column(String, nullable=False)
    vehicle_class = Column(String, nullable=False)
    url = Column(String, nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    edited = Column(DateTime, nullable=False)
    favorites = relationship("Favorites", backref="vehicle", lazy=True)

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    birth_year = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    homeworld = Column(String, nullable=False)
    films = Column(String, nullable=False)
    species = Column(String, nullable=False)
    vehicles = Column(String, nullable=False)
    starships = Column(String, nullable=False)
    created = Column(DateTime)
    edited = Column(DateTime)
    url = Column(String)
    favorites = relationship("Favorites", backref="character", lazy=True)

    
class Favorites(Base):
    __tablename__="favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
    character_id = Column(Integer, ForeignKey("character.id"))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
