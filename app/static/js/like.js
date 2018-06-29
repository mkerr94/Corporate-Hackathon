$(document).ready(function(){
    var user = 'theUser';

    $('.post-upvote-arrow').click(function(){
        post_id = $(this).parent().attr('id');

        var context=this;
        $.post('/vote', {'post_id':post_id, 'user_id':user, 'vote_type':1}, function(data) {
            $(context).parent().find('span')[0].innerHTML = parseInt($(context).parent().find('span')[0].innerHTML) + data.result + " votes";
        });
    })

    $('.post-downvote-arrow').click(function(){
        post_id = $(this).parent().attr('id');

        var context=this;
        $.post('/vote', {'post_id':post_id, 'user_id':user, 'vote_type':0}, function(data) {
            $(context).parent().find('span')[0].innerHTML = parseInt($(context).parent().find('span')[0].innerHTML) - data.result + " votes";
        });
    })

    $('.comment-form').submit(function(event){
        event.preventDefault();

        post_id = $(this).parent().attr('id');
        var $form = $( this );
        url = $form.attr( 'action' );

        $.post('/comment', {'comment': $(this).find('input').val(), 'post_id':post_id, 'user_id':user});

        $(this)[0].style.visibility = 'hidden';
        $(this)[0].reset();
        $(this).parent().append('<p>Thanks for commenting!</p>')
    })

})