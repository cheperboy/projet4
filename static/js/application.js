$(function() {
    $('#buttonSetSystem').click(function() {
        console.log('in progress');
        $.ajax({
            url: '/SetSystem',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log('succes');
                console.log(response);
                setTimeout(function(){location.reload();}, 1000); 
            },
            error: function(error) {
                console.log('error');
                console.log(error);s
            }
        });
    });
});


