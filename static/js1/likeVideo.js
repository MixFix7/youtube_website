$('.like-btn').click(function() {
    var video_id = $(this).data('video-id');

    $.get('/like_video/', {'video_id': video_id}, function(data) {
        if (data.status == 'ok') {
            $('#video-' + video_id + '-likes').text(data.likes);
        }
    });
});
