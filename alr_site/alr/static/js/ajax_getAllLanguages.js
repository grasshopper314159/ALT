$(document).ready(function(){

  $.ajax(
    {
      type: 'GET',
      url: '/ajax/getAllLanguages/',

      success: function(response)
      {
        // id of the select is Languages
        Options = document.getElementById('Languages')
        options = Options.innerHTML;
        for (var key in response) {
          options += '<option value=\"' + response[key] + '\">' + response[key] + '</option>';
        }
        Options.innerHTML = options;
      },

      failure: function()
      {
        alert("AJAX FAILED!");
      }
    }
  );
});
