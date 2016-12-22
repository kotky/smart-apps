$( document ).ready(function() {
  // Handler for .ready() called.
  GetAllJsonDataAndRender();
});

function GetAllJsonDataAndRender()
{
    var options = {
        url: "/multimeter/api",
        type: "GET",
        dataType: "json",
        timeout: 5000
    };

    $.ajax(options)
    .done(function(data) {
        console.log(data);
        var data_proccessed = []; 
        var dataSeries = { type: "line" };
        var dataPoints = [];
        for (var i = 0; i < data.length; i += 1) {
            dataPoints.push({
              x: data[i].data.i,
              y: data[i].data.y               
            });
        }
        dataSeries.dataPoints = dataPoints;
        data_proccessed.push(dataSeries);
        console.log(data_proccessed);
        multimeter_chart = new CanvasJS.Chart("chartContainer",
        {
          zoomEnabled: true,
          title:{
            text: "Stress Test: 100,000 Data Points" 
          },
          animationEnabled: true,
          axisX:{
            labelAngle: 30
          },
          
          axisY :{
            includeZero:false
          },
          
          data: data_proccessed  // random generator below
          
        });

        multimeter_chart.render();
    })
    .fail(function(data) {
        console.log("Ajax failed to fetch data");
        console.log(data)
    });
}