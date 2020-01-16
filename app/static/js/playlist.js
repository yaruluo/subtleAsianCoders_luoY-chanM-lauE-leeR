var openPlaylist = function(iframe) {
    $("#playlist_slide").css("display", "initial");
    $("#playlist_slide_content").show(500);
    $("#playlist_link").prop("src", `https://open.spotify.com/embed/playlist/${iframe}`)
}

var closePlaylist = function() {
    $("#playlist_slide_content").hide(1000);
    $("#playlist_slide").css("display", "none");
}
