function postRating(trim_id, value, comments) {
  console.log(trim_id);
  $.ajax(
    {
      type: 'POST',
      data: {
        'trim_id':trim_id,
        'value':value,
        'comments':comments
      },
      url: '/ajax/postRating/',

      success: function() {
        alert("SUCCESS!");
      },

      failure: function()
      {
        alert("AJAX FAILED!");
      }
    }
  );
}
