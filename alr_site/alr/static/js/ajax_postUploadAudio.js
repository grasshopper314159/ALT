// this is code I copied from  ajax_getAllAudioTrims, which is not a post....

$(document).ready(function(){

  $.ajax(
    {
      type: 'GET',
      url: '/ajax/getAllAudioTrim/',

      success: function(response)
      {
        data = document.getElementById('data');
        // // test data
        // owner = 'Me';
        // speaker = 'you';
        // text_original = 'Hello';
        // text_english = 'Hello';
        // score = '7';
        // date = '02/07/2020';


        for (var key in response) {
          if (response[key]['score'] == null) {
            response[key]['score'] = 'N/A';
          }
          if (response[key]['date'] == null) {
            response[key]['date'] = 'N/A';
          }

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


// $("login_user").ajaxSubmit({url: '/ajax/loginUser', type: 'POST'})

// <form class="signUpForm" action="/ajax/createUser/" onsubmit="return validatePage()" method="post">
// <button type="submit" class="w3-btn w3-green">Sign-Up</button>