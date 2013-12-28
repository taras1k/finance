function form_ajax(form){

  form.find('button[type=submit]').on('click', function(e){
    e.preventDefault();
    $.ajax({
      url: '#',
      method: 'POST',
      data: form.serialize(),
      success: function(data){
        window.location.replace(data);
      },
      error: function(data){
        form.find('.control-group').removeClass('error');
        form.find('.help-inline').remove();
        var errors = $.parseJSON(data.responseText);
        for(var key in errors){
          var error_inline = $('<span />').addClass('help-inline')
                                          .text(errors[key]);
          error_inline.insertAfter(form.find('#'+key));
          form.find('#'+key+'_div').addClass('error');
        };
      }
    });
  });
}
