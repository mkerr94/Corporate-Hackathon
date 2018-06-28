var shown = false;

$(document).ready(function(){
    $(".show-button").click(function() {
        if (!shown) {
            $(".categories").css({"max-width": "200px", "height": "101%"});
            $(".show-button").css("background-image", "url('../static/images/chevron-right.svg'");
        }
        else {
            $(".categories").css({"max-width": "", "height": ""});
            $(".show-button").css("background-image", "");
        }
        shown = !shown;
    })
});