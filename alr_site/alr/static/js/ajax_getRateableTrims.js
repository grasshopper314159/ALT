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

          // entry = '<tr id="0">' +
          //   '<td>""</td>'
          //   <td></td>
          //   <td>Hello world</td>
          //   <td class="w3-center">7/20/20</td>
          //   <td id="score_0" class="w3-center">N/A</td>
          //   <td class="w3-center"><button class="w3-button w3-tiny w3-white w3-border w3-round" onclick="toggle_rate('0'); document.getElementById('ratingContainer').classList.toggle('hide');">Rate</button></td>
          //   <td class="w3-center"><input id="submit_check_0" class="w3-check" type="checkbox"></td>
          // </tr>

          entry = '<tr><td>' +
            '<div class="w3-bar">' +
            '<button class="w3-button w3-tiny w3-white w3-border w3-round">Edit</button>'+
            '<button class="w3-button w3-tiny w3-white w3-border w3-round">Del</button>'+
            '</div></td>' +
            '<td>' + response[key]['owner'] + '</td>' +
            '<td>' + response[key]['speaker'] + '</td>' +
            '<td>' + response[key]['original_text'] + '</td>' +
            '<td>' + response[key]['english_text'] + '</td>' +
            '<td>' + response[key]['score'] + '</td>' +
            '<td>' + response[key]['date'] + '</td>' +
            '<td><button class="w3-btn w3-white w3-block w3-border w3-round">Show</button>' +
            '</td></tr>';
          data.innerHTML += entry;
        }
      },

      failure: function()
      {
        alert("AJAX FAILED!");
      }
    }
  );
});
