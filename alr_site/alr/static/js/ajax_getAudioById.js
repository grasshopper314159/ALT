function getAudio(id) {
    $.ajax(
        {
            type: 'POST',
            data: {'id': id},
            url: '/ajax/getAudioByID/',

            success: function(response)
            {

            },

            failure: function()
            {
                alert("AJAX FAILED!");
            }
        }
    );

}
