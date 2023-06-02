// ----------------------------------------------------------------------------
// Game Data
// ----------------------------------------------------------------------------
let GAME_DATA    = {};
let WINNER_FOUND = false;
let GAME_IS_ON   = false;

function get_Flask_Data() {

    let deferredData = new jQuery.Deferred();
    $.ajax({
        type     : "GET",
        url      : "/get_ajax",
        dataType : "json",
        success  : function(data) { deferredData.resolve(data); },
        complete : function(xhr, textStatus) {
          // console.log("AJAX Request complete -> ", xhr, " -> ", textStatus); console.log('Data Updated') 
        }
    });
    return deferredData; // contains the passed data
};

function check_game_status() {
  /*Game is start if : game difficulties is selected, and player's role (X or O) is selected
    Game is over  if : The winner is found, or all cells are selected*/
  
  //.Get game data & update game status
  let start = GAME_DATA["game_start"], over = GAME_DATA["game_over"]
  let total_cells      = GAME_DATA["game_board"]["row"] * GAME_DATA["game_board"]["col"];
  GAME_IS_ON = ( start === true && over  === false && 
                 GAME_DATA["open_cells"] > 0 && GAME_DATA["winner_found"] == false );
  update_attr();
  check_turn();
}

function check_turn() {
  
  if(GAME_DATA["player_turn"] === GAME_DATA["game_roles"]["Comp"]) {

    //1.Avoid player click any cell -> disable all buttons
    let btn_cell =  $('.game-board .squares .square')
    btn_cell.addClass('disabled');
   
    //2.Get auto selected comp cell
    let comp_cell = GAME_DATA["comp_autoCell"]["cell"]
    let comp_cell_index = GAME_DATA["comp_autoCell"]["index"]

    //3.Choose html cell which match with auto selected comp cell
    let open_cells = $('.game-board .squares .square').map( 
      function() { return $(this); } 
    );
    let html_cell  = open_cells[comp_cell_index];

    //4.Trigger click event of the html cell
    html_cell.trigger( "click" );
  }

}

function update_attr() {
  
  //2.Update Player turn element
  let player_turn_element = $('.game-turn .player-turn');
  let text_turn_element   = $('.game-turn .text-turn');
  
  if (GAME_IS_ON) {
    player_turn_element.text(GAME_DATA["player_turn"]);
    text_turn_element.text("Turn");
  } else if (!GAME_IS_ON && GAME_DATA["winner_found"]) {
    let win_mark = GAME_DATA["game_winner"].Mark
    let win_role = GAME_DATA["game_winner"].Role
    player_turn_element.text('');
    text_turn_element.text(`Congratulations : ${win_mark} (${win_role})`);
  } else if (!GAME_IS_ON) {
    player_turn_element.text('');
    text_turn_element.text("Start game or select player");
  }

  //3.Update board cells element
  let btn_cell =  $('.game-board .squares .square')
  if      (GAME_IS_ON === false) { btn_cell.addClass('disabled'); }
  else if (GAME_IS_ON === true)  { btn_cell.removeClass('disabled'); }
  
  //4.Update game re-start button
  let btn_restart = $(".game-restart a.btn")
  if(GAME_IS_ON) {
    btn_restart.text('in game');
    btn_restart.addClass('disabled in_game');
  } else if (!GAME_IS_ON) {
    btn_restart.text('Restart Game');
    btn_restart.removeClass('disabled in_game');
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
    let level_btn = $(".game-level .level-btn")
    let item_btn  = $(this)

    $.when( update_game_data  ).done( function( data ) {
      GAME_DATA = data
      level_btn.text(item_btn.text());
      level_btn.val(item_btn.text());
      level_btn.addClass('disabled');
      check_game_status();
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
    let btnX = $(this)
    let btnO = $(".btn-role-O")

    $.when( update_game_data  ).done( function( data ) {
      GAME_DATA = data;
      btnX.addClass('disabled-color');
      btnO.addClass('disabled');
      check_game_status();
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
      GAME_DATA = data;
      btnX.addClass('disabled');
      btnO.addClass('disabled-color');
      check_game_status();
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
    request.send();

    //3.Get data, change html button value of square cell
    //  make the square cell disable
    let update_game_data = get_Flask_Data();
    let cell_btn         = $(this)

    $.when( update_game_data ).done( function( data ) {
      //a.Update cell text
      cell_btn.text(GAME_DATA["player_turn"]);
      cell_btn.addClass('disabled disable-color');

      //b.Update data & change text of player turn
      GAME_DATA = data
      check_game_status();

    });

  });
});

// ----------------------------------------------------------------------------
// Restart Game
// ----------------------------------------------------------------------------
$(document).ready(function () {
  $('.game-restart a.btn').one('click', function (e) {
    e.preventDefault();
    if(!GAME_IS_ON) {
      //Refresh the game, and reload home page
      let request = new XMLHttpRequest();
      request.open("POST", `/restart_game`, false);
      request.send();
      location.reload();
    }
    
  });
});

// ----------------------------------------------------------------------------
// OTHERS
// ----------------------------------------------------------------------------
if (GAME_IS_ON === false && GAME_DATA.length === undefined) {
  let update_game_data = get_Flask_Data();
  $.when( update_game_data ).done( function( data ) {
    GAME_DATA = data;
    check_game_status();
  });
}