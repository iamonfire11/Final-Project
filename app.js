var connectionURL = "http://172.16.188.15:3000"

window.onload = function() { 
    sessionStorage.clear();
    drawTableBody();
};

function addTableHead(){
    var table = document.getElementById("content-table");
    var header = table.createTHead();
    var row = header.insertRow(0);

    var workstationIDHead = row.insertCell(0);
    var coughHead = row.insertCell(1);
    var tempHead = row.insertCell(2);
    var lastupdatedHead = row.insertCell(3);

    workstationIDHead.innerHTML = "Workstation";
    coughHead.innerHTML = "Coughs per day";
    tempHead.innerHTML = "Temperature";
    lastupdatedHead.innerHTML = "Last Updated";  
}

function addTableBody(user){
    var table = document.getElementById("content-table");

    var row = table.insertRow(0);
   
    var workstationIDContent = row.insertCell(0);
    var coughContent = row.insertCell(1);
    var tempContent = row.insertCell(2);
    var lastupdatedContent = row.insertCell(3);

    workstationIDContent.innerHTML = user.workstation;
    coughContent.innerHTML = user.cough_count;
    tempContent.innerHTML = user.temperature;
    lastupdatedContent.innerHTML = user.last_updated.$date;  
}

function getUsers(){
    return fetch(connectionURL.concat("/user"))
    .then((res) => res.json())
    .then((json) => json);
}

async function drawTableBody(){
    let users = await getUsers();

    users.forEach((user) => {
        addTableBody(user);
    });
    addTableHead();
}
