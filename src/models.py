import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class FavoritesPerson(Base):
    __tablename__ = 'favoritesperson'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    rating = Column(Integer, nullable = True) 

class FavoritesPlanets(Base):
    __tablename__ = 'favoritesplanets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    

class FavoritesVehicles(Base):
    __tablename__ = 'favoritevehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
   

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(20), nullable=False)
    eyes_color = Column(String(20), nullable = True) #nullable = True es que se puede dejar vacía la información
    birth_year = Column(String(250), nullable = False)
    skin_color = Column(String(250), nullable = False)
    height = Column(Integer, nullable = False)
    homeworld = Column(String(250), nullable = False)
    film = Column(Integer, nullable = False)
    mass = Column(Integer, nullable = False)
    created = Column(String(250), nullable = False)
    edited = Column(String(250), nullable = False)
    species = Column(Integer, nullable = False)
    starships = Column(Integer, nullable = False)
    url = Column(String(250), nullable = False)
    vehicles = Column(Integer, nullable = False)
    hair_color = Column(String(250), nullable = False)
    favorites_person = relationship(FavoritesPerson, backref='person', lazy=True) #backref es una autoreferencia


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    age = Column(Integer, nullable = False)
    favorites_person = relationship(FavoritesPerson, backref='user', lazy=True)

    
class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    cargo_capacity= Column(Integer, nullable=False)
    consumables = Column(String(20), nullable=False)
    cost_in_credits = Column(Integer, nullable = True) 
    created = Column(String(250), nullable = False)
    crew = Column(Integer, nullable = False)
    edited = Column(String(250), nullable = False)
    length = Column(Integer, nullable = False)
    manufacturer = Column(String(250), nullable = False)
    max_atmosphering_speed = Column(Integer, nullable = False)
    name = Column(String(250), nullable = False)
    passengers = Column(Integer, nullable = False)
    pilots = Column(Integer, nullable = False)
    films = Column(Integer, nullable = False)
    url = Column(String(250), nullable = False)
    vehicle_class = Column(String(250), nullable = False)
    favorites_veicles = relationship(FavoritesVehicles, backref='person', lazy=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    climate= Column(Integer, nullable=False)
    created = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable = True)
    gravity = Column(Integer, nullable = False)
    edited = Column(String(250), nullable = False)
    films = Column(String(250), nullable = False)
    name = Column(String(250), nullable = False)
    orbital_period = Column(Integer, nullable = False)
    population = Column(Integer, nullable = False)
    residents= Column(String(250), nullable = False)
    rotation_period = Column(Integer, nullable = False)
    surface_water = Column(Integer, nullable = False)
    terrain = Column(String(250), nullable = False)
    url = Column(String(250), nullable = False)
    favorites_planets = relationship(FavoritesPlanets, backref='person', lazy=True)
    


render_er(Base, 'diagram.png')
