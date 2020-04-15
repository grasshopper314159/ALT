function getAudio(id) {
  console.log(id);
  $.ajax(
        {
            type: 'GET',
            data: {'id': id},
            url: '/ajax/getAudioFileById/',

            success: function(response)
            {
              console.log(response);
              soundFile = new p5.soundFile(response);
            },

            failure: function()
            {
                alert("AJAX FAILED!");
            }
        }
    );

}
