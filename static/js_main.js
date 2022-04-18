var txt = document.querySelector('p');
var btn_pekin = document.getElementsByName("pekin") ; 
var btn_both = document.getElementsByName("both") ;
var btn_tokyo = document.getElementsByName("tokyo") ;
var btn_display = document.getElementById("display")
var input_medals = document.getElementById("medals")
var input_countries = document.getElementById("countries");

//var btn = document.querySelector(('input[class^=button]'));

var btn_data = document.querySelectorAll('.button-data');

btn_data.forEach((btn, index) => {
  // conditional logic here.. access element
  btn.addEventListener('click', () => updateBtn_data(btn));
  }
); 


function updateBtn_data(btn) {
  if (btn.value == 'Tokyo 2020') {
      selected_button(btn_tokyo, [btn_pekin, btn_both])
  } else if (btn.value == 'Beijing 2022') {
      selected_button(btn_pekin, [btn_tokyo, btn_both])
  } else if (btn.value == 'Both') {
      selected_button(btn_both, [btn_pekin, btn_tokyo])
  }
}


function selected_button(btn1, list_btn){
  console.log("ok", btn1)
  btn1[0].style.color = 'white' ; 
  btn1[0].style.backgroundColor  = "rgb(13, 36, 243)"; 
  for (btn of list_btn) {
      btn[0].style.color = "rgb(70, 67, 67)";
      btn[0].style.border = "rgb(70, 67, 67)";
      btn[0].style.backgroundColor = "rgb(128, 128, 128)";
  };
}


