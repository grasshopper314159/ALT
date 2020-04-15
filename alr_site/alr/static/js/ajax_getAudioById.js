function getAudio(id) {
  console.log(id);
  $.ajax(
        {
            type: 'GET',
            data: {'id': id},
            url: '/ajax/getAudioFileById/',

            success: function(response)
            {
              soundFile = new p5.soundFile(response);
              console.log(soundFile);
            },

            failure: function()
            {
                alert("AJAX FAILED!");
            }
        }
    );

}
