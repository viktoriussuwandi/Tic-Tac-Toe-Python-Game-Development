function get_level() {
  $('.menu-level .item-level').on('click', function() {

    //Get selected item value
    $('.item-level').val($(this).text());
    let txt = ($(this).text());

    let request = new XMLHttpRequest()
    request.open("POST", `/update_level/${JSON.stringify(txt)}`)
    request.send()
    
    //Change button value of dropdown as selected
    $(".level-btn").text($(this).text());
    $(".level-btn").val($(this).text());
  });

}
