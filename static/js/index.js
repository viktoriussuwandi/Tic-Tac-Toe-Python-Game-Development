// -------------------------------------------------------------------------------------
// Game Level
// -------------------------------------------------------------------------------------
function get_level() {
  $('.game-level .menu-level .item-level').on('click', function() {

    //1.Get selected item value
    $('.item-level').val($(this).text());
    let level_selected = ($(this).text());

    //2.Send variable to flask function
    let request = new XMLHttpRequest()
    request.open("POST", `/update_level/${JSON.stringify(level_selected)}`)
    let res = request.send()
    
    //3.Change button value of dropdown as selected, and make the button disable
    $(".level-btn").text($(this).text());
    $(".level-btn").val($(this).text());
    $(".level-btn").addClass('disabled');
    
  });

}

// -------------------------------------------------------------------------------------
// Player Role
// -------------------------------------------------------------------------------------
function get_role(role_selected) {
  console.log(role_selected)
}

function set_role_X() {
  $('.game-role .btn-role-X').on('click',function() {
    let role_selected = $('.role-X').text();
    get_role(role_selected)
    $(".btn-role-O").addClass('disabled');
  });
}

function set_role_O() {
  $('.game-role .btn-role-O').on('click',function() {
    let role_selected = $('.role-O').text();
    get_role(role_selected)
    $(".btn-role-X").addClass('disabled');
  });
  
}

// -------------------------------------------------------------------------------------
// Board cells
// -------------------------------------------------------------------------------------
