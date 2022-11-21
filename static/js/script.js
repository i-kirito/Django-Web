const container = document.getElementsByClassName("container")[0];
const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");

signUpBtn.addEventListener("click", () => {
    container.classList.add("right_panel_active");
});

signInBtn.addEventListener("click", () => {
    container.classList.remove("right_panel_active");
});

function login() {}

function sign() {}