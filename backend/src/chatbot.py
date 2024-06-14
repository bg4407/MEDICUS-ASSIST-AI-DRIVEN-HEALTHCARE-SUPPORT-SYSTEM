class chatbot:

    def chatbot():
        responses = {
            "headache": "It sounds like you have a headache. You might try taking some rest and drinking plenty of water. If it persists, consider taking a pain reliever like ibuprofen or acetaminophen.",
            "fever": "For a fever, it's important to stay hydrated and rest. Over-the-counter medications like acetaminophen or ibuprofen can help reduce the fever.",
            "cough": "If you have a cough, staying hydrated is important. Warm drinks like tea with honey can soothe your throat. If the cough persists, you might consider seeing a doctor.",
            "cold": "Common cold symptoms can be managed with rest, fluids, and over-the-counter medications like decongestants and pain relievers.",
            "stomach ache": "For a stomach ache, try to rest and avoid eating heavy meals. Drinking clear fluids and eating light, bland foods like crackers or toast might help.",
            "allergy": "If you're experiencing allergies, over-the-counter antihistamines can help. Avoiding the allergen and keeping your living space clean can also reduce symptoms.",
            "injury": "For minor injuries, applying ice and keeping the affected area elevated can help reduce swelling. If it's severe, please seek medical attention.",
            "stress": "Managing stress involves regular exercise, healthy eating, and adequate sleep. Techniques like deep breathing, meditation, and talking to someone can also be beneficial.",
            "anxiety": "For anxiety, practices like deep breathing, meditation, and talking to a therapist can help. Regular physical activity and avoiding caffeine can also be beneficial.",
            "fatigue": "If you're feeling fatigued, make sure you're getting enough sleep and eating a balanced diet. Regular physical activity can also improve energy levels.",
            "back pain": "For back pain, try to rest and avoid heavy lifting. Applying ice or heat, as well as taking over-the-counter pain relievers, can help. If pain persists, consult a doctor.",
            "nausea": "For nausea, try sipping clear fluids and eating bland foods like crackers or toast. Ginger tea or peppermint can also help soothe your stomach.",
            "insomnia": "If you're having trouble sleeping, establish a regular sleep schedule, create a restful environment, and avoid caffeine and electronics before bed.",
            "diarrhea": "For diarrhea, stay hydrated with clear fluids and consider over-the-counter medications like loperamide. Avoid dairy and high-fiber foods until you feel better.",
            "constipation": "For constipation, increase your fiber intake with fruits, vegetables, and whole grains. Drinking plenty of water and staying active can also help.",
            "sore throat": "For a sore throat, drink warm liquids like tea with honey, and use throat lozenges. Gargling with salt water can also provide relief.",
            "earache": "For an earache, applying a warm compress and taking over-the-counter pain relievers can help. If pain persists, see a doctor.",
            "rash": "If you have a rash, avoid scratching and try applying a gentle moisturizer or hydrocortisone cream. If it gets worse, consult a doctor.",
            "burn": "For minor burns, cool the area with running water and apply aloe vera or a burn ointment. Cover it with a sterile bandage and avoid popping any blisters.",
            "dehydration": "For dehydration, drink plenty of water and consider oral rehydration solutions. Avoid caffeine and alcohol, which can worsen dehydration.",
            "dizziness": "If you feel dizzy, sit or lie down and avoid sudden movements. Drinking water and eating something can also help if dizziness is due to low blood sugar."
        }   

        print("Chatbot: Hi! I am your medical assistant. How can I help you today? (Type your ailment, or END to end the chat)")
        
        while True:
            user_input = input("You: ").lower()
            
            if user_input == "END":
                print("Chatbot: Goodbye! Take care!")
                break
            
            found_response = False
            for keyword, response in responses.items():
                if keyword in user_input:
                    print(f"Chatbot: {response}")
                    found_response = True
                    break
            
            if not found_response:
                print("Chatbot: I'm sorry, I didn't understand that. Can you please describe your symptoms or issue in more detail?")

    if __name__ == "__main__":
        chatbot()