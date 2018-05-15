function getData(dataset) {
    var data = [];
    switch (dataset) {
    case "dataset1":
      data = [1, 2, 3, 39];
      break;
    case "dataset2":
      data = [10, 20, 30, 37];
      break;
    case "dataset3":
      data = [100, 200, 300, 23];
      break;
    default:
      data = [30, 30, 30, 11];
    }
    updatePlotly(data);
  }
  

// function buildPlot() {
//     /* data route */
//     var url = "/api/pals";
//     Plotly.d3.json(url, function(error, response) {

//         console.log(response);

//         var data = [response]

//         var layout = {
//             title: "Pet Pals",
//             xaxis: {
//                 title: "Pet Type"
//             },
//             yaxis: {
//                 title: "Number of Pals"
//             }
//         };

//         Plotly.newPlot("plot", data, layout);
//     });
// }

// buildPlot();