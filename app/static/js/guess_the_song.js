function init(songs, counter) {
    console.log(songs)
    var hasLost = false;
    $(window).on('load', () => {
        // Starting question
        loadQuestion(songs[counter], 0);
        console.log(songs[counter]);
        $("#choice-1, #choice-2, #choice-3, #choice-4").on("click", btn => {
            // If finished with final question
            if (counter >= 10) {
                $("#endscore").html(`${$("#score").text()}/10`)
                $("#game").empty();
                $("#endgame").css("display", "initial");
            }

            // Checking correct answer
            console.log("CHOSEN ANSWER:");
            console.log($(btn.target).html());

            console.log("ANSWER CHECK:");
            console.log($(btn.target).html() == `${songs[counter].title} by ${songs[counter].artist}`);
            var currScore = parseInt($("#score").text());
            if ($(btn.target).html() == `${songs[counter].title} by ${songs[counter].artist}`) {
                loadQuestion(songs[++counter], ++currScore);
            } else {
                loadQuestion(songs[++counter], currScore);
            }
            console.log(songs[counter]);
        });
    });
}

function loadQuestion(song, score) {
    $("#lyrics").html(`${song.lyrics.replace(/\n/g, "<br>")}`);

    $("#choice-1").html(`${song.choices[0].title} by ${song.choices[0].artist}`);
    $("#choice-2").html(`${song.choices[1].title} by ${song.choices[1].artist}`);
    $("#choice-3").html(`${song.choices[2].title} by ${song.choices[2].artist}`);
    $("#choice-4").html(`${song.choices[3].title} by ${song.choices[3].artist}`);

    $("#score").html(`${score}`);

    console.log(`CORRECT ANSWER: [${song.title}] by [${song.artist}]`)
}