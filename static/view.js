;(function (window, $, r) {
    r = {
        /** Initializes the view of the entire page */
        initialize : function() {
            console.log("current pathname: " + window.location.pathname)
            var url = window.location.pathname;
            url = url.replace("view", "data");
            console.log("Getting data from: " + url);
            $.getJSON(url, function(data) {
                console.log(data);
                r.renderResult(data);
            });
        },

        renderResult : function(result) {

        }
    };
    window.viewRenderer = r;
}(window, jQuery));

viewRenderer.initialize();
