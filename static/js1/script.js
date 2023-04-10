const menu = document.querySelector('#menu');
console.log(menu);
const sidebar = document.querySelector('.sidebar');
console.log(sidebar);

menu.addEventListener('click', function () {
  sidebar.classList.toggle('show-sidebar');
});

function checkPasswordMatch() {
  var password = document.getElementById("password");
  var confirmPassword = document.getElementById("confirm-password");
  var submitButton = document.getElementById("submit-button");

  if (password.value == confirmPassword.value) {
    submitButton.disabled = false;
  } else {
    submitButton.disabled = true;
  }
}