$('.collapsable-sub-header').click(function(){
    $(this).nextUntil('tr.collapsable-sub-header').slideToggle(200)
    }
)