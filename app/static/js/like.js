$(document).ready(function(){
    var user = $('.web-container').attr('id');

    $('.post-upvote-arrow').click(function(){
        post_id = $(this).parent().attr('id');

        var context=this;
        $.post('/vote', {'post_id':post_id, 'user_id':user, 'vote_type':1}, function(data) {
            $(context).parent().find('.post-votes')[0].innerHTML = parseInt(data.upvotes) - parseInt(data.downvotes);
            $(context).parent().find('.post-upvote-count')[0].innerHTML = data.upvotes;
            $(context).parent().find('.post-downvote-count')[0].innerHTML = data.downvotes;
        });
    })

    $('.post-downvote-arrow').click(function(){
        post_id = $(this).parent().attr('id');

        var context=this;
        $.post('/vote', {'post_id':post_id, 'user_id':user, 'vote_type':0}, function(data) {           
            $(context).parent().find('span')[0].innerHTML = parseInt(data.upvotes) - parseInt(data.downvotes);
            $(context).parent().find('.post-upvote-count')[0].innerHTML = data.upvotes;
            $(context).parent().find('.post-downvote-count')[0].innerHTML = data.downvotes;
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