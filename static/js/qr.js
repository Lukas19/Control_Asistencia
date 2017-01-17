function read(a)
{
    var form = new FormData();

    form.append('qr-value', a);

    $.ajax({
        url: '/empleados/lector',
        type: 'POST',
        data: form,
        processData: false,
        contentType: false,
        success: function (data) {
            console.log(data);
            if(!data['error']) {
                alert('Registro completo')
            }
        },
        error: function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown)
        }
    });
    $("#qr-value").text(a);
}
qrcode.callback = read;


