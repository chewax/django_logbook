$('.collapsable-row').click(function(){
    $(this).nextUntil('tr.collapsable-row').slideToggle(200)
    }
)

$('.drawer-menu').click(function(){
    $('.top-menu').toggleClass('toggle')
    }
)