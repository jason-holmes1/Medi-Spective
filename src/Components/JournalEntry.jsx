import { useEffect, useState } from "react";
import "./JournalEntry.css";
//Build out journal Enrty component, so that it fetches the journal entry from the backend and displays it on the page.
function JournalEntry() {
    const [journalEntry, setJournalEntry] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:5555/journal-entries")
            .then(response => response.json())
            .then(data => setJournalEntry(data));
    }, []);
const handleDelete = (id) => {
    console.log("entries before deletion", journalEntry)
    fetch(`/journal-entry/${id}`, {
        method: 'DELETE',
    })
        .then(() => {
            setJournalEntry(journalEntry.filter(entry => entry.id !== id));
            console.log("entries after deletion", journalEntry)
        });
}
  return (
    <div className="JournalEntry">
      <h1>Journal Entries</h1>
      {journalEntry.map((entry) => (
          <div key={entry.id}>
              <h2>{entry.title}</h2>
              <p>{entry.content}</p>
              <button onClick={() => handleDelete(entry.id)}>Delete</button>
          </div>
      ))}
    </div>
  );
}

export default JournalEntry;