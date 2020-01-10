function s(e) {
    return document.querySelector(e);
}

function loadGame() {
    var buttons = document.querySelectorAll("#right-text button");
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener("click", loadAnswer)
    }
}

function loadAnswer(btn) {
    
}