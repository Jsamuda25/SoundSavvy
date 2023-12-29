import React, {useState, useEffect} from 'react';
import {TextField, Button} from '@material-ui/core';
function Form(){

    const [id, setId] = useState("");
    const [songs, setSongs] = useState([]);

    const changeId = (e) => {
        setId(e.target.value);
    }


    const handleSubmit = async(e) => {
        e.preventDefault();
        console.log(id);
        
     
        const idRes = await fetch("http://localhost:5000/playlist_id?id="+ id, {
            method: "GET",
            mode:"no-cors",
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin" : "*", 
                "Access-Control-Allow-Credentials" : true 
            }
         });

         const idData = await idRes.json();
        console.log(idData);
    }


    return(
    <>
        <div>
            <form className="id-form" onSubmit={handleSubmit}>
                <TextField id="id-input"
                    label="Playlist ID"
                    placeholder="Enter Spotify Playlist ID"
                    required
                    variant = "outlined"
                    onChange={changeId}
                />
                <Button  variant="contained" id="id-button" type="submit">Go</Button>

            </form>
            
        </div> 
    </>
    )

}
export default Form;