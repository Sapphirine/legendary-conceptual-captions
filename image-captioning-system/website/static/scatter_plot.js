function scatter_plot() {

    let margin = {top: 10, right: 30, bottom: 30, left: 60},
        width = 460 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    let svg = d3.select("#pca-googlecc-100k")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    //Read the data
    d3.csv("https://raw.githubusercontent.com/MADHAVAN001/image-captioning-system/master/website/static/pca.csv", function (data) {

        // Add X axis
        let x = d3.scaleLinear()
            .domain([-15, 15])
            .range([0, width]);
        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));

        // Add Y axis
        let y = d3.scaleLinear()
            .domain([-15, 15])
            .range([height, 0]);
        svg.append("g")
            .call(d3.axisLeft(y));

        function getRandomColor() {
            let letters = '0123456789ABCDEF';
            let color = '#';
            for (let i = 0; i < 6; i++) {
                color += letters[Math.floor(Math.random() * 16)];
            }
            return color;
        }

        let colors_list = [];

        for (let i = 0; i < 50; i++) {
            colors_list.push(getRandomColor())
        }

        // Add dots
        svg.append('g')
            .selectAll("dot")
            .data(data)
            .enter()
            .append("circle")
            .attr("cx", function (d) {
                return x(d.x);
            })
            .attr("cy", function (d) {
                return y(d.y);
            })
            .attr("r", 1.5)
            .style("fill", function (d) {
                return colors_list[d.c];
            })

    });

}

scatter_plot();