// function ExecPythonCommand(pythonCommand){
//   var request = new XMLHttpRequest()
//   request.open("GET", "/" + pythonCommand, true)
//   request.send()
// }

function get_level(pythonCommand) {
  $('.dropdown-menu .dropdown-item').on('click', function(){

    //Get selected item value
    $('.dropdown-item').val($(this).text());
    let txt = ($(this).text());

    //Change button value of dropdown as selected
    $(".dropdown-toggle").text($(this).text());
    $(".dropdown-toggle").val($(this).text());

    let request = new XMLHttpRequest()
    request.open("GET", "/" + pythonCommand, true)
    request.send()
  });

}
