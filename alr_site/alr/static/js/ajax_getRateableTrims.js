$(document).ready(function(){

  $.ajax(
    {
      type: 'GET',
      url: '/ajax/getAllAudioTrims/',

      success: function(response)
      {
        // ViewAudio.html table body has id='data'
        data = document.getElementById('data');
        rate_boxes = document.getElementById('ratingBox');

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
          // </tr>

          entry = '<tr>' +
            '<td>' + response[key]['owner'] + '</td>' +
            '<td>' + response[key]['speaker'] + '</td>' +
            '<td>' + response[key]['original_text'] + '</td>' +
            '<td>' + response[key]['english_text'] + '</td>' +
            '<td id="score_' + key + '" class="w3-center">' + response[key]['score'] + '</td>' +
            '<td>' + response[key]['date'] + '</td>' +
            '<td class="w3-center"><button class="w3-button w3-tiny w3-white w3-border w3-round" onclick="toggle_rate(' + key + ');">Rate</button>' +
            '</td></tr>';
          data.innerHTML += entry;

          rate_box =
          '<div id="Rate_' + key + '" class="hide"><h6><b class="w3-third">Speaker</b><b class="w3-third" style="float: right">Researcher</b></h6><br><h6>' +
            '<b class="w3-third">' + response[key]['speaker'] + '</b>' +
            '<b class="w3-third" style="float: right">' + response[key]['owner'] + '</b></h6><br>' +
            '<div class="" style="border: solid 1px grey; border-radius: 5px; padding: 2px; margin: 2vh;">' +
            // TODO: same problem as viewdata, this will play whole audio file
            '<audio controls><source src="' + response[key]['url'] + '" type="audio/wav">Your browser does not support the audio element.</audio>' +

            '<!-- Audio Controls --><!--Audio Controls will be here-->' +
            '</div><p class="w3-third">Not native-like</p>' +
            '<p class="w3-third">Moderately native-like</p>' +
            '<p class="w3-third">Native-like</p>' +
            '<p class="w3-third">1</p>' +
            '<p class="w3-third">4</p><p class="w3-third">7</p><div>' +
            '<div class="w3-bar"><hr class="w3-border" style="margin: 2vh;"><table id="ratings">' +
            '<thead><tr><th><b style="margin-left:2em">1</b></th><th><b style="margin-left:2em">2</b></th>' +
            '<th><b style="margin-left:2em">3</b></th><th><b style="margin-left:2em">4</b></th>' +
            '<th><b style="margin-left:2em">5</b></th><th><b style="margin-left:2em">6</b></th>' +
            '<th><b style="margin-left:2em">7</b></th></tr></thead>' +
            '<tbody class="radioButtons"><tr>' +
                '<td><input id="radio_' + key + '_1" type="radio" name="radiorating" value="1"></td>' +
                '<td><input id="radio_' + key + '_2" type="radio" name="radiorating" value="2"></td>' +
                '<td><input id="radio_' + key + '_3" type="radio" name="radiorating" value="3"></td>' +
                '<td><input id="radio_' + key + '_4" type="radio" name="radiorating" value="4"></td>' +
                '<td><input id="radio_' + key + '_5" type="radio" name="radiorating" value="5"></td>' +
                '<td><input id="radio_' + key + '_6" type="radio" name="radiorating" value="6"></td>' +
                '<td><input id="radio_' + key + '_7" type="radio" name="radiorating" value="7"></td>' +
              '</tr>' +
            '</tbody></table></div></div><div><h3>Comments</h3>' +
            // TODO: upload comments with rating
            '<textarea rows="2" cols="30" style="border: solid 1px grey; padding: 3px; width: 90%;" name="comment_' + key + '"></textarea></div>' +
            // TODO: don't use a form to upload rating use an ajax post?
            '<form class="" action="/ajax/postRating/" method="post">' +
                '<input type="submit" class="w3-btn w3-green" id="uploadButton" value="Save" onclick="add_rating(' + key + ')"></input>' +
            '</form></div>';

            rate_boxes.innerHTML += rate_box;
        }
      },

      failure: function()
      {
        alert("AJAX FAILED!");
      }
    }
  );
});
