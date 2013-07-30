;
(function (window, $, r) {
    r = {
        /** Initializes the view of the entire page */
        initialize: function () {
            console.log("current pathname: " + window.location.pathname)
            var url = window.location.pathname;
            url = url.replace("view", "data");
            console.log("Getting data from: " + url);
            $.getJSON(url, function (response) {
                console.log(response);
                $.each(response, function (feature_name, data) {
                    r.renderFeature(feature_name, data);
                });
            });
        },

        renderFeature: function (feature_name, data) {
            nv.addGraph(function () {
                var chart = nv.models.lineChart()
                    // .showDistX(true)
                    // .showDistY(true)
                    .color(d3.scale.category10().range());

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
        },

        getMockResult: function () {
            return [
                {
                    'key': 'Running',
                    'values': [
                        {'x': 0, 'y': 3},
                        {'x': 1, 'y': 2.5},
                        {'x': 2, 'y': 3.4},
                        {'x': 3, 'y': 7.1}
                    ]
                },
                {
                    'key': 'Walking',
                    'values': [
                        {'x': 0, 'y': 4.1},
                        {'x': 1, 'y': 3.5},
                        {'x': 2, 'y': 6.8},
                        {'x': 3, 'y': 8.2}
                    ]
                }
            ]
        }
    };
    window.viewRenderer = r;
}(window, jQuery));

viewRenderer.initialize();
