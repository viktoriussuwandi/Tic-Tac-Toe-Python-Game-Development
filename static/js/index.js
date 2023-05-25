// ----------------------------------------------------------------------------
// GAME DATA
// ----------------------------------------------------------------------------

function getData() {

    var deferredData = new jQuery.Deferred();

    $.ajax({
        type: "GET",
        url: "/ajax",
        dataType: "json",
        success: function(data) { 
            deferredData.resolve(data);
            },
        complete: function(xhr, textStatus) {
            console.log("AJAX Request complete -> ", xhr, " -> ", textStatus);
            }
    });

    return deferredData; // contains the passed data
};

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
    
    //3.Change html button value of dropdown as selected, and make the html button disable
    $(".level-btn").text($(this).text());
    $(".level-btn").val($(this).text());
    $(".level-btn").addClass('disabled');

    let get_game_data = getData();
    $.when( get_game_data  ).done( function( game_data ) {
      console.log("The data is: " + game_data);
      console.log(game_data)
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
    
    //3.Disabled O button
    $(".btn-role-O").addClass('disabled');
    
    let get_game_data = getData();
    $.when( get_game_data  ).done( function( game_data ) {
      console.log("The data is: " + game_data);
      console.log(game_data)
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
    
    //3.Disabled O button
    $(".btn-role-X").addClass('disabled');
    
    let get_game_data = getData();
    $.when( get_game_data  ).done( function( game_data ) {
      console.log("The data is: " + game_data);
      console.log(game_data)
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
    
    //3.Change html button value of square cell, and make the square cell disable    
    $(this).addClass('disabled');
    
    let get_game_data = getData();
    $.when( get_game_data  ).done( function( game_data ) {
      console.log("The data is: " + game_data);
      console.log(game_data)
    });
    
  });
});
