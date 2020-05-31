let sortDirection = false;

let animalData = [
    {animalType: 'Dog', name = 'Sparky', age=4, ID = 19234, breed = 'saint bernard', medicationsNeed = 'none', taken='not applicable' },
    {animalType: 'Hamster', name = 'Sparky', age=4, ID = 19236, breed = 'saint bernard' ,medicationsNeed = 'none', taken='not applicable' },
    {animalType: 'Rabbit', name = 'Sparky', age=4, ID = 19237, breed = 'saint bernard' ,medicationsNeed = 'none', taken='not applicable' },
    {animalType: 'Dog', name = 'Sparky', age=4, ID = 19238, breed = 'saint bernard' ,medicationsNeed = 'none', taken='not applicable' },
]

class Animal {
    constructor(type, name, age, ID, breed, medNeed, taken) {
        this.animalType = type;
        this.name = name;
        this.age = age;
        this.ID = ID;
        this.breed = breed;
        this.medicationsNeed = medNeed;
        this.medsTaken = taken;
    }
}


window.onload = () => {
    loadTableData(animalData);
}

function loadTableData(data){
    const tableBody = document.getElementById('database-data');
    let dataHTML = '';
    for(let animal of data){
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

}

document.getElementById('database-addbtn').addEventListener('click', () => {
    console.log('add button clicked')
    const tableFoot = document.getElementById('database-data')
    let formHTML = '';
    
     
});

document.getElementById('database-removebtn').addEventListener('click', () => {
    console.log('remove button clicked')
});
