function s(e) {
    return document.querySelector(e);
}

// persist scrolling position
document.addEventListener("DOMContentLoaded", function(event) {
  var scrollpos = localStorage.getItem("scrollpos");
  if (scrollpos) window.scrollTo(0, scrollpos);
});

window.onbeforeunload = function(e) {
  localStorage.setItem("scrollpos", window.scrollY);
};
