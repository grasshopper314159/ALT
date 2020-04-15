$(document).ready(function(){
  $.ajax(
    {
      type: 'GET',
      url: '/ajax/getAllAudioTrims/',

      success: function(response)
      {
        // ViewAudio.html table body has id='data'
        data = document.getElementById('data');

        for (var key in response) {
          if (response[key]['score'] == null) {
            response[key]['score'] = 'N/A';
          }
          if (response[key]['date'] == null) {
            response[key]['date'] = 'N/A';
          }

          entry = '<tr><td>' +
            '<div class="w3-bar">' +
            '<button class="w3-button w3-tiny w3-white w3-border w3-round" onclick="getAudio(' + response[key]['big_audio_id'] + ')">Edit</button>'+
            '<button class="w3-button w3-tiny w3-white w3-border w3-round">Del</button>'+
            '</div></td>' +
            '<td>' + response[key]['owner'] + '</td>' +
            '<td>' + response[key]['speaker'] + '</td>' +
            '<td>' + response[key]['original_text'] + '</td>' +
            '<td>' + response[key]['english_text'] + '</td>' +
            '<td>' + response[key]['score'] + '</td>' +
            '<td>' + response[key]['date'] + '</td>' +
            '<td><button class="w3-btn w3-white w3-block w3-border w3-round" onclick="showTrimDetails(\'id\');">Show</button>' + '</td>' +
            '<td><audio controls>'+
            '<source src="' + getAudioURL(response[key]['big_audio_id']) + '"type=' + '"audio/wav"> ' +
            'Your browser does not support the audio element. </audio> ' +
            '</td></tr>';

          //   <audio controls>
          //   <source src="/media/user_24_big/arctic_a0010_UTQtWJz.wav" type="audio/wav">
  
          // Your browser does not support the audio element.
          // </audio>


          data.innerHTML += entry;
        }
        // TODO: use localStorage to save reaponse for later?
        // localStorage.setS

      },

      failure: function()
      {
        alert("AJAX FAILED!");
      }
    }
  );
});

function showTrimDetails(id) {

}
