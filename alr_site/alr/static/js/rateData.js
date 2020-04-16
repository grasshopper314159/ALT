function toggle_rate(id) {
  console.log("Rate_"+id);

  if (document.getElementById('ratingContainer').classList.contains('hide')) {
    document.getElementById('ratingContainer').classList.toggle('hide');
    rate = document.getElementById(('Rate_' + id))
    rate.classList.toggle('hide')
  }

}

function add_rating(id) {
  for (i = 1; i <= 7; i++) {
    if (document.getElementById('radio_'+id+'_'+i).checked) {
      document.getElementById('score_'+id).innerHTML = document.getElementById('radio_'+id+'_'+i).value;
      //document.getElementById('submit_check_'+id).value = document.getElementById('radio_'+id+'_'+i).value;
      //document.getElementById('submit_check_'+id).checked = true;
    }
  }
}
