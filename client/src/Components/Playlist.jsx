import React, {useState} from 'react'
import Song from './Song';

const tempSongs = [{"album":"Sobadsolong","artist":"Toto Ruibal","image":"https://i.scdn.co/image/ab67616d0000b2736299edb029b311c3102e26b1","song":"Sobadsolong"},{"album":"Mira","artist":"Tom Mckeen","image":"https://i.scdn.co/image/ab67616d0000b273067cc04d388d32c57fb054fc","song":"Mira"},{"album":"Instrumentals, Vol. 9","artist":"Alx Beats","image":"https://i.scdn.co/image/ab67616d0000b2730a9bfdcaa40aab45b76d9c89","song":"Push"},{"album":"Through the Clouds","artist":"Zodiaque","image":"https://i.scdn.co/image/ab67616d0000b273554c95c738b15402931473a7","song":"Through the Clouds"},{"album":"San Melas","artist":"Leopold Kroll","image":"https://i.scdn.co/image/ab67616d0000b2732060f5e172d54855ce07acbf","song":"San Melas"},{"album":"Oysters","artist":"Jerryfish","image":"https://i.scdn.co/image/ab67616d0000b27339567a987ed3b4d88ab9f1a4","song":"Charge"},{"album":"Only Friend","artist":"Notize","image":"https://i.scdn.co/image/ab67616d0000b27346223e6f882510f331dd29a1","song":"Only Friend"},{"album":"Glide","artist":"Heretixx","image":"https://i.scdn.co/image/ab67616d0000b273515ff1ef32912a9eb83f692f","song":"Glide"},{"album":"LCSTRAX004","artist":"Ourmindz","image":"https://i.scdn.co/image/ab67616d0000b273bc68553021835e32c1bd42a4","song":"Dusty"},{"album":"Light Of Life","artist":"Shazee","image":"https://i.scdn.co/image/ab67616d0000b273258dbed729bfe97f5cc5a43e","song":"Light Of Life - Original Mix"}]

function Playlist() {

    // const [isPlaying, setPlaying] = useState(false)
    const [songs, setSongs] = useState([]);
    
    const updateSongs = () => {
        setSongs(tempSongs);
    }

    return (
        <div title='Playlist'>
            <button onClick={updateSongs} type="button">A button</button>
            <ul>
                {songs.map((s, index) => (
                    <li key={index}>
                        {/* <h1>something</h1> */}
                        <Song song={s} />
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default Playlist