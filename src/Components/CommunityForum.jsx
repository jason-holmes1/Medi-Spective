import React, { useState } from 'react';


function CommunityForum() {
    const [formData, setFormData] = useState({
        title: '',
        content: '',
        image_url: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleSubmit = (e) => {
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
        .then(newEntry => {
            console.log("New journal entry added:", newEntry);
            // Optionally, you can perform any additional actions after successful addition, such as updating state or displaying a success message
        })
        .catch(error => {
            console.error('Error adding new journal entry:', error);
            // Optionally, you can handle errors here, such as displaying an error message to the user
        });
    };

    return (
        <div className="fullscreen-bg">
            <div className="content">
                <h2>Add New Journal Entries Here!</h2>
                <div className="form-box">
                    <form onSubmit={handleSubmit}>
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
            </div>
        </div>
    );
}

export default CommunityForum;
