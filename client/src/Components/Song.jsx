import React from 'react'

const Song = ({song}) => {
  return (
    <div>
        <h1>Song title: {song.song}</h1>
        <h4>Artist: {song.artist}</h4>
        <h4>Album: {song.album}</h4>
        <img src={song.image} alt="song image" />
    </div>
  )
}

export default Song