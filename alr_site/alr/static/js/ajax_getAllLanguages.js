$(document).ready(function(){

  $.ajax(
    {
      type: 'GET',
      url: '/ajax/getAllLanguages/',

      success: function(response)
      {
        Options = document.getElementById('Languages')
        select = Options.innerHTML;
        for (var key in response) {
          language = response[key];
          option = '<option value=\"' + langauge + '\">' + language + '</option>';

          select += option;
          select += '</optgroup>';
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
