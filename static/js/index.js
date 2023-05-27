// ----------------------------------------------------------------------------
// Game Data
// ----------------------------------------------------------------------------
let GAME_DATA   = {}
let GAME_STATUS = 'end'

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

function update_game() {

  //1.Get game data & update game status
  let start = GAME_DATA["game_start"]
  let over  = GAME_DATA["game_over"]
  GAME_STATUS = ( start === true && over === false ) ? 'start' : 'end';

  //2.Update Player turn element
  let player_turn_element = $('.game-turn .player-turn');
  let text_turn_element   = $('.game-turn .text-turn');
  
  if (GAME_STATUS === "start" && GAME_DATA["player_turn"] != null) {
    player_turn_element.text(GAME_DATA["player_turn"]);
    text_turn_element.text("Turn");

//-----------------------------------------------------------------------------------------------------
//-----------------------------------------------------------------------------------------------------

    //If current turn is comp => Click the cell automatically
    console.log(`current turn : ${GAME_DATA["player_turn"].trim()}; Comp role : ${GAME_DATA["game_roles"]["Comp"].trim()}`);
    if (GAME_DATA["player_turn"].trim() === GAME_DATA["game_roles"]["Comp"].trim()) {
      console.log(`current turn : ${GAME_DATA["player_turn"].trim()}; Comp role : ${GAME_DATA["game_roles"]["Comp"].trim()}`);
      console.log(`Cell selected by comp : ${temp_data["comp_cells"]}`);
      // let temp_update_data = get_Flask_Data();
      // $.when( temp_update_data  ).done( function( temp_data ) {
      //   console.log(`Cell selected by comp : ${temp_data["comp_cells"]}`);
      // });
    }

//-----------------------------------------------------------------------------------------------------
//-----------------------------------------------------------------------------------------------------
    
  } else if (GAME_STATUS === "end") { 
    text_turn_element.text("Start game or select player");
  }

  //3.Disabled cells before starting the game
  let btn_cell =  $('.game-board .squares .square')
  if      (GAME_STATUS === "end") { btn_cell.addClass('disabled'); }
  else if (GAME_STATUS === "start"){ btn_cell.removeClass('disabled'); }

  //3.Disabled button restart game element
  let btn_restart = $(".game-restart a.btn")
  if(GAME_STATUS === "start") {
    btn_restart.addClass('in_game');
  }
  
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
    let update_game_data = get_Flask_Data();
    let level_btn     = $(".game-level .level-btn")
    let item_btn      = $(this)
    
    $.when( update_game_data  ).done( function( data ) {
      GAME_DATA = data
      
      level_btn.text(item_btn.text());
      level_btn.val(item_btn.text());
      level_btn.addClass('disabled');
      update_game()
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
    let update_game_data = get_Flask_Data();
    let btnX          = $(this)
    let btnO          = $(".btn-role-O")
    
    $.when( update_game_data  ).done( function( data ) {
      GAME_DATA = data

      btnX.addClass('disabled-color');
      btnO.addClass('disabled');
      update_game()
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
    let update_game_data = get_Flask_Data();
    let btnX          = $(".btn-role-X")
    let btnO          = $(this)
    
    $.when( update_game_data  ).done( function( data ) {
      GAME_DATA = data
      
      btnX.addClass('disabled');
      btnO.addClass('disabled-color');
      update_game()   
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
    cell_value = $(this).text().trim();
    // let turn_mark = $(this).val();
    
    //2.Send variable to flask function
    let request = new XMLHttpRequest();
    request.open("POST", `/update_cells/${cell_value}`, false);
    request.send()
    
    //3.Get data, change html button value of square cell
    //  make the square cell disable
    let update_game_data = get_Flask_Data();
    let cell_btn         = $(this)
    
    $.when( update_game_data  ).done( function( data ) {
      //a.Update cell text
      cell_btn.text(GAME_DATA["player_turn"]);
      cell_btn.addClass('disabled disable-color');
      
      //b.Update data & change text of player turn
      GAME_DATA = data
      update_game();
      if (GAME_STATUS === "end" && GAME_DATA["game_winner"]["Role"] != "") { 
          text_turn_element.text(`Winner : ${GAME_DATA["game_winner"]["Role"]}`);
      }
      
    });
    
  });
});

update_game()