function init(songs, counter) {
  var hasLost = false;
  $(document).ready(() => {
    var nextPageIndex = parseInt($("#higher-btn").attr('next-page'));
    console.log(counter);
    loadGame(songs, counter, 0);
    $("#higher-btn, #lower-btn").on("click", (btn) => {
        console.log(counter);
        var leftSongPopularity = parseInt($("#left-song-popularity").html());
        var rightSongPopularity = parseInt($("#right-song-popularity").html());
      if (counter < 8) {
        $(btn.target).attr('next-page', ++counter);
        loadGame(songs, counter, 0);
      }
    });
  });
}

function loadGame(songs, counter, curscore) {
    
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
  console.log(curscore);
  $("#score").html(`${curscore}`);
}

