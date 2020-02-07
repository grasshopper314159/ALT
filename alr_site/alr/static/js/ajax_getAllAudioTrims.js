$(document).ready(function(){

  $.ajax(
    {
      type: 'GET',
      url: '/ajax/getAllAudioTrim/',

      success: function(response)
      {
        data = document.getElementById('data');
        owner = 'Me';
        speaker = 'you';
        project = 'mine';
        text_original = 'Hello';
        text_english = 'Hello';
        score = '7';
        date = '02/07/2020';
        console.log('HELP');
        for (var key in response) {
            entry = '<tr><td>' +
              '<div class="w3-bar">' +
              '<button class="w3-button w3-tiny w3-white w3-border w3-round">Edit</button>'+
              '<button class="w3-button w3-tiny w3-white w3-border w3-round">Del</button>'+
              '</div></td>' +
              '<td>' + owner + '</td>' +
              '<td>' + speaker + '</td>' +
              '<td>' + project + '</td>' +
              '<td>' + text_original + '</td>' +
              '<td>' + text_english + '</td>' +
              '<td>' + score + '</td>' +
              '<td>' + date + '</td>' +
              '<td><button class="w3-btn w3-white w3-block w3-border w3-round">Show</button>' +
              '</td></tr>';
      },

      failure: function()
      {
        alert("AJAX FAILED!");
      }
    }
  );
  console.log("FUCK")
});


// $(document).ready(function(){
//   $.ajax(
//     {
//       type: 'GET',
//       url: '/ajax/getAllAudioTrim/',
//
//       success: function(response)
//       {
//         alert('success')
//             data.innerHTML += entry;
//       },
//
//       failure: function()
//       {
//         console.log('HELP')
//         alert("AJAX FAILED!");
//       }
//     }
//   );
// });
