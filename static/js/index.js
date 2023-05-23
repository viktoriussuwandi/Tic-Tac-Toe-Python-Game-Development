// ----------------------------------------------------------------------------
// Game Level - Function to select level
// ----------------------------------------------------------------------------

$(document).ready(function () {
  $('.game-level .menu-level a').one('click', function (e) {
    e.preventDefault();
    
    //1.Get selected html item value
    let level_selected= ($(this).text());

    //2.Send variable to flask function
    let request = new XMLHttpRequest();
    request.open("POST", `/update_level/${JSON.stringify(level_selected)}`, false);
    request.send();
    
    //3.Change html button value of dropdown as selected, and make the html button disable
    $(".level-btn").text($(this).text());
    $(".level-btn").val($(this).text());
    $(".level-btn").addClass('disabled');
  });

});

// ----------------------------------------------------------------------------
// Player Role - Function to select User Role
// ----------------------------------------------------------------------------

$(document).ready(function () {
  $('.game-role .btn-role-X').one('click', function (e) {
    e.preventDefault();
    
    //1.Get selected html item value
    let role_selected = $('.role-X').text();

    //2.Send variable to flask function
    let request = new XMLHttpRequest();
    request.open("POST", `/update_role/${JSON.stringify(role_selected)}`, false);
    request.send();
    
    //3.Disabled O button
    $(".btn-role-O").addClass('disabled');
    
  });
});

$(document).ready(function () {
  $('.game-role .btn-role-O').one('click', function (e) {
    e.preventDefault();
    
    //1.Get selected html item value
    let role_selected = $('.role-O').text();

    //2.Send variable to flask function
    let request = new XMLHttpRequest();
    request.open("POST", `/update_role/${JSON.stringify(role_selected)}`, false);
    request.send();
    
    //3.Disabled O button
    $(".btn-role-X").addClass('disabled');
    
  });
});

function get_role(role_selected) {
  //Send variable to flask function
//   let request = new XMLHttpRequest();
//   request.open("POST", `/update_role/${JSON.stringify(role_selected)}`, false);
//   request.send();
// }

// function set_role_X() {
//   // Get selected html item value
//   $('.game-role .btn-role-X').on('click',function() {
//     let role_selected = $('.role-X').text();
//     get_role(role_selected);
//     $(".btn-role-O").addClass('disabled');
//   });
// }

// function set_role_O() {
//   // Get selected html item value
//   $('.game-role .btn-role-O').on('click',function() {
//     let role_selected = $('.role-O').text();
//     get_role(role_selected);
//     $(".btn-role-X").addClass('disabled');
//   });
}

// ----------------------------------------------------------------------------
// Game Board
// ----------------------------------------------------------------------------

function cells(row_selected, col_selected) {
  $('.game-board .square').on('click', function() {
    //1.Get selected html item value
    row = row_selected
    col = col_selected
    let cell = {'row' : row, 'col' : col}

    //2.Send variable to flask function
    let request = new XMLHttpRequest();
    request.open("POST", `/update_cells/${JSON.stringify(cell.row)}/${JSON.stringify(cell.col)}`, false);
    request.send()
    
    //3.Change html button value of square cell, and make the square cell disable    
    $(this).addClass('disabled');
  })
}
