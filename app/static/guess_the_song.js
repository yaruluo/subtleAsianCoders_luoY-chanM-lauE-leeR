function init(songs, counter) {
    console.log(songs)
    var hasLost = false;
    $(document).ready(() => {
        // Starting question
        loadQuestion(songs[counter], 0);
        console.log(songs[counter])
        $("#choice-1, #choice-2, #choice-3, #choice-4").on("click", btn => {
            // If finished with final question
            if (counter >= 10) $("#content").hide();

            // Checking correct answer
            console.log($(btn.target).html());
            console.log(parseInt($("#score").text()));
            console.log($(btn.target).html() == `[${songs[counter].choices[0].title}] by [${songs[counter].choices[0].artist}]`);
            var currScore = parseInt($("#score").text());
            if ($(btn.target).html() == `[${songs[counter].choices[0].title}] by [${songs[counter].choices[0].artist}]`) {
                loadQuestion(songs[++counter], ++currScore);
            } else {
                loadQuestion(songs[++counter], currScore);
            }
        });

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

    $("#choice-1").html(`[${song.choices[0].title}] by [${song.choices[0].artist}]`);
    $("#choice-2").html(`[${song.choices[1].title}] by [${song.choices[1].artist}]`);
    $("#choice-3").html(`[${song.choices[2].title}] by [${song.choices[2].artist}]`);
    $("#choice-4").html(`[${song.choices[3].title}] by [${song.choices[3].artist}]`);

    $("#score").html(`${score}`);
}