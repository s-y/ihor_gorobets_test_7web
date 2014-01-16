$(document).ready(function() {
    $('#form').submit(function() {
        $.ajax({
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
            data: $(this).serialize(),
            type: 'POST',
            url: $(this).attr('action'),
            success: function(response) {
                console.log(JSON.stringify(response));
                if (response._error === false) {
                $('.panel-default').last().after(
                "<div class=\"panel panel-default\"> <div class=\"panel-heading\"> <h3 class=\"panel-title active\">" +
                response.name + "</h3> </div><div class=\"panel-body\">" + response.text +"</div></div>")
                 }
                else {
                    alert(response.__all__ , response.text, response.name)
                }
            }
        });
        return false;
    });
});

