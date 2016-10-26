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
    })
    .fail(function(data) {
        console.log("Ajax failed to fetch data");
        console.log(data)
    });
}