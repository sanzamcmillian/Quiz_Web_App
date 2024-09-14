import React, { useState } from 'react';

const Feedback = () => {
  const [feedback, setFeedback] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Feedback submitted:', feedback);
    setSubmitted(true);
  };

  return (
    <div className="container">
      <h2>Feedback</h2>
      {submitted ? (
        <p>Thank you for your feedback!</p>
      ) : (
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label htmlFor="feedback" className="form-label">Your Feedback</label>
            <textarea className="form-control" id="feedback" rows="5" value={feedback} onChange={(e) => setFeedback(e.target.value)} required></textarea>
          </div>
          <button type="submit" className="btn btn-primary">Submit Feedback</button>
        </form>
      )}
    </div>
  );
};

export default Feedback;
