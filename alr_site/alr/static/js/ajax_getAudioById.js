// not needed for view data
//needed for
// TODO: fix that it gets whole big_audio not just the trimmed section
// or trim the big before adding to audio controls
function getAudio(id) {
  $.ajax(
        {
            type: 'GET',
            data: {'id': id},
            url: '/ajax/getAudioFileById/',

            success: function(response)
            {
              return response;
            },

            failure: function()
            {
                alert("AJAX FAILED!");
            }
        }
    );
}
