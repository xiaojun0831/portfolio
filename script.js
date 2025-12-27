async function loadSpotify() {
  try {
    const res = await fetch("/api/spotify");
    const data = await res.json();

    const container = document.getElementById("spotify-status");

    if (!data.playing) {
      container.textContent = "Not playing anything right now";
      return;
    }

    container.innerHTML = `
      <img src="${data.albumArt}" width="48" height="48" />
      <div>
        <strong>${data.title}</strong><br />
        <span>${data.artist}</span>
      </div>
    `;
  } catch (err) {
    document.getElementById("spotify-status").textContent =
      "Spotify unavailable";
  }
}

loadSpotify();
setInterval(loadSpotify, 30000);
