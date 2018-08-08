$(document).ready(function(){
    $( "#target" ).click(function() {
        $.ajax({
            method: "POST",
            url: "/user",
            data: { accessToken: response.accessToken }
            })
            .done(function( msg ) {
                $("#pokemon").attr("src",msg);
            });
      });
});