function showPlaying() {
  var playButton = document.getElementById("icon-button-play");
  var stopButton = document.getElementById("icon-button-stop");

  playButton.style.display = "none";
  stopButton.style.display = "inline-block";
}

function showStopped() {
  var playButton = document.getElementById("icon-button-play");
  var stopButton = document.getElementById("icon-button-stop");

  playButton.style.display = "inline-block";
  stopButton.style.display = "none";
}

function toggleAudio() {
  var audio = document.getElementById("tag-audio");

  // TODO: create a slide volume
  audio.volume = 0.5;

  if (audio.paused) {
    audio.play();
  } else {
    audio.pause();
  }
}
