cario = [30.0444, 31.2357]
Hurghada = [27.2579, 33.8116]
var map = L.map('map', {
  center: Hurghada,
  zoom: 14
});
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

var control = L.Routing.control({
  waypoints: [
    L.latLng(30.0444, 31.2357) // Default start point    
  ],
  routeWhileDragging: true
}).addTo(map);

function createButton(label, container) {
  var btn = L.DomUtil.create('button', '', container);
  btn.setAttribute('type', 'button'); btn.innerHTML = label;
  return btn;
}

function SetWayPoints(Btn, latlng, count) {
  L.DomEvent.on(Btn, 'click', function () {
    control.spliceWaypoints(count, 1, latlng);
    map.closePopup();
  });
}

function CreatPopUp(e) {
  var container = L.DomUtil.create('div');
  sourceBtn = createButton('Source', container);
  destBtn = createButton('Destination', container);

  L.popup()
    .setContent(container)
    .setLatLng(e.latlng)
    .openOn(map);
}

function getLatLng() {
  var waypoints = control.getWaypoints();
  return waypoints.map(function (waypoint) {
    return waypoint.latLng;
  });
}


function getUserLocation(map) {
  var marker = L.marker([0, 0]).addTo(map);

  map.locate({ setView: true, maxZoom: 16 });

  map.on('locationfound', function (e) {
    marker.setLatLng(e.latlng);
  });

  map.on('locationerror', function (e) {
    alert("Location access denied");
  });
}

map.on('click', function (e) {
  getUserLocation(map);
  CreatPopUp(e);
  SetWayPoints(sourceBtn, e.latlng, 0);
  SetWayPoints(destBtn, e.latlng, 1);
  var latLng = getLatLng()
  console.log(JSON.stringify(latLng));
});