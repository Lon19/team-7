import React from 'react'
import './style.css'
import * as d3 from 'd3'

class BubbleChart extends React.Component {
    componentDidMount() {
        var width = window.innerWidth*2/5;
        d3.select(".bubbleVisualisationSvg")
            .style("width", width)
            .style("height", width);
    
    var svg = d3.select("svg"),
        margin = 20,
        diameter = width,
        g = svg.append("g").attr("transform", "translate(" + diameter / 2 + "," + diameter / 2 + ")");

    var color = d3.scaleLinear()
        .domain([-1, 5])
        .range(["hsl(152,80%,80%)", "hsl(228,30%,40%)"])
        .interpolate(d3.interpolateHcl);

    var pack = d3.pack()
        .size([diameter - margin, diameter - margin])
        .padding(2);

    // d3.json("http://localhost:3000/d.json", function(error, root) {
    // if (error) throw error;
    var root = JSON.parse('{"name":"variants","children":[{"name":"Stress","children":[{"name":"Lack of wind down", "size":90}, {"name":"Overreacting", "size":70}, {"name":"Nervous energy", "size":50}, {"name":"Agitation", "size":60}, {"name":"No relaxation", "size":90}, {"name":"Feeling down", "size":50}, {"name":"Not tolerating people", "size":90}, {"name":"No physical extertion", "size":60}]},{"name":"Depression","children":[{"name":"Negative feelings", "size":70}, {"name":"No initiative", "size":60}, {"name":"Not looking forward", "size":20}, {"name":"Lack of enthusiasm", "size":30}, {"name":"No personality", "size":30}, {"name":"Touchiness", "size":40}]},{"name":"Anxiety","children":[{"name":"Dry mouth", "size":10}, {"name":"Shortness of breath", "size": 80}, {"name":"Trembling", "size":30}, {"name":"Worrying", "size":40}, {"name":"Panic", "size":20}, {"name":"Scareness", "size":70}, {"name":"No meaning in life", "size":10}]}]}');

    root = d3.hierarchy(root)
        .sum(function(d) { return d.size; })
        .sort(function(a, b) { return b.value - a.value; });

    var focus = root,
        nodes = pack(root).descendants(),
        view;

    var circle = g.selectAll("circle")
        .data(nodes)
        .enter().append("circle")
        .attr("class", function(d) { return d.parent ? d.children ? "node" : "node node--leaf" : "node node--root"; })
        .style("fill", function(d) { return d.children ? color(d.depth) : null; })
        .on("click", function(d) { if (focus !== d) return zoom(d), d3.event.stopPropagation(); });

    var text = g.selectAll("text")
        .data(nodes)
        .enter().append("text")
        .attr("class", "label")
        .style("fill-opacity", function(d) { return d.parent === root ? 1 : 0; })
        .style("font-size", "14")
        .style("font-weight", "bold")
        .style("display", function(d) { return d.parent === root ? "inline" : "none"; })
        .text(function(d) { return d.data.name; });

    var node = g.selectAll("circle,text");

    svg
        .style("background", color(-1))
        .on("click", function() { zoom(root); });

    zoomTo([root.x, root.y, root.r * 2 + margin]);

    function zoom(d) {
        var focus0 = focus; focus = d;

        var transition = d3.transition()
            .duration(d3.event.altKey ? 7500 : 750)
            .tween("zoom", function(d) {
            var i = d3.interpolateZoom(view, [focus.x, focus.y, focus.r * 2 + margin]);
            return function(t) { zoomTo(i(t)); };
            });

        transition.selectAll("text")
        .filter(function(d) { return d.parent === focus || this.style.display === "inline"; })
            .style("fill-opacity", function(d) { return d.parent === focus ? 1 : 0; })
            .on("start", function(d) { if (d.parent === focus) this.style.display = "inline"; })
            .on("end", function(d) { if (d.parent !== focus) this.style.display = "none"; });
    }

    function zoomTo(v) {
        var k = diameter / v[2]; view = v;
        node.attr("transform", function(d) { return "translate(" + (d.x - v[0]) * k + "," + (d.y - v[1]) * k + ")"; });
        circle.attr("r", function(d) { return d.r * k; });
    }
    // });
    }

    render() {
        return (
            <div class="bubbleVisualisation" align="center">
                <svg class="bubbleVisualisationSvg"></svg>
            </div>
        )
    }
}

export default BubbleChart