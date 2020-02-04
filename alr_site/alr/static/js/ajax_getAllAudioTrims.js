$(document).ready(function(){

  $.ajax(
    {
      type: 'GET',
      url: '/ajax/getAllAudioTrim/',

      success: function(response)
      {
        //
        // template
        // <tr>
        //   <td>
        //     <div class="w3-bar">
        //       <button class="w3-button w3-tiny w3-white w3-border w3-round">Edit</button>
        //       <button class="w3-button w3-tiny w3-white w3-border w3-round">Del</button>
        //     </div>
        //   </td>
        //   <td>M. Miyashita</td>
        //   <td>Mike Mansfield</td>
        //   <td>Website Development</td>
        //   <td>犬</td>
        //   <td>dog</td>
        //   <td>4</td>
        //   <td>7/20/20</td>
        //   <td><button class="w3-btn w3-white w3-block w3-border w3-round">Show</button></td>
        // </tr>

        // Options = document.getElementById('options')
        // select = Options.innerHTML;
        // for (var key in response) {
        //   optgroup = '<optgroup label=\"' + key + '\">';
        //   for (var i = 0; i < response[key].length; i++) {
        //     value = response[key][i];
        //     option = '<option value=\"' + (key+','+value) + '\">' + value + '</option>';
        //     optgroup += option;
        //   }
        //   optgroup += '</optgroup>';
        //
        //   console.log(optgroup);
        //   select += optgroup;
        // }
        // Options.innerHTML = select;

      },

      failure: function()
      {
        alert("AJAX FAILED!");
      }
    }
  );
});
