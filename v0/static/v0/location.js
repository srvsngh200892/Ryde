function getLocation(){
	if(navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(showPosition);
		
	}
}
function showPosition(position)	{
 	var latlong = position.coords.latitude +','+ position.coords.longitude;
	
	var img_url = "http://maps.googleapis.com/maps/api/staticmap?center=
    "+latlong+"&zoom=14&size=400x300&sensor=false";
	$(".map").html("<img src='"+img_url+"'>");
}
$(document).on('ready', function() {
	getLocation();
});
