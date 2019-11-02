import React from 'react'
import './style.css'
import * as d3 from 'd3'

class PieChart extends React.Component {
    componentDidMount() {
        var data = [
            {name: "Mostly agree", val: 0.7},  
            {name: "Mostly disagree", val: 0.3}
        ];
        
        var w = 500,
            h = 400,
            r = Math.min(w, h) / 2,
            labelr = r, // radius for label anchor
            color = d3.scaleOrdinal(d3.schemePastel1),
            donut = d3.pie(),
            arc = d3.arc().innerRadius(r*.6).outerRadius(r);
        
        var vis = d3.select("body")
          .append("svg:svg")
            .data([data])
            .attr("width", w)
            .attr("height", h);
        
        var arcs = vis.selectAll("g.arc")
            .data(donut.value(function(d) { return d.val }))
          .enter().append("svg:g")
            .attr("class", "arc")
            .attr("transform", "translate(" + (r + 30) + "," + r + ")");
        
        arcs.append("svg:path")
            .attr("fill", function(d, i) { return color(i); })
            .attr("d", arc);
        
        arcs.append("text")
            .attr("text-anchor", "middle")
            .attr("x", function(d) {
                var a = d.startAngle + (d.endAngle - d.startAngle)/2 - Math.PI/2;
                d.cx = Math.cos(a) * (r - 45);
                return d.x = Math.cos(a) * (r+30);
            })
            .attr("y", function(d) {
                var a = d.startAngle + (d.endAngle - d.startAngle)/2 - Math.PI/2;
                d.cy = Math.sin(a) * (r - 45);
                return d.y = Math.sin(a) * (r + 30);
            })
            .text(function(d) { return d.data.name;  })
            .each(function(d) {
                var bbox = this.getBBox();
                d.sx = d.x - bbox.width/2 - 2;
                d.ox = d.x + bbox.width/2 + 2;
                d.sy = d.oy = d.y + 5;
            });
        
            arcs.append("path")
            .attr("class", "pointer")
            .style("fill", "none")
            .style("stroke", "black")
            
            .attr("d", function(d) {
             console.log(d);
                if(d.cx > d.ox) {
                    return "M" + d.sx + "," + d.sy + "L" + d.ox + "," + d.oy + " " + d.cx + "," + d.cy;
                } else {
                    return "M" + d.ox + "," + d.oy + "L" + d.sx + "," + d.sy + " " + d.cx + "," + d.cy;
                }
            });
    }

    render() {
        return <svg></svg>;
    }
}

export default PieChart