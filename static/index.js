modalDiv = $('#modal-Div')
$(document).on('submit','#user_data_form',function(e){
        e.preventDefault();
        $.ajax({
           type:'POST',
           url:'/analyze',
           data:$(this).serialize(),
           success:function(data){
                alert(data)
                $('#analyzed_text').modal('show');
           },
           fail: function(xhr, textStatus, errorThrown){
               alert('Failed');
            }
        });
    });