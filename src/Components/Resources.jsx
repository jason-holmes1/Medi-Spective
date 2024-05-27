import "./Resources.css";
function Resources() {
    return (
        <div className="resources">
            <h1 className="resourceTitle"> Resources</h1>
            <p className="resourceContent">Here are some resources to help you feel more comfortable with what you might be struggling with. You are not Alone!:</p>
            <ul classname ="hotlinks">
                <li>
                    <a href="https://www.nimh.nih.gov/get-involved/digital-shareables/shareable-resources-on-anxiety-disorders" target="_blank" rel="noopener noreferrer">
                        <button> Anxiety Disorders</button>
                    </a>
                </li>
                <li>
                    <a href="https://www.nimh.nih.gov/get-involved/digital-shareables/shareable-resources-on-adhd" target="_blank" rel="noopener noreferrer">
                        <button>ADHD</button>
                    </a>
                </li>
                <li>
                    <a href="https://www.nimh.nih.gov/get-involved/digital-shareables/shareable-resources-on-depression" target="_blank" rel="noopener noreferrer">
                        <button>Depressive Disorders</button>
                    </a>
                </li>
                <li>
                    <a href="https://www.nimh.nih.gov/get-involved/digital-shareables/shareable-resources-on-ptsd" target="_blank" rel="noopener noreferrer">
                        <button>Post Traumatic Stress Disorder</button>
                    </a>
                </li>
                <li>
                    <a href="https://www.nimh.nih.gov/get-involved/digital-shareables/shareable-resources-on-bipolar-disorder" target="_blank" rel="noopener noreferrer">
                        <button>Bipolar Disorder</button>
                    </a>
                </li>
            </ul>
        </div>
    );
}
export default Resources;