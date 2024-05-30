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
    <div className="dashboard-container">
      <header className="dashboard-header">
        Medicus Assist
      </header>
      <div className="dashboard">
        <div className="category">
          <div className="category-header">Scheduling</div>
          {categories.scheduling.map((item, index) => (
            <button key={index} onClick={() => onSelectExample(item)} className="example-button">{item}</button>
          ))}
        </div>
        <div className="category">
          <div className="category-header">Medical Advice</div>
          {categories.medicalAdvice.map((item, index) => (
            <button key={index} onClick={() => onSelectExample(item)} className="example-button">{item}</button>
          ))}
        </div>
        <div className="category">
          <div className="category-header">Medication Reminders</div>
          {categories.medicationReminders.map((item, index) => (
            <button key={index} onClick={() => onSelectExample(item)} className="example-button">{item}</button>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
