function init(songs, counter) {
  var hasLost = false;
  $(document).ready(() => {
    var nextPageIndex = parseInt($("#higher-btn").attr("next-page"));
    console.log(counter);
    loadGame(songs, counter, 0);
    $("#higher-btn, #lower-btn").on("click", btn => {
      console.log(counter);
      var leftSongPopularity = JSON.parse($("#left-song-popularity").text()); // JSON used to remove double quotations on both ends of string
      var rightSongPopularity = JSON.parse($("#right-song-popularity").text());
      console.log(parseInt(leftSongPopularity));
      console.log(parseInt(rightSongPopularity)); 
      if (counter >= 8) $(".container").hide(); // finished all 10 questions
      // scorekeepin
      if (
        (leftSongPopularity <= rightSongPopularity && // right choice
          $(btn.target).html() == "Higher") ||
        (leftSongPopularity >= rightSongPopularity &&
          $(btn.target).html() == "Lower")
      ) {
        curScore = parseInt($("#score").text());
        // $(".left-half, .right-half").animate({right: '50%'});
        $(btn.target).attr("next-page", ++counter);
        loadGame(songs, counter, ++curScore);
      } else { // wrong choice
        $(".container").hide();
      }
    });
  });
}

function loadGame(songs, counter, score) {
  $(".left-half").css(
    "background",
    `linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url("${songs[counter]["coverArtLink"]}") no-repeat`
  );
  $(".left-half").css("backgroundSize", "100% 100%");
  $("#left-song-title").html(`"${songs[counter]["title"]}"`);
  $("#left-song-artist").html(`"${songs[counter]["artist"]}"`);
  $("#left-song-popularity").html(`"${songs[counter]["popularity"]}"`);
  $(".right-half").css(
    "background",
    `linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url('${
      songs[counter + 1]["coverArtLink"]
    }') no-repeat`
  );
  $(".right-half").css("backgroundSize", "100% 100%");
  $("#right-song-title").html(`"${songs[counter + 1]["title"]}"`);
  $("#right-song-artist").html(`"${songs[counter + 1]["artist"]}"`);
  $("#right-song-popularity").html(`"${songs[counter + 1]["popularity"]}"`);
  console.log(score);
  $("#score").html(`${score}`);
}
