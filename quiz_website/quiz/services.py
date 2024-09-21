"""module to handle third party API requests"""
import requests



def get_questions(category=None, difficulty=None, num_questions=10):
    """
    Fetch quiz questions from a third-party API (like Open Trivia Database)
    """
    url = "https://opentdb.com/api.php"
    params = {
        "amount": num_questions,
        "type": "multiple",  # Use 'multiple' for multiple-choice questions
    }
    
    # Optional filters
    if category:
        params['category'] = category
    if difficulty:
        params['difficulty'] = difficulty
    
    # Make the request to the external API
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        # Check if we have valid results
        if data['response_code'] == 0:  # 0 means success
            return data['results']
        else:
            return []
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []
