
let animalData = [{
        animalType: 'Dog',
        name = 'Sparky',
        age = 4,
        ID = 19234,
        breed = 'saint bernard',
        medicationsNeed = 'none',
        taken = 'not applicable'
    },
    {
        animalType: 'Hamster',
        name = 'Sparky',
        age = 4,
        ID = 19236,
        breed = 'saint bernard',
        medicationsNeed = 'none',
        taken = 'not applicable'
    },
    {
        animalType: 'Rabbit',
        name = 'Sparky',
        age = 4,
        ID = 19237,
        breed = 'saint bernard',
        medicationsNeed = 'none',
        taken = 'not applicable'
    },
    {
        animalType: 'Dog',
        name = 'Sparky',
        age = 4,
        ID = 19238,
        breed = 'saint bernard',
        medicationsNeed = 'none',
        taken = 'not applicable'
    },
]

class Animal {
    constructor(type, name, age, ID, breed, medNeed) {
        this.animalType = type;
        this.name = name;
        this.age = age;
        this.ID = ID;
        this.breed = breed;
        this.medicationsNeed = medNeed;
    }
}


window.onload = () => {
    loadTableData(animalData);
}

function loadTableData(data) {
    const tableBody = document.getElementById('database-data');
    let dataHTML = '';
    for (let animal of data) {
        dataHTML += `<tr><td>${animal.animalType}</td>
                    <td>${animal.name}</td> 
                    <td>${animal.age}</td>
                    <td>${animal.ID}</td>
                    <td>${animal.breed}</td>
                    <td>${animal.medicationsNeed}</td>
                    <td>${animal.taken}</td>
                    </tr>`
    }

    console.log(dataHTML);
    tableBody.innerHTML = dataHTML

}

document.getElementById('database-addbtn').addEventListener('click', () => {
    console.log('add button clicked')
    const tableFoot = document.getElementById('database-data')
    const addBtns = [document.getElementById('addAnimalbtn'), document.getElementById('database-cancelbtn')]
    tableFoot.style.display = ";"
    for (let i = 0; i < addBtns.length(); i++) {
        addBtns[i].style.display = "inline-block";
    }
});

document.getElementById('addAnimalbtn').addEventListener('click', () => {
    console.log('New Animal Added!')
    let animalType = document.getElementById('animal-type-form').value
    let animalName = document.getElementById('name-form').value
    let animalAge = document.getElementById('age-form').value
    let animalID = document.getElementById('IDnumber-form').value
    let animalBreed = document.getElementById('breed-form').value
    let meds = document.getElementById('medications-form').value

    const newAnimal = Animal(animalType, animalName, animalAge, animalID, animalBreed, meds)
    loadDataform(newAnimal)

});

function loadDataform(Animal) {
    const tableBody = document.getElementById('database-data');
    let dataHTML = '';
    for (const property in Animal) {
        dataHTML += `<tr><td>${animal.animalType}</td>
                    <td>${animal.name}</td> 
                    <td>${animal.age}</td>
                    <td>${animal.ID}</td>
                    <td>${animal.breed}</td>
                    <td>${animal.medicationsNeed}</td>
                    </tr>`
    }

    console.log(dataHTML)
    tableBody.innerHTML = dataHTML
}