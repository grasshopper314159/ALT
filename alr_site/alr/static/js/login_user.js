// $(document).ready(function(){
//   $.ajax(
//     {
//       type: 'POST',
//       url: '/ajax/login_user/',
//
//       success: function(response)
//       {
//         alert("AJAX Succeded!");
//       },
//
//       failure: function()
//       {
//         alert("AJAX FAILED!");
//       }
//     }
//   );
// });
$("login_user").ajaxSubmit({url: '/ajax/loginUser', type: 'POST'})
