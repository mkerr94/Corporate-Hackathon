var shown = false;

$(document).ready(function(){
    $(".show-button").click(function() {
        if (!shown) {
            $(".sidebar").css({"max-width": "200px", "height": "101%"});
            $(".show-button").css("background-image", "url('../static/images/chevron-right.svg'");
            $(".filters").css({"display": "grid"});
        }
        else {
            $(".sidebar").css({"max-width": "", "height": ""});
            $(".show-button").css("background-image", "");
            $(".filters").css({"display": ""});
        }
        shown = !shown;
    })
});