function toggleAudio() {
  var audio = document.getElementById("tag-audio");
  if (audio.paused) {
    audio.play();
    document.querySelector(".audio-button").innerText = "Pause Audio";
  } else {
    audio.pause();
    document.querySelector(".audio-button").innerText = "Play Audio";
  }
}
