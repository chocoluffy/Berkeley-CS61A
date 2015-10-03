/* Adapted from https://strongriley.github.io/d3/ex/voronoi.html */

var margins = {top: 0, right: 0, bottom: 0, left: 0},
    height = 580 - margins.top - margins.bottom,
    width =  580 - margins.left - margins.right;

var x = d3.scale.linear().range([0, width]);
var y = d3.scale.linear().range([0, height]);
var xAxis = d3.svg.axis().scale(x).orient("bottom");
var yAxis = d3.svg.axis().scale(y).orient("left");

var clusterColor = d3.scale.category10();
var fillColor = d3.scale.linear().domain([1, 5]).range(["blue", "yellow"]);
var fillOpacity = 0.3;
var hoverOpacity = 0.7;

var svg = d3.select("body").append("svg")
    .attr("width", width + margins.left + margins.right)
    .attr("height", height + margins.top + margins.bottom)
    .append("g")
    .attr("transform", "translate(" + margins.left + "," + margins.top + ")");

var tooltip = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

var makeValidID = function(s) {
    return "#" + s.replace(/[^a-zA-Z]/g, "-");
};

var updateColor = function(d, i) {
    svg.select(makeValidID(d.name))
        .style("opacity", hoverOpacity)
        .style("fill", function (d) { return clusterColor(d.cluster); });
};

var resetColor = function(d, i) {
    svg.select(makeValidID(d.name))
        .style("opacity", fillOpacity)
        .style("fill", function (d) { return fillColor(d.weight); });
};

d3.json("voronoi.json", function(data) {
    // extents of Berkeley restaurants
    x.domain([-122.272, -122.248]).nice();
    y.domain([37.88, 37.86]).nice();

    var voronoi = d3.geom.voronoi().clipExtent([[0, 0], [width, height]]);
    var polygons = voronoi(data.map(function (d) { return [x(d.y), y(d.x), d.weight]; }))
            .map(d3.geom.polygon);
    polygons.forEach(function (val, i, arr) {
        val.weight = data[i].weight;
        val.name = data[i].name;
        val.cluster = data[i].cluster;
    });

    svg.selectAll("path")
        .data(polygons)
        .enter()
        .append("path")
        .attr("class", "cell")
        .attr("id", function (d) { return makeValidID(d.name).substr(1); })
        .attr("stroke", "black")
        .style("opacity", fillOpacity)
        .style("fill", function (d) { return fillColor(d.weight); })
        .attr("d", function (d) { return "M" + d.join("L") + "Z"; })
        .on("mouseover", function (d, i) {
            updateColor(d);
        })
        .on("mousemove", function(d, i) {
            tooltip.transition()
                .duration(100)
                .style("opacity", 0.9);
            tooltip.html(d.name + " (" + Math.round(d.weight * 100) / 100 + ")")
                .style("left", (d3.event.pageX + 5) + "px")
                .style("top", (d3.event.pageY - 28) + "px");
        })
        .on("mouseout", function (d, i) {
            tooltip.transition()
                .duration(200)
                .style("opacity", 0);
            resetColor(d);
        });

    svg.selectAll(".dot")
        .data(data)
        .enter()
        .append("circle")
        .attr("class", "dot")
        .attr("r", function (d) { return 4; })
        .attr("cx", function(d) { return x(d.y); })
        .attr("cy", function(d) { return y(d.x); })
        .style("fill", function(d) { return clusterColor(d.cluster); })
        .on("mouseover", function(d) {
            tooltip.transition()
                .duration(100)
                .style("opacity", 0.9);
            tooltip.html(d.name + " (" + Math.round(d.weight * 100) / 100 + ")")
                .style("left", (d3.event.pageX + 5) + "px")
                .style("top", (d3.event.pageY - 28) + "px");
            updateColor(d);
        })
        .on("mouseout", function(d) {
            tooltip.transition()
                .duration(200)
                .style("opacity", 0);
            resetColor(d);
        });
});
