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

  if (audio.paused) {
    audio.play();
  } else {
    audio.pause();
  }
}

function copyToClipboard(text) {
  navigator.clipboard
    .writeText(text)
    .then(() => {
      showPopup();
    })
    .catch((err) => {
      console.error("Could not copy text: ", err);
    });
}

function showPopup() {
  var popup = document.getElementById("popup");
  popup.style.display = "block";
  setTimeout(function () {
    hidePopup();
  }, 1000);
}

function hidePopup() {
  var popup = document.getElementById("popup");
  popup.style.animation = "slideOut 0.5s forwards";
  setTimeout(function () {
    popup.style.display = "none";
    popup.style.animation = "";
  }, 500);
}
