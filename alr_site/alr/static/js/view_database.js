$(document).ready(function()
{
  $("display").click(function()
  {
    $.ajax
    ({
      type: "GET",
      url: "display.php",
      dataType: "html",
      success: function(response)
      {
        $("#responsecontainer").html(response);
      }
    });
  });
});
      