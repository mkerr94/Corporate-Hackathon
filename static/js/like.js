$(document).ready(function(){
    var user = 'theUser';

    $('.post-upvote-arrow').click(function(){
        post_id = $(this).parent().attr('id');
        $.post('/vote', {'post_id':post_id, 'user_id':user, 'vote_type':1})
    })

    $('.post-downvote-arrow').click(function(){
        post_id = $(this).parent().attr('id');
        $.post('/vote', {'post_id':post_id, 'user_id':user, 'vote_type':0})
    })
})