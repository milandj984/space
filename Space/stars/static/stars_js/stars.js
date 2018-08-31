// Prikazivanje forme za postovanje
function post(){
    $('#show-post-form').toggle();
    $('#post-form').toggle()
}

$('#show-post-form').click(post);
$('#hide-post').click(post);
// ------------------------------------


// Prikazivanje confirm delete
var pop_text = $(".confirm-popuptext");
$('#delete').click(function () {
    var el_width = this.offsetWidth;
    var el_height = pop_text.css('height');
    var left = this.offsetLeft;
    var top = this.offsetTop;

    pop_text.css({top: top - parseInt(el_height) - 15, left: left + el_width/2 - parseInt(pop_text.css('width'))/2});
    pop_text.toggleClass('show')
});

// Dugme "No"
$('#confirm-delete-hide').click(function () {
    pop_text.toggleClass('show')
});
// ------------------------------------


//Hidden menu
var hiddenMenu = $('.hidden-menu');
var menu = $('.menu');

hiddenMenu.click(function () {
    if (parseInt(hiddenMenu.css('right')) === 0){
       hiddenMenu.animate({right: 160}, 400);
       menu.animate({right: 0}, 400);
    }
    else {
        hiddenMenu.animate({right: 0}, 400);
        menu.animate({right: -160}, 400);
    }
});
//-------------------------------------