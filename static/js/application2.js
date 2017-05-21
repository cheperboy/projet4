$(document).ready(function() {
  $('#set_on').click(function() {
    alert( "Handler for .click() called." );  
    $.post('/system_state/on');
  });
  $('#set_off').click(function() {
    $.post('/system_state/off');
  });
});

/*$(function() {
    $('button').click(function() {
        var pass = $('#tepassword').val();
        $.ajax({
            url: '/signUpUser',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log('succes');
                console.log(response);
            },
            error: function(error) {
                console.log('error');
                console.log(error);s
            }
        });
    });
});

*/
$(function() {
    $('button').click(function() {
        console.log('in progress');
        var pass = $('#tepassword').val();
        $.ajax({
            url: '/SetSystem',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log('succes');
                console.log(response);
            },
            error: function(error) {
                console.log('error');
                console.log(error);s
            }
        });
    });
});


