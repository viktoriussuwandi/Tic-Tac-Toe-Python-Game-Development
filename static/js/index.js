// ----------------------------------------------------------------------------
// Game Data
// ----------------------------------------------------------------------------
let GAME_DATA

function get_Flask_Data() {
    let deferredData = new jQuery.Deferred();
    $.ajax({
        type     : "GET",
        url      : "/get_ajax",
        dataType : "json",
        success  : function(data) { deferredData.resolve(data); },
        complete : function(xhr, textStatus) { 
          // console.log("AJAX Request complete -> ", xhr, " -> ", textStatus);
          // console.log('Data Updated')
            }
    });

    return deferredData; // contains the passed data
};

function update_turn() {
  let checkStart = GAME_DATA["game_start"]
  let checkOver  = GAME_DATA["game_over"]
  console.log(`Start : ${checkStart} ; Over : ${checkOver}`)
}

// ----------------------------------------------------------------------------
// Game Level - Function to select level
// ----------------------------------------------------------------------------

$(document).ready(function () {
  $('.game-level .menu-level .item-level').one('click', function (e) {
    e.preventDefault();
    
    //1.Get selected html item value
    let level_selected = $(this).text().trim();
    
    //2.Send variable to flask function
    let request = new XMLHttpRequest();
    request.open("POST", `/update_level/${level_selected}`, false);
    request.send();
    
    //3.Get game data, & Change html button value of dropdown as selected, 
    //  and make the html button disable
    let get_game_data = get_Flask_Data();
    let level_btn     = $(".game-level .level-btn")
    let item_btn      = $(this)
    
    $.when( get_game_data  ).done( function( data ) {
      GAME_DATA = data
      console.log(`Level : ${GAME_DATA["game_level"]}`)
      update_turn()
      level_btn.text(item_btn.text());
      level_btn.val(item_btn.text());
      level_btn.addClass('disabled');
    });
    
  });
});

// ----------------------------------------------------------------------------
// Player Role - Function to select User Role
// ----------------------------------------------------------------------------

// ------------------------------------------------------------
// Role X
// ------------------------------------------------------------
$(document).ready(function () {
  $('.game-role .btn-role-X').one('click', function (e) {
    e.preventDefault();
    
    //1.Get selected html item value
    let role_selected = $('.role-X').text();

    //2.Send variable to flask function
    let request = new XMLHttpRequest();
    request.open("POST", `/update_role/${role_selected}`, false);
    request.send();
    
    //3.Get data, & disabled O button
    let get_game_data = get_Flask_Data();
    let btnX          = $(this)
    let btnO          = $(".btn-role-O")
    
    $.when( get_game_data  ).done( function( data ) {
      GAME_DATA = data
      console.log(`Roles : ${JSON.stringify(GAME_DATA["game_roles"])}`)
      update_turn()
      btnX.addClass('disabled-color');
      btnO.addClass('disabled');
    });
    
  });
});

// ------------------------------------------------------------
// Role O
// ------------------------------------------------------------
$(document).ready(function () {
  $('.game-role .btn-role-O').one('click', function (e) {
    e.preventDefault();
    
    //1.Get selected html item value
    let role_selected = $('.role-O').text();

    //2.Send variable to flask function
    let request = new XMLHttpRequest();
    request.open("POST", `/update_role/${role_selected}`, false);
    request.send();
    
    //3.Get data, & disabled X button
    let get_game_data = get_Flask_Data();
    let btnX          = $(".btn-role-X")
    let btnO          = $(this)
    
    $.when( get_game_data  ).done( function( data ) {
      GAME_DATA = data
      console.log(`Roles : ${GAME_DATA["game_roles"]}`)
      update_turn()
      btnX.addClass('disabled');
      btnO.addClass('disabled-color');
    });
    
  });
});

// ----------------------------------------------------------------------------
// Game Board
// ----------------------------------------------------------------------------
$(document).ready(function () {
  $('.game-board .squares .square').one('click', function (e) {
    e.preventDefault();
    
    //1.Get selected html item value
    cell = $(this).text().trim();
    // let turn_mark = $(this).val();
    
    //2.Send variable to flask function
    let request = new XMLHttpRequest();
    request.open("POST", `/update_cells/${cell}`, false);
    request.send()
    
    //3.Get data, change html button value of square cell
    //  make the square cell disable
    let get_game_data = get_Flask_Data();
    let btn           = $(this)
    
    $.when( get_game_data  ).done( function( data ) {
      GAME_DATA = data
      console.log(`Turn : ${GAME_DATA["player_turn"]}`)
      update_turn()
      btn.addClass('disabled');
    });
    
  });
});