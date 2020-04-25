$(document).ready(function() {
  var percent = restore() || 100;
  
  //Increase the font size when "+" is clicked
  $(".increase").click(function() {
    percent += 10;
    setFontSize(percent);
  });
  
  //Decrease font size when "-" is clicked
  $(".decrease").click(function() {
    percent -= 10;
    setFontSize(percent);
  });
  
  function save(percent) {
    sessionStorage.setItem('fontSize', percent);
  }

  function restore() {
    percent = parseInt(sessionStorage.getItem('fontSize'));
    setFontSize(percent);
    return percent;
  }

function setFontSize(percent) {
    $('body').css('fontSize', percent + '%');
    save(percent);
  }
  
});