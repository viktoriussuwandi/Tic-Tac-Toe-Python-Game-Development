// ----------------------------------------------------------------------------
// Game Level - Function to select level
// ----------------------------------------------------------------------------

$(document).ready(function () {
  $('.game-level .menu-level .item-level').one('click', function (e) {
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
    request.open("POST", `/update_role/${JSON.stringify(role_selected)}`, false);
    request.send();
    
    //3.Disabled O button
    $(".btn-role-O").addClass('disabled');
    
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
    request.open("POST", `/update_role/${JSON.stringify(role_selected)}`, false);
    request.send();
    
    //3.Disabled O button
    $(".btn-role-X").addClass('disabled');
    
  });
});

// ----------------------------------------------------------------------------
// Game Board
// ----------------------------------------------------------------------------
$(document).ready(function () {
  $('.game-board .squares .square').one('click', function (e) {
    e.preventDefault();
    
    //1.Get selected html item value
    cell = $(this).text().trim()
    // cell = $(this).text().replace(/^\s+|\s+$/gm,'')
    console.log(cell)

    //2.Send variable to flask function
    let request = new XMLHttpRequest();
    request.open("POST", `/update_cells/${cell}`, false);
    request.send()
    
    //3.Change html button value of square cell, and make the square cell disable    
    $(this).addClass('disabled');
    
  });
});

// function cells(row_selected, col_selected) {
//   $('.game-board .square').on('click', function() {
//     //1.Get selected html item value
//     row = row_selected
//     col = col_selected
//     let cell = {'row' : row, 'col' : col}

//     //2.Send variable to flask function
//     let request = new XMLHttpRequest();
//     request.open("POST", `/update_cells/${JSON.stringify(cell.row)}/${JSON.stringify(cell.col)}`, false);
//     request.send()
    
//     //3.Change html button value of square cell, and make the square cell disable    
//     $(this).addClass('disabled');
//   })
// }
