function init(songs, counter) {
  var hasLost = false;
  $(document).ready(() => {
    var nextPageIndex = parseInt($("#higher-btn").attr("next-page"));
    // console.log(counter);
    loadGame(songs, counter, 0);
    $("#higher-btn, #lower-btn").on("click", btn => {
      var leftSongPopularity = parseInt($("#left-song-popularity").text());
      var rightSongPopularity = parseInt($("#right-song-popularity").text());
      if (counter >= 8) $(".container").hide(); // finished all 10 questions
      // scorekeeping
      if (
        (leftSongPopularity <= rightSongPopularity && // right choice
          $(btn.target).html() == "Higher") ||
        (leftSongPopularity >= rightSongPopularity &&
          $(btn.target).html() == "Lower")
      ) {
        curScore = parseInt($("#score").text());
        $(btn.target).attr("next-page", ++counter);
        loadGame(songs, counter, ++curScore);
      } else { // wrong choice
        $("#higher-lower").empty()
        // Implement end game screen
      }
    });
  });
}

function loadGame(songs, counter, score) {
  $("#left-image").prop("src", songs[counter]["coverArtLink"])

  console.log(songs[counter]["title"])

  $("#left-song-iframe").prop("src", songs[counter]["iframe"]);
  $("#left-song-title").html(songs[counter]["title"]);
  $("#left-song-artist").html(songs[counter]["artist"]);
  $("#left-song-popularity").html(songs[counter]["popularity"]);

  $("#right-image").prop("src", songs[counter + 1]["coverArtLink"])

  $("#right-song-iframe").prop("src", songs[counter + 1]["iframe"]);
  $("#right-song-title").html(songs[counter + 1]["title"]);
  $("#right-song-artist").html(songs[counter + 1]["artist"]);
  $("#right-song-popularity").html(songs[counter + 1]["popularity"]);
  $("#score").html(score);
}
