// function ExecPythonCommand(pythonCommand){
//   var request = new XMLHttpRequest()
//   request.open("GET", "/" + pythonCommand, true)
//   request.send()
// }

function get_level() {
  const dropdownElementList = document.querySelectorAll('.dropdown-toggle')
  const dropdownList = [...dropdownElementList].map(dropdownToggleEl => new bootstrap.Dropdown(dropdownToggleEl))
  let level = new bootstrap.Dropdown.getInstance(dropdownElementList)
  console.log(dropdownList)
  console.log(level)
}
