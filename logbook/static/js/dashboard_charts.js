var chart;
var graph;
var $selection;

$("#dropdown_limit").change(function(){
    $selection = $(this).val();
    // All time chart
    //e.preventDefault();
    var ajax_response = $.ajax({url:"/dashboard/get_flight_data/", type:"POST", data:{retrieve:$selection}, dataType:"json",  async:false});
    var chartData = ajax_response.responseJSON;
    chart.dataProvider = chartData;
    chart.validateData();

});

//DATA
// Async must be false, otherwise it continues and chartData is null.
var ajax_response = $.ajax({url:"/dashboard/get_flight_data/", type:"POST", dataType:"json", data:{retrieve:"30d"},  async:false});
var chartData = ajax_response.responseJSON;

AmCharts.ready(function () {

    // SERIAL CHART
    chart = new AmCharts.AmSerialChart();
    chart.pathToImages = "/static/amcharts/images/";
    chart.dataProvider = chartData;
    chart.marginLeft = 10;
    chart.categoryField = "date";
    chart.dataDateFormat = "YYYY-MM-DD";
    chart.color = "#0EABF8";
    chart.gridColor = "#0EABF8";
    chart.gridAlpha = 0;
    chart.marginBottom = 10;

    // listen for "dataUpdated" event (fired when chart is inited) and call zoomChart method when it happens
    //chart.addListener("dataUpdated", zoomChart);

    // AXES
    // category
    var categoryAxis = chart.categoryAxis;
    categoryAxis.parseDates = true; // as our data is date-based, we set parseDates to true
    categoryAxis.minPeriod = "DD";
    categoryAxis.dashLength = 3;
    categoryAxis.minorGridEnabled = true;
    categoryAxis.gridAlpha = 0.5;
    categoryAxis.minorGridAlpha = 0.07;
    categoryAxis.gridColor = "#0EABF8";
    categoryAxis.color = "#0EABF8";

    // value
    var valueAxis = new AmCharts.ValueAxis();
    valueAxis.axisAlpha = 0;
    valueAxis.inside = true;
    valueAxis.dashLength = 3;
    valueAxis.color = "#0EABF8";
    chart.addValueAxis(valueAxis);


    //  TIME
    graph = new AmCharts.AmGraph();
    //graph.type = "smoothedLine"; // this line makes the graph smoothed line.
    graph.type = "line";
    graph.lineColor = "#FD772D";
    graph.bullet = "round";
    graph.bulletSize = 5;
    graph.bulletBorderColor = "#FFFFFF";
    graph.bulletBorderAlpha = 1;
    graph.bulletBorderThickness = 1;
    graph.lineThickness = 2;
    graph.valueField = "time";
    graph.balloonText = "Last 30 days:<br><b><span style='font-size:14px;'>[[value]]hs</span></b>";

    chart.addGraph(graph);


    //  LIMIT
    graph = new AmCharts.AmGraph();
    //graph.type = "smoothedLine"; // this line makes the graph smoothed line.
    graph.type = "line";
    graph.lineColor = "#E32708";
    graph.lineThickness = 1;
    graph.valueField = "limit";
    //graph.balloonText = null;
    graph.balloonText = "30 days limit: [[value]] hs</b>";
    chart.addGraph(graph);


    // CURSOR
    var chartCursor = new AmCharts.ChartCursor();
    chartCursor.cursorAlpha = 0;
    chartCursor.cursorPosition = "mouse";
    chartCursor.categoryBalloonDateFormat = "YYYY";
    chart.addChartCursor(chartCursor);

    // SCROLLBAR
    var chartScrollbar = new AmCharts.ChartScrollbar();
    chartScrollbar.backgroundAlpha = 1;
    chartScrollbar.backgroundColor = "#808080";
    chartScrollbar.usePeriod = "DD";
    chartScrollbar.selectedBackgroundAlpha = 0.5;
    chartScrollbar.dragIconWidth = 10;
    chartScrollbar.dragIconHeight = 14;
    chartScrollbar.scrollbarHeight = 10;

    //chart.addChartScrollbar(chartScrollbar);

    chart.creditsPosition = "top-left";

    // WRITE
    chart.write("chartdiv");
});

// this method is called when chart is first inited as we listen for "dataUpdated" event
//function zoomChart() {
//    // different zoom methods can be used - zoomToIndexes, zoomToDates, zoomToCategoryValues
//    chart.zoomToDates(new Date(2015, 01), new Date(2015, 02));
//}
