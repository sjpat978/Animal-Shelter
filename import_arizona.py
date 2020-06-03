import os,csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://postgres:postgres@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))


def main():
    f = open("arizona.csv", "r")  # needs to be opened during reading csv
    reader = csv.reader(f)
    next(reader)
    for ID, AnimalName, Age, Gender, Breed, AnimalType in reader:
        db.execute("INSERT INTO arizona (ID, AnimalName, Age, Gender, Breed, AnimalType) VALUES (:ID, :AnimalName, :Age, :Gender, :Breed, :AnimalType)",
               {"ID": ID, "AnimalName": AnimalName, "Age": Age, "Gender": Gender, "Breed": Breed, "AnimalType": AnimalType})
        db.commit()
        print(f"Added animal with ID: {ID} Name: {AnimalName}  Age: {Age}  Gender: {Gender} Breed: {Breed} Type: {AnimalType}")


if __name__ == '__main__':
    main()