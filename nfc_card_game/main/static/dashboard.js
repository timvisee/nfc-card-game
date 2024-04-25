const ctx = document.getElementById('myChart')

var base_url = "ws://"+ window.location.host + "/ws/"
const websocket = new WebSocket('ws://localhost:8000/ws/');

websocket.onopen = function(){
  console.log("COnnected!");
};

websocket.onclose = function(event) {
  if (event.wasClean){
    console.log(`Connection closed cleanly, code=${event.code}`)
  }else{
    console.log('Connection died!')
  }
}


websocket.onerror = function(error){
  console.log(`[WebSocket Error] ${error}`);
  console.log(error);
};

websocket.onmessage = function(event){
  log_message(event);
  update_table(event);
  update_chart(event);
};

function log_message(event){
  var data = JSON.parse(event.data);
  var table = document.getElementById("logtable");
  let row = table.insertRow(0);
  let c1 = row.insertCell(0);
  let c2 = row.insertCell(1);
  let c3 = row.insertCell(2);
  let c4 = row.insertCell(3);
  
  if(table.rows.length > 5){
    table.deleteRow(-1);
  }
  if(data.data.bought != null){
    c2.innerText = data.data.bought.amount + 'x ' +data.data.bought.item.name;
  }else{
    c2.innerText = "";
  };
  c1.innerText = data.data.player.name;
  c3.innerText = items_to_string(data.data.costs);
  c4.innerText= data.data.log;

};

function update_table(event){
  var data = JSON.parse(event.data)
  if(data.data.bought == null){
    var td_amount = document.getElementById(data.data.player.team +  '_' + Object.values(data.data.costs)[0].currency);
    cur_amount = parseInt(td_amount.innerText);
    cur_amount += Object.values(data.data.costs)[0].amount;
    td_amount.innerText = cur_amount;
  }
};


function update_chart(event) {
  var data = JSON.parse(event.data);
  
  if (data.data.bought == null) {
    var team_name = data.data.player.team_name;
    var index = c.data.labels.findIndex(label => label === team_name);
    var datasetIndex = c.data.datasets.findIndex(dataset => dataset.label === Object.values(data.data.costs)[0].post_name);
    
    if (datasetIndex !== -1) {
      var cur_amount = c.data.datasets[datasetIndex].data[index];
      c.data.datasets[datasetIndex].data[index] = parseInt(cur_amount) + parseInt(Object.values(data.data.costs)[0].amount);
      
      c.update();
    }
  }
};


function items_to_string(items, newline=true){
  let retstr = "";
  for(item in items){
    retstr += items[item].amount + " " + items[item].name;
    if(newline){
      retstr += '\n';
    }
  }
  return retstr;
};


function get_color_from_currency(currency) {
  if (currency === 'BLUE') return "rgba(54, 162, 235, 0.5)";
  if (currency === 'RED') return "rgba(255, 99, 132, 0.5)";
  if (currency === 'GREEN') return "rgba(130, 255, 54, 0.5)";
}

function init_bar_chart() {
  team_info.sort((a, b) => a.team.localeCompare(b.team));

  var chartData = {
    labels: [],
    datasets: []
  };

  var mineDatasets = {};

  team_info.forEach(team => {
    if(!chartData.labels.includes(team.team)){
      chartData.labels.push(team.team);
    }

    if(!mineDatasets[team.mine]){
      mineDatasets[team.mine] = {
        label: team.mine,
        backgroundColor: get_color_from_currency(team.currency),
        data: []
      };
    }
    mineDatasets[team.mine].data.push(team.mine_amount);
  });

  Object.values(mineDatasets).forEach(dataset => {
    chartData.datasets.push(dataset);
  })

  c.data = chartData;
  console.log(chartData)
  c.update();
}


c = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: [],
    datasets: []
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
        stacked: false
      },
    }
  }
});

init_bar_chart();

//
// c = new Chart(ctx, {
//   type: 'bar',
//   data: {
//     labels: ['team1', 'team2'],
//     datasets: [{
//         label: 'mine1',
//         backgroundColor: get_color_from_currency('RED'),
//         data: [2, 4]
//       },{
//         label: 'mine2',
//         backgroundColor: get_color_from_currency('BLUE'),
//         data: [2, 4]
//       },{
//         label: 'mine3',
//         backgroundColor: get_color_from_currency('GREEN'),
//         data: [2, 4]
//       }] 
//   },
//   options: {
//     scales: {
//       y: {
//         beginAtZero: true,
//         stacked: false
//       },
//     }
//   }
// });
