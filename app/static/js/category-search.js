$(document).ready(function() {
    var context = $('#cat-search').first();
    context.keypress(function(event) {
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if(keycode == '13'){
            search_text = context.val();
            $.get('/searchCategory', {keyword: search_text}, function(data) {
                catdiv = context.next();
                catdiv.empty();
                for (i = 0; i < data.categories.length; i++) {
                    category = data.categories[i];
                    catdiv.append("<label><input class='category-checkbox' type='checkbox' name='" + category.id + "'>" + category.name + "</label>");
                }
            })
        }
    })
});