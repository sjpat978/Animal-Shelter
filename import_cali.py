import os,csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://postgres:postgres@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))


def main():
    f = open("SPCA.csv", "r")  # needs to be opened during reading csv
    reader = csv.reader(f)
    next(reader)
    for ID, AnimalName, Age, AnimalWeight, Gender, Breed, AnimalType, Needs in reader:
        db.execute("INSERT INTO california (ID, AnimalName, Age, AnimalWeight, Gender, Breed, AnimalType, Needs) VALUES (:ID, :AnimalName, :Age, :Gender, :Breed, :AnimalType, :Needs)",
               {"ID": ID, "AnimalName": AnimalName, "Age": Age, "AnimalWeight": AnimalWeight, "Gender": Gender, "Breed": Breed, "AnimalType": AnimalType, "Needs": Needs})
        db.commit()
        print(f"Added animal with ID: {ID} AnimalName: {AnimalName}  Age: {Age}  AnimalWeight: {AnimalWeight} Gender: {Gender} Breed: {Breed} AnimalType: {AnimalType} Needs: {Needs}")


if __name__ == '__main__':
    main()