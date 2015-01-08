$(".datetimepicker").datetimepicker({
    format:'Y-m-d H:i',
    mask:true
});

$('#add_more').click(function() {
    cloneMore('.flight-legs table tr:last', 'flightleg_set');

    $(".datetimepicker").datetimepicker({
    format:'Y-m-d H:i',
    mask:true
    });

});

$('#remove_row').click(function() {
    unClone('.flight-legs table tr:last', 'flightleg_set');
});

function cloneMore(selector, type) {
    var newElement = $(selector).clone();
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });
    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
}

function unClone(selector, type) {
    //var newElement = $(selector).clone();
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    if (total > 1) {
        $(selector).remove();
        total--;
        $('#id_' + type + '-TOTAL_FORMS').val(total);
    }
}