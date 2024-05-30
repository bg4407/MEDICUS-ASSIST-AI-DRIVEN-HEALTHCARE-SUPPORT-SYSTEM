import React from 'react';
import './Dashboard.css';

function Dashboard({ onSelectExample }) {
  const categories = {
    scheduling: [
      "Schedule an appointment for me with a dermatologist at 3 PM.",
      "Set up a meeting with my physiotherapist next Monday at 10 AM.",
      "Book a follow-up session for next week with my nutritionist."
    ],
    medicalAdvice: [
      "What are some of the most common symptoms of the flu?",
      "How can I manage chronic pain without medication?",
      "What are the early signs of diabetes?"
    ],
    medicationReminders: [
      "Remind me to take Tylenol today at 7:00 PM.",
      "Set a reminder for my daily vitamins at 8:00 AM.",
      "Alert me to take my blood pressure medication at 9:00 PM tonight."
    ]
  };

  return (
    <div className="dashboard">
      <div className="category">
        <h2>Scheduling</h2>
        {categories.scheduling.map((item, index) => (
          <button key={index} onClick={() => onSelectExample(item)} className="example-button">{item}</button>
        ))}
      </div>
      <div className="category">
        <h2>Medical Advice</h2>
        {categories.medicalAdvice.map((item, index) => (
          <button key={index} onClick={() => onSelectExample(item)} className="example-button">{item}</button>
        ))}
      </div>
      <div className="category">
        <h2>Medication Reminders</h2>
        {categories.medicationReminders.map((item, index) => (
          <button key={index} onClick={() => onSelectExample(item)} className="example-button">{item}</button>
        ))}
      </div>
    </div>
  );
}

export default Dashboard;
