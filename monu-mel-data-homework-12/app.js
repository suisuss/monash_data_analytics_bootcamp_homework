
function getPlot(id) {
    
  // Read in data
  d3.json("data/samples.json").then((data)=> {
      console.log(data)

      var wfreq = data.metadata.map(d => d.wfreq)
      console.log(`Washing Freq: ${wfreq}`)

      // Filtered sample values by ID 
      var samples = data.samples.filter(s => s.id.toString() === id)[0];

      console.log(`Samples: ${samples}`);

      // Top 10 sample values to plot and reverse
      var sampleValues = samples.sample_values.slice(0, 10).reverse();

      // Top 10 otu ids
      var idValues = (samples.otu_ids.slice(0, 10)).reverse();
      
      // OTU id's in the desired format for the plot
      var idOtu = idValues.map(d => "OTU " + d)

      console.log(`OTU IDS: ${idOtu}`)

      // get the top 10 labels for the plot
      var labels = samples.otu_labels.slice(0, 10);

      console.log(`Sample Values: ${sampleValues}`)
      console.log(`Id Values: ${idValues}`)

      // Bar chart data + layout
      var barChartData = [{
          x: sampleValues,
          y: idOtu,
          text: labels,
          type:"bar",
          orientation: "h",
      }];

      var barChartLayout = {
          title: "Top 10 OTU",
          yaxis:{
              tickmode:"linear",
          },
          margin: {
              l: 100,
              r: 100,
              t: 30,
              b: 20
          }
      };

      // Bar chart plot
      Plotly.newPlot("bar", barChartData, barChartLayout);

      console.log(`IDs: ${samples.otu_ids}`)
      
      // Bubble chart data + layout
      var bubbleChartData = [{
          x: samples.otu_ids,
          y: samples.sample_values,
          mode: "markers",
          marker: {
              size: samples.sample_values,
              color: samples.otu_ids
          },
          text: samples.otu_labels

      }];

      var bubbleChartLayout = {
          xaxis:{title: "OTU ID"},
          height: 600,
          width: 1300
      };

      // Bubble chart plot
      Plotly.newPlot("bubble", bubbleChartData, bubbleChartLayout); 

      // Pie chart data
      var pieChartData = [{
          labels: idOtu,
          values:sampleValues,
          type:"pie",
      }]
      
      // Pie chart plot
      Plotly.newPlot("pie", pieChartData)

  });    
}

function getInfo(id) {
  // Read in data
  d3.json("data/samples.json").then((data)=> {
      
      // Metadata info for demographic panel
      var metadata = data.metadata;

      console.log(`Metadata: ${metadata}`)

      // Filtered meta data info by ID
      var result = metadata.filter(meta => meta.id.toString() === id)[0];

      // Selected demographic panel html element
      var demographicInfo = d3.select("#sample-metadata");
      
      // Empty the demographic info panel incase there was a pervious id plot
      demographicInfo.html("");

      // Demographic data for the id and append the info to the panel
      Object.entries(result).forEach((key) => {   
              demographicInfo.append("h5").text(key[0].toUpperCase() + ": " + key[1] + "\n");    
      });
  });
}

// create the function for the change event
function optionChanged(id) {
  getPlot(id);
  getInfo(id);
}

// create the function for the initial data rendering
function init() {
  // select dropdown menu 
  var dropdown = d3.select("#selDataset");

  // read the data 
  d3.json("data/samples.json").then((data)=> {
      console.log(`Data: ${data}`)

      // get the id data to the dropdwown menu
      data.names.forEach(function(name) {
          dropdown.append("option").text(name).property("value");
      });

      // call the functions to display the data and the plots to the page
      getPlot(data.names[0]);
      getInfo(data.names[0]);
  });
}

init();