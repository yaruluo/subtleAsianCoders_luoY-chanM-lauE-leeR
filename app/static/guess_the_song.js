function init(songs, counter) {
    console.log(songs)
    var hasLost = false;
    $(document).ready(() => {
        // Starting question
        loadQuestion(songs[counter], 0);
        console.log(songs[counter])
        // $("#choice-1", "#choice-2", "#choice-3", "#choice-4").on("click", btn => {
        //     // If finished with final question
        //     if (counter > 10) $("#content").hide();

        //     // Checking correct answer
        //     if ()
        // });

        // $("#higher-btn, #lower-btn").on("click", btn => {
        //     var leftSongPopularity = parseInt($("#left-song-popularity").text());
        //     var rightSongPopularity = parseInt($("#right-song-popularity").text());
        //     if (counter >= 8) $(".container").hide(); // finished all 10 questions
        //     // scorekeeping
        //     if (
        //         (leftSongPopularity <= rightSongPopularity && // right choice
        //             $(btn.target).html() == "Higher") ||
        //         (leftSongPopularity >= rightSongPopularity &&
        //             $(btn.target).html() == "Lower")
        //     ) {
        //       curScore = parseInt($("#score").text());
        //       // $(".left-half, .right-half").animate({right: '50%'});
        //       $(btn.target).attr("next-page", ++counter);
        //       loadGame(songs, counter, ++curScore);
        //     } else { // wrong choice
        //       $("#higher-lower").empty()
        //       // Implement end game screen
        //     }
        //   });
    });
}

function loadQuestion(song, score) {
    $("#lyrics").html(`${song.lyrics}`);
    
    $("#score").html(`${score}`);
}