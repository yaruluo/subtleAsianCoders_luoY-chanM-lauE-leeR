function init(songs, counter) { // params are meant to preserve the state of the game throughout playing; songs is the list of songs (with song title, artist, popularity rating, cover art link, etc.) and counter is the current index in the songs list that the game is on. Initially, the game is on the 0th song, so on first load, counter should equal 0.
  var curScore = 0;
  shuffle = (array) => array.sort(() => Math.random() - 0.5);
  songs = shuffle(songs);
  $(window).on('load', () => {
    // when the document is ready to be loaded, run code below
    loadGame(songs, counter, 0);
    $("#higher-btn, #lower-btn").on("click", btn => {
      $("#higher-btn, #lower-btn").hide(500);
      var leftSongPopularity = parseInt($("#left-song-popularity").text()); // get the left song popularity rating
      $("#right-song-popularity").show(250);
      setTimeout(() => {}, 2000);
      var rightSongPopularity = parseInt($("#right-song-popularity").text()); //get the right song popularity rating
      $("#right-song-popularity").hide(500);
      setTimeout(() => {}, 2000);
      if (counter >= 8) {
        $("#higher-lower").empty(); // this means the user finished all 10 questions; hide the page so they cannot play anymore.
        $("#game-message").html("You Won!");
        $("#game-score").html(`Your score: ${curScore}`);
        $("#endgame").css("display", "initial");
      }
      // scorekeeping
      if (
        (leftSongPopularity <= rightSongPopularity && // if the user chooses the 'Higher' choice and the right song is indeed higher in popularity than the left song, or if the user chooses the 'Lower' choice and the right song is indeed lower in popularity than the left song, then consider that the user picked the right choice and move on to the next question (if applicable)
          $(btn.target).html() == "Higher") ||
        (leftSongPopularity >= rightSongPopularity &&
          $(btn.target).html() == "Lower")
      ) {
        $("#higher-btn, #lower-btn").show(500);
        curScore = parseInt($("#score").text()); // gets the current score of the user
        $(btn.target).attr("next-page", ++counter); // set the counter equal to counter + 1 and then return its updated value here.
        loadGame(songs, counter, ++curScore); // song and counter is explained above; curScore (current score) is incremented and then its value is returned and loaded back into loadGame for the next question (if applicable—user did not finish all 10 questions yet)
      } else {
        // wrong choice
        $("#right-song-popularity").show(500);
        setTimeout(() => {
          $("#higher-lower").empty();
          $("#game-message").html("You Lost!");
          $("#game-score").html(`Your score: ${curScore}`);
          $("#endgame").css("display", "initial");
          $("body").css("background-image", `url("../static/img/high_low_2.jpg")`);
          $("body").css("background-size", "cover")
        }, 2000);
      }
    });
  });
}

function loadGame(songs, counter, score) { // this fxn basically updates the moving parts of the game: the left and right images, song titles, song artists, popularity ratings, etc.; this modularization allows us to call this function again and again after a button is clicked—to update the DOM each time upon an event.
  renderInfo(songs, counter, "left", 0);
  renderInfo(songs, counter, "right", 1);

  $("#score").html(`${score}`);
}

var renderInfo = function (songs, counter, side, increment) {
  $(`#${side}-image`).prop("src", songs[counter + increment]["coverArtLink"]);
  $(`#${side}-heart`).prop("href", `/save_song/${songs[counter + increment]["spotify_id"]}`);
  $(`#${side}-song-iframe`).prop("src", songs[counter + increment]["iframe"]);
  $(`#${side}-song-title`).html(songs[counter + increment]["title"]);
  $(`#${side}-song-artist`).html(songs[counter + increment]["artist"]);
  $(`#${side}-song-popularity`).html(songs[counter + increment]["popularity"]);
}

var fillHeart = function () {
  this.setAttribute("src", "../static/img/heart_full.png");
}

var emptyHeart = function () {
  this.setAttribute("src", "../static/img/heart_outline.png");
}

var addListeners = function (element) {
  element.addEventListener("mouseover", fillHeart);
  element.addEventListener("mouseout", emptyHeart);
}

addListeners(document.getElementById("left-heart").firstElementChild);
addListeners(document.getElementById("right-heart").firstElementChild);
