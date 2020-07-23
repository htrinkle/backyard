var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: [],
        datasets: [{
            label: 'Temperature',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: []
        }]
    },

    // Configuration options go here
    options: {}
});

var gauge = new LinearGauge({
	renderTo: 'myGauge',
	width: 100,
	units: "°C",
	value: 0
}).draw();

function fetchData() {
	fetch('https://backyard.azurewebsites.net/api/hansnodemcu?key=1234abcd')
		.then(response => response.json())
		.then(data => updateData(data));
}
		
function updateData(data) {
    console.log(data);
	
	t_list = data["time"].split(",").map(Number)
	v_list = data["temp"].split(",").map(Number).map(x => x*3.3/10.23)
	
	console.log(t_list)
	console.log(v_list)
    console.log(t_list[t_list.length - 1])	
	
	chart.data['labels'] = t_list
	chart.data['datasets'][0]['data'] = v_list
	chart.update();
	
	gauge.value = v_list[v_list.length - 1]
	gauge.update()
	
}		

var intervalId = setInterval(fetchData, 10000);
fetchData();
		
