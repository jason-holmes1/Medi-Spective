import React, { useState } from 'react';
import './NewEntries.css';

function NewEntries() {
    const [formData, setFormData] = useState({
        title: ' ',
        content: ' ',
        date: "2024, 5, 29"
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleJournalSubmit = (e) => {
        e.preventDefault();
        fetch("/journal-entries", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Failed to add new journal entry');
        })
    };

    const handlePostSubmit = (e) => {
        e.preventDefault();
        fetch("/community-posts", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Failed to add new community post');
        })
    };

    return (
        <div className="new">
            <div className="content">
                <h3>Add New Journal Entries Here!</h3>
                <div className="journal-form">
                    <form onSubmit={handleJournalSubmit}>
                        <div className="form-group">
                            <label htmlFor="title">Title:</label>
                            <input type="text" id="title" name="title" value={formData.title} onChange={handleChange} autoComplete="on" />
                        </div>
                        <div className="form-group">
                            <label htmlFor="content">Content:</label>
                            <textarea id="content" name="content" value={formData.content} onChange={handleChange} autoComplete="on"></textarea>
                        </div>
                        <button type="submit">Submit</button>
                    </form>
                </div>
                <div className="post-form">
                    <h3>Add New Community Posts Here!</h3>
                    <form onSubmit={handlePostSubmit}>
                        <div className="form-group">
                            <label htmlFor="postTitle">Post Title:</label>
                            <input type="text" id="postTitle" name="postTitle" value={formData.postTitle} onChange={handleChange} autoComplete="on" />
                        </div>
                        <div className="form-group">
                            <label htmlFor="postContent">Post Content:</label>
                            <textarea id="postContent" name="postContent" value={formData.postContent} onChange={handleChange} autoComplete="on"></textarea>
                        </div>
                        <button type="submit">Submit</button>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default NewEntries;
