import { useEffect, useState } from "react";
import "./JournalEntry.css";



function JournalEntry() {
    const [journalEntry, setJournalEntry] = useState([]);
    const [communityForum, setCommunityForum] = useState([]);
    //!To implement
    // const [comments, setComments] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:5555/journal-entries")
            .then(response => response.json())
            .then(data => setJournalEntry(data));
    }, []);
    useEffect(() => {
        fetch("http://127.0.0.1:5555/community-posts")
            .then(response => response.json())
            .then(data => setCommunityForum(data));
    }, []);
//!To implement
    // useEffect(() => {
    //     fetch("http://127.0.0.1:5555/comments")
    //         .then(response => response.json())
    //         .then(data => setComments(data));
    // }, []); 

    const handleDelete = id => {
        console.log("entries before deletion", journalEntry);
        fetch(`/journal-entry/${id}`, {
            method: "DELETE"
        })
            .then(() => {
                setJournalEntry(journalEntry.filter(entry => entry.id !== id));
                console.log("entries after deletion", journalEntry);
            });
    };
    const handleComDelete = id => {
        console.log("entries before deletion", journalEntry);
        fetch(`/journal-entry/${id}`, {
            method: "DELETE"
        })
            .then(() => {
                setCommunityForum(communityForum.filter(post => post.id !== id));
                console.log("entries after deletion", journalEntry);
            });
    };



    return (
        <div className="JournalEntry">
            <h1>Journal Entries</h1>
            {journalEntry.map((entry) => (
                <div key={entry.id}>
                    <h2>{entry.title}</h2>
                    <p>{entry.content}</p>
                    <p>{entry.date}</p>
                    <button onClick={() => handleDelete(entry.id)}>Delete</button>
                </div>
            ))} 
            <h1>Community Posts</h1>
            {communityForum.map((post) => (
                <div key={post.id}>
                    <h2>{post.title}</h2>
                    <p>{post.content}</p>
                    <p>{post.date}</p>
                    <button onClick={() => handleComDelete(post.id)}>Delete</button>
                </div>   
           ))}
        </div>
                    );
            }

export default JournalEntry;
