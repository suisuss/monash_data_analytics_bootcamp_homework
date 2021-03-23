// from data.js
var tableData = data;
var tbody = d3.select('tbody');
var input = d3.selectAll('input');
var btn = d3.select('button');

populateTable(tableData);
input.on('change', handleChange);
btn.on('click', handleClick);

function populateTable(data) {
    tbody.html("");

    data.forEach(dataRow => {
        var row = tbody.append('tr');

        Object.values(dataRow).forEach(val => {
            var cell = row.append('td');
            cell.text(val);
        });
    });
};

function handleChange() {
    var filteredData = tableData;
    var key = d3.select(this).property('id');
    var value = d3.select(this).property('value');

    if (value) {
        filteredData = filteredData.filter(row => row[key] === value);
    };

    populateTable(filteredData);
}

function handleClick() {
    input.property("value", "");

    var filteredData = tableData;

    populateTable(filteredData);
}