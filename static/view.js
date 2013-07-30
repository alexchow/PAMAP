;
(function (window, $, r) {
    r = {
        /** Initializes the view of the entire page */
        initialize: function () {
            var url = window.location.href;
            console.log("current URL: " + url)
            url = url.replace("view", "data");
            console.log("Getting data from: " + url);
            $.getJSON(url, function (response) {
                console.log(response);
                $.each(response, function (index, feature) {
                    r.renderFeature(feature['feature_name'], feature['data'], feature['plot_type']);
                });
            });
        },

        renderFeature: function (feature_name, data, plot_type) {
            plot_type = plot_type || "lineChart";
            nv.addGraph(function () {
                var chart = nv.models[plot_type]()
                    // .showDistX(true)
                    // .showDistY(true)
                    .color(d3.scale.category10().range());

                if (plot_type === "scatterChart") {
                    chart.showDistX(true).showDistY(true)
                }

                chart.xAxis.tickFormat(d3.format('.02f'))
                chart.yAxis.tickFormat(d3.format('.02f'))

                var newElem = $('<div>' +
                    '<h2 class="featureName">' + feature_name +'</h2>' +
                    '<svg style="height:500px"></svg>' +
                    '</div>').appendTo('body');

                d3.select(newElem.find('svg').get(0))
                    .datum(data)
                    .transition().duration(500)
                    .call(chart);

                nv.utils.windowResize(chart.update);

                return chart;
            });
        }
    };
    window.viewRenderer = r;
}(window, jQuery));

viewRenderer.initialize();
