$(".datetimepicker").datetimepicker({
    format:'Y-m-d H:i',
    mask:true
});

$('#add_more').click(function() {
    clone('.flight-legs table tr:last', 'flightleg_set');
    $(".datetimepicker").datetimepicker({
    format:'Y-m-d H:i',
    mask:true
    });

});

$('#remove_row').click(function() {
    unClone('.flight-legs table tr:last', 'flightleg_set');
});
