     
//           let perform_button = document.querySelector("#perform_order");
//           perform_button.innerHTML = "adssad";
// perform_button.addEventListener("click",function(){
//     let kilometr = document.querySelector("#dataforkilo").value;
//     let orig = document.querySelector("#orig").value;
//     let dest = document.querySelector("#dest").value;
//     let obj = {
//         kilometr:kilometr,
//         orig:orig,
//         dest:dest
//     }
//     var token = '{%csrf_token%}';
//    $.ajax({
//        url: "post/order/",
//        type: 'post',
//        dataType: 'json',
//        headers:{
//         "X-CSRFToken":token
//        },
//        contentType: "application/json",
//        data: JSON.stringify(obj),
//        success:function(data)
//        {
//         window.location.href="kalkul"
//        }
//      });
// });
function initMap() {
            var map = new google.maps.Map(document.getElementById('map'), {
                mapTypeControl: false,
                center: {
                    lat: 43.245,
                    lng: 76.837
                },
                zoom: 11
            });

            new AutocompleteDirectionsHandler(map);
        }

        /**
         * @constructor
         */
        function AutocompleteDirectionsHandler(map) {
            this.map = map;
            this.originPlaceId = null;
            this.destinationPlaceId = null;
            this.travelMode = 'WALKING';
            this.directionsService = new google.maps.DirectionsService;
            this.directionsRenderer = new google.maps.DirectionsRenderer;
            this.directionsRenderer.setMap(map);

            var originInput = document.getElementById('origin-input');
            var destinationInput = document.getElementById('destination-input');
            var modeSelector = document.getElementById('mode-selector');

            var originAutocomplete = new google.maps.places.Autocomplete(originInput);
            // Specify just the place data fields that you need.
            originAutocomplete.setFields(['place_id']);
            originAutocomplete.setComponentRestrictions({'country': ['kz']});


      
            var destinationAutocomplete =
                new google.maps.places.Autocomplete(destinationInput);
            // Specify just the place data fields that you need.
            destinationAutocomplete.setFields(['place_id']);
            destinationAutocomplete.setComponentRestrictions({'country': ['kz']}); 
            this.setupClickListener('changemode-walking', 'WALKING');
            this.setupClickListener('changemode-transit', 'TRANSIT');
            this.setupClickListener('changemode-driving', 'DRIVING');

            this.setupPlaceChangedListener(originAutocomplete, 'ORIG');
            this.setupPlaceChangedListener(destinationAutocomplete, 'DEST');

            // this.map.controls[google.maps.ControlPosition.TOP_LEFT].push(originInput);
            // this.map.controls[google.maps.ControlPosition.TOP_RIGHT].push(
            //     destinationInput);
            this.map.controls[google.maps.ControlPosition.TOP_LEFT].push(modeSelector);

        }

        // Sets a listener on a radio button to change the filter type on Places
        // Autocomplete.
        AutocompleteDirectionsHandler.prototype.setupClickListener = function(
            id, mode) {
            var radioButton = document.getElementById(id);
            var me = this;

            radioButton.addEventListener('click', function() {
                me.travelMode = mode;
                me.route();
            });
        };

        AutocompleteDirectionsHandler.prototype.setupPlaceChangedListener = function(
            autocomplete, mode) {
            var me = this;
            autocomplete.bindTo('bounds', this.map);

            autocomplete.addListener('place_changed', function() {
                var place = autocomplete.getPlace();

                if (!place.place_id) {
                    window.alert('Please select an option from the dropdown list.');
                    return;
                }
                if (mode === 'ORIG') {
                    me.originPlaceId = place.place_id;
                } else {
                    me.destinationPlaceId = place.place_id;
                }
                me.route();
            });
        };

        AutocompleteDirectionsHandler.prototype.route = function() {
            if (!this.originPlaceId || !this.destinationPlaceId) {
                return;
            }
            var me = this;
            console.log(this.originPlaceId);
            this.directionsService.route({
                    origin: {
                        'placeId': this.originPlaceId
                    },
                    destination: {
                        'placeId': this.destinationPlaceId
                    },
                    travelMode: this.travelMode
                },
                function(response, status) {
                    if (status === 'OK') {
                        me.directionsRenderer.setDirections(response);
                        let myinput = document.getElementById("distance");
                        myinput.value = response.routes[0].legs[0].distance.text;
                        alert(response.routes[0].legs[0].distance.text);
                        var orig_old= document.getElementById('origin-input');
                        var dest_old= document.getElementById('destination-input');
                        var orig_new= document.getElementById('from');
                        var dest_new= document.getElementById('to');
                        orig_new.value=orig_old.value;
                        dest_new.value=dest_old.value;

                    } else {
                        window.alert('Directions request failed due to ' + status);
                    }
                });

        };



function fun1() {
    var sel=document.getElementById('money').selectedIndex;
    var options=document.getElementById('money').options;
    alert('Выбрана опция '+options[sel].text);
    document.getElementById('summa').style.display = 'block';
}





$(document).ready(function() {
    $('.myLinkModal').click( function(event){
        event.preventDefault();
        $('#myOverlay').fadeIn(297, function(){
      $('#myModal') 
      .css('display', 'block')
      .animate({opacity: 1}, 198);
        });
    });

    $('#myModal__close, #myOverlay').click( function(){
        $('#myModal').animate({opacity: 0}, 198,
      function(){
        $(this).css('display', 'none');
        $('#myOverlay').fadeOut(297);
        });
    });

    $('.icon').on("click", function(){
    $(this).closest('.menu').toggleClass('menu-open');
  });
});