$('.collapsable-row').click(function(){
    $(this).nextUntil('tr.collapsable-row').slideToggle(200)
    }
)

$('.drawer-menu').click(function(){
    $('.top-menu').toggleClass('toggle')
    }
)

function clone(selector, type) {
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