$(document).ready(function(){
    var user = 'theUser';

    $('.post-upvote-arrow').click(function(){
        post_id = $(this).parent().attr('id');

        $(this).parent().find('span')[0].innerHTML = parseInt($(this).parent().find('span')[0].innerHTML) + 1;

        $.post('/vote', {'post_id':post_id, 'user_id':user, 'vote_type':1})
    })

    $('.post-downvote-arrow').click(function(){
        post_id = $(this).parent().attr('id');

        // Display the comments form
        comment_form_id = 'comment_form_'+post_id;
        $(this).parent().find('form')[0].style.visibility = 'visible';

        $(this).parent().find('span')[0].innerHTML = parseInt($(this).parent().find('span')[0].innerHTML) - 1;

        $.post('/vote', {'post_id':post_id, 'user_id':user, 'vote_type':0})
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