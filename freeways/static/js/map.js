$(function() {
    // start the map in downtown LA
    var map = L.map('map', {
        center: [34.038496, -118.273906],
        zoom: 9,
        minZoom: 7,
        maxZoom: 15                 
    });
    var geoJsonLayer;

    // create the map tile layer with correct attribution
    var osmUrl='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
    var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 12, attribution: osmAttrib});		

    map.addLayer(osm);
    
    // add GeoJSON shapes for the counties
    L.geoJson(counties, {
        style: {
            weight: 1,
            color: "#999",
            opacity: 0.4,
            fillColor: "#f90",
            fillOpacity: 0.2
        }
    }).addTo(map);

    $("#city_id_select").on('change', update_map);

    function update_map() {

        // call the Django API to get the routes data
        $.getJSON( "/city/" + $("#city_id_select").val(), function( data ) {

            // change the city name and statistics
            $("#city_name").html(data.name);
            $("#city_lm").html(data.lane_miles);
            var la_lane_miles = 5246;    // lane miles in LA, from http://www.fhwa.dot.gov/policyinformation/statistics/2013/hm72.cfm
            var perc = data.lane_miles / la_lane_miles * 100;
            $("#city_percent").html(perc.toFixed(1) + '%');

            // remove previous geojson layer, if any
            if (typeof geoJsonLayer != 'undefined') {
                map.removeLayer(geoJsonLayer);
            }
            // add the routes
            geoJsonLayer = L.geoJson(data.routes);
            geoJsonLayer.addTo(map);
        });   

    }
    update_map();
});
