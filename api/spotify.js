export default async function handler(req, res) {
  const tokenRes = await fetch("https://accounts.spotify.com/api/token", {
    method: "POST",
    headers: {
      Authorization:
        "Basic " +
        Buffer.from(
          process.env.SPOTIFY_CLIENT_ID +
            ":" +
            process.env.SPOTIFY_CLIENT_SECRET
        ).toString("base64"),
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      grant_type: "refresh_token",
      refresh_token: process.env.SPOTIFY_REFRESH_TOKEN,
    }),
  });

  const token = await tokenRes.json();

  const nowPlaying = await fetch(
    "https://api.spotify.com/v1/me/player/currently-playing",
    {
      headers: {
        Authorization: `Bearer ${token.access_token}`,
      },
    }
  );

  if (nowPlaying.status === 204) {
    return res.status(200).json({ playing: false });
  }

  const song = await nowPlaying.json();

  res.status(200).json({
    playing: true,
    title: song.item.name,
    artist: song.item.artists.map((a) => a.name).join(", "),
    albumArt: song.item.album.images[0].url,
  });
}
