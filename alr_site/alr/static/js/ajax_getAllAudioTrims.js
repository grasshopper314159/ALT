$(document).ready(function(){

  $.ajax(
    {
      type: 'GET',
      url: '/ajax/getAllAudioTrim/',

      success: function(response)
      {
        Options = document.getElementById('options');
        select = Options.innerHTML;
        for (var key in response) {
          optgroup = '<optgroup label=\"' + key + '\">';
          for (var i = 0; i < response[key].length; i++) {
            value = response[key][i];
            option = '<option value=\"' + (key+','+value) + '\">' + value + '</option>';
            optgroup += option;
          }
          optgroup += '</optgroup>';

          console.log(optgroup);
          select += optgroup;
        }
        Options.innerHTML = select;

      },

      failure: function()
      {
        alert("AJAX FAILED!");
      }
    }
  );
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
//         data = document.getElementById('data');
//         owner = 'Me';
//         speaker = 'you';
//         project = 'mine';
//         text_original = 'Hello';
//         text_english = 'Hello';
//         score = '7';
//         date = '02/07/2020';
//         console.log('HELP');
//         for (var key in response) {
//             entry = '<tr><td>' +
//               '<div class="w3-bar">' +
//               '<button class="w3-button w3-tiny w3-white w3-border w3-round">Edit</button>'+
//               '<button class="w3-button w3-tiny w3-white w3-border w3-round">Del</button>'+
//               '</div></td>' +
//               '<td>' + owner + '</td>' +
//               '<td>' + speaker + '</td>' +
//               '<td>' + project + '</td>' +
//               '<td>' + text_original + '</td>' +
//               '<td>' + text_english + '</td>' +
//               '<td>' + score + '</td>' +
//               '<td>' + date + '</td>' +
//               '<td><button class="w3-btn w3-white w3-block w3-border w3-round">Show</button>' +
//               '</td></tr>';
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
