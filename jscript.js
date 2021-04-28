//chart1
google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(drawChart);
function drawChart() {

    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Topping');
    data.addColumn('number', 'Slices');
    data.addRows([
        ['Mushrooms', 3],
        ['Onions', 1],
        ['Olives', 1],
        ['Zucchini', 1],
        ['Pepperoni', 2]
    ]);

    var options = {
        'title': 'How Much Pizza I Ate Last Night',
        'width': 400,
        'height': 300
    };

    var chart = new google.visualization.PieChart(document.getElementById('chart1_div'));
    chart.draw(data, options);
}


//chart2
google.charts.load('current', { packages: ['corechart', 'bar'] });
google.charts.setOnLoadCallback(drawMultSeries);

function drawMultSeries() {
    var data = new google.visualization.DataTable();
    data.addColumn('timeofday', 'Time of Day');
    data.addColumn('number', 'Motivation Level');
    data.addColumn('number', 'Energy Level');

    data.addRows([
        [{ v: [8, 0, 0], f: '8 am' }, 1, .25],
        [{ v: [9, 0, 0], f: '9 am' }, 2, .5],
        [{ v: [10, 0, 0], f: '10 am' }, 3, 1],
        [{ v: [11, 0, 0], f: '11 am' }, 4, 2.25],
        [{ v: [12, 0, 0], f: '12 pm' }, 5, 2.25],
        [{ v: [13, 0, 0], f: '1 pm' }, 6, 3],
        [{ v: [14, 0, 0], f: '2 pm' }, 7, 4],
        [{ v: [15, 0, 0], f: '3 pm' }, 8, 5.25],
        [{ v: [16, 0, 0], f: '4 pm' }, 9, 7.5],
        [{ v: [17, 0, 0], f: '5 pm' }, 10, 10],
    ]);

    var options = {
        title: 'Motivation and Energy Level Throughout the Day',
        hAxis: {
            title: 'Time of Day',
            format: 'h:mm a',
            viewWindow: {
                min: [7, 30, 0],
                max: [17, 30, 0]
            }
        },
        vAxis: {
            title: 'Rating (scale of 1-10)'
        }
    };

    var chart2 = new google.visualization.ColumnChart(
        document.getElementById('chart2_div'));

    chart2.draw(data, options);
}

//chart3
google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart2);

      function drawChart2() {
        var data = google.visualization.arrayToDataTable([
          ['Year', 'Sales', 'Expenses'],
          ['2004',  1000,      400],
          ['2005',  1170,      460],
          ['2006',  660,       1120],
          ['2007',  1030,      540]
        ]);

        var options = {
          title: 'Company Performance',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart3 = new google.visualization.LineChart(document.getElementById('curve_chart'));

        chart3.draw(data, options);
      }

//chart4
google.charts.load('current', {'packages':['line']});
      google.charts.setOnLoadCallback(drawChart4);

    function drawChart4() {

      var data = new google.visualization.DataTable();
      data.addColumn('number', 'Day');
      data.addColumn('number', 'Guardians of the Galaxy');
      data.addColumn('number', 'The Avengers');
      data.addColumn('number', 'Transformers: Age of Extinction');

      data.addRows([
        [1,  37.8, 80.8, 41.8],
        [2,  30.9, 69.5, 32.4],
        [3,  25.4,   57, 25.7],
        [4,  11.7, 18.8, 10.5],
        [5,  11.9, 17.6, 10.4],
        [6,   8.8, 13.6,  7.7],
        [7,   7.6, 12.3,  9.6],
        [8,  12.3, 29.2, 10.6],
        [9,  16.9, 42.9, 14.8],
        [10, 12.8, 30.9, 11.6],
        [11,  5.3,  7.9,  4.7],
        [12,  6.6,  8.4,  5.2],
        [13,  4.8,  6.3,  3.6],
        [14,  4.2,  6.2,  3.4]
      ]);

      var options = {
        chart: {
          title: 'Box Office Earnings in First Two Weeks of Opening',
          subtitle: 'in millions of dollars (USD)'
        },
        width: 900,
        height: 500
      };

      var chart4 = new google.charts.Line(document.getElementById('linechart_material'));

      chart4.draw(data, google.charts.Line.convertOptions(options));
    }        
