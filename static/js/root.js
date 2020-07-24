var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'scatter',

    // The data for our dataset
    data: {
        datasets: [{
            label: 'Temperature',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: []
        }]
    },

    // Configuration options go here
    options: {
      legend: false,
      scales: {
        xAxes: [{
          ticks: {
            callback: function(value, index, values) {
              return moment(value*1000).format('DD:MM:YYYY h:mm a')
            }
          }
        }],
      }
    }
});

var gaugeTest = document.getElementById('gaugeText')
var gauge = new LinearGauge({
	renderTo: 'myGauge',
	width: 100,
    height: 400,
	units: "°C",
	value: 0
}).draw();

var n = 100

function fetchData() {
	fetch('https://backyard.azurewebsites.net/api/hansnodemcu?key=1234abcd&n='+n.toString())
		.then(response => response.json())
		.then(data => updateData(data));
}
		
function updateData(data) {
    console.log(data);
	
	t_list = data["time"].split(",").map(Number)
	v_list = data["temp"].split(",").map(Number).map(x => x*3.3/10.23)
	
	console.log(t_list)
	console.log(v_list)

    var data = []
    for (i=0; i<v_list.length; i++) {
      data.push({'x':t_list[i], 'y':v_list[i]})
    }

	chart.data['datasets'][0]['data'] = data
	chart.update();
	
	gauge.value = v_list[v_list.length - 1]
    gaugeText.innerHTML = "Temperature of " +
      v_list[v_list.length-1].toFixed(1).toString() + " °C" +
      " was recorded at " + 
      moment(t_list[t_list.length -1]*1000).format('DD:MM:YYYY h:mm:ss a')
      
	gauge.update()
	
}	
	
document.getElementById("numSamples").value = n

function setN() {
  n=document.getElementById("numSamples").value
  console.log(n);
  fetchData();
}

var intervalId = setInterval(fetchData, 10000);
fetchData();
		
