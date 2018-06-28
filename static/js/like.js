$(document).ready(function(){
    var user = 'theUser';

    $('.post-upvote-arrow').click(function(){
        $.post('/vote', {'post_id':1, 'user_id':user, 'vote_type':1})
        alert('Thanks for voting!');
    })

    $('.post-downvote-arrow').click(function(){
        $.post('/vote', {'post_id':1, 'user_id':user, 'vote_type':0})
        alert('Thanks for voting!');
    })
})