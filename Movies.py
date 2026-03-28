import re
import random
from typing import Dict, List, Tuple, Optional
from datetime import datetime

class BollywoodMotivationBot:
    def __init__(self):
        self.movies_db = self._load_movies()
        self.quotes_db = self._load_quotes()
        self.history = []
    
    def _load_movies(self) -> Dict[str, List[Dict]]:
        """Database of motivational Bollywood movies post-2017"""
        return {
            'struggle_to_success': [
                {
                    'title': 'Dangal (2016)*',
                    'year': 2016,
                    'rating': '8.3/10',
                    'theme': 'Never give up, family support, gender equality',
                    'story': "A father trains his daughters to become world-class wrestlers against all odds.",
                    'motivation': "Proves that with determination and hard work, anyone can achieve greatness.",
                    'lessons': ['Persistence beats talent', 'Family support is key', 'Break stereotypes'],
                    'iconic_scene': "Final wrestling match - Geeta vs Kadam"
                },
                {
                    'title': 'Sultan (2016)*',
                    'year': 2016,
                    'rating': '7.0/10',
                    'theme': 'Redemption, comeback, love for wrestling',
                    'story': "A fallen wrestler makes a comeback to regain his glory and save his love.",
                    'motivation': "No matter how many times you fall, you can rise again stronger.",
                    'lessons': ['Second chances exist', 'Love fuels determination', 'Age is just a number'],
                    'iconic_scene': "Sultan vs Fateh - epic comeback fight"
                },
                {
                    'title': 'Secret Superstar (2017)',
                    'year': 2017,
                    'rating': '7.8/10',
                    'theme': 'Follow your dreams, courage against oppression',
                    'story': "A young girl pursues singing dreams while hiding from her abusive father.",
                    'motivation': "Your talent can change your destiny, even in toughest circumstances.",
                    'lessons': ['Believe in yourself', 'One supporter can change everything', 'Courage over comfort'],
                    'iconic_scene': "Insia\'s first viral song performance"
                },
            ],
            
            'career_ambition': [
                {
                    'title': 'Gangubai Kathiawadi (2022)',
                    'year': 2022,
                    'rating': '8.1/10',
                    'theme': 'Rise from adversity, leadership, self-respect',
                    'story': "A woman rises from brothel to become a powerful mafia queen.",
                    'motivation': "Transform your pain into power and command respect.",
                    'lessons': ['Own your story', 'Leadership through empathy', 'Rise above circumstances'],
                    'iconic_scene': "Gangubai\'s powerful speech at Azad Maidan"
                },
                {
                    'title': 'Chhichhore (2019)',
                    'year': 2019,
                    'rating': '8.3/10',
                    'theme': 'Failure is success in progress, college life',
                    'story': "Friends teach a young man that losing isn\'t failing.",
                    'motivation': "Failure is just a temporary detour, not a dead end.",
                    'lessons': ['Redefine success', 'Friendship > competition', 'Enjoy the journey'],
                    'iconic_scene': "Raggie\'s suicide prevention speech"
                },
                {
                    'title': 'Super 30 (2019)',
                    'year': 2019,
                    'rating': '7.7/10',
                    'theme': 'Education changes destiny, against all odds',
                    'story': "An IITian teaches 30 underprivileged students to crack IIT.",
                    'motivation': "One teacher can change hundreds of lives through education.",
                    'lessons': ['Knowledge > money', 'Help others rise with you', 'Quality over quantity'],
                    'iconic_scene': "All 30 students crack IIT JEE"
                },
            ],
            
            'sports_spirit': [
                {
                    'title': '83 (2021)',
                    'year': 2021,
                    'rating': '8.1/10',
                    'theme': 'Teamwork, national pride, underdog victory',
                    'story': "India\'s historic 1983 Cricket World Cup victory.",
                    'motivation': "United we stand, divided we fall - team spirit wins trophies.",
                    'lessons': ['Team > individual', 'Believe when others don\'t', 'History is made by underdogs'],
                    'iconic_scene': "Kapil Dev catches Viv Richards"
                },
                {
                    'title': 'Paan Singh Tomar (2012)*',
                    'year': 2012,
                    'rating': '8.1/10',
                    'theme': 'Hidden talent, revenge through excellence',
                    'story': "Army runner becomes bandit after injustice.",
                    'motivation': "Channel your anger into excellence and world records.",
                    'lessons': ['Talent needs opportunity', 'Injustice fuels determination', 'Records > revenge'],
                    'iconic_scene': "Paan Singh\'s national record race"
                },
                {
                    'title': 'Mimi (2021)',
                    'year': 2021,
                    'rating': '7.6/10',
                    'theme': 'Motherhood struggles, never give up',
                    'story': "Surrogate mother fights to keep her child.",
                    'motivation': "A mother\'s love and determination can move mountains.",
                    'lessons': ['Fight for family', 'Selfless love wins', 'Never abandon dreams'],
                    'iconic_scene': "Mimi\'s emotional courtroom fight"
                },
            ],
            
            'life_lessons': [
                {
                    'title': '12th Fail (2023)',
                    'year': 2023,
                    'rating': '9.0/10',
                    'theme': 'UPSC journey, persistence, mental strength',
                    'story': "Manoj Kumar Sharma\'s real-life journey from failure to IPS officer.",
                    'motivation': "12th fail doesn\'t mean life fail - persistence creates IPS officers.",
                    'lessons': ['Small steps daily', 'Failure builds character', 'Honesty > shortcuts'],
                    'iconic_scene': "Manoj\'s 4th UPSC attempt success"
                },
                {
                    'title': 'Laapataa Ladies (2023)',
                    'year': 2023,
                    'rating': '8.5/10',
                    'theme': 'Women empowerment, self-discovery',
                    'story': "Two brides get swapped and find their true calling.",
                    'motivation': "Sometimes getting lost is how you find your true path.",
                    'lessons': ['Self-reliance', 'Education transforms', 'Value yourself'],
                    'iconic_scene': "Phool\'s transformation from housewife to police officer"
                },
                {
                    'title': 'Article 370 (2024)',
                    'year': 2024,
                    'rating': '8.1/10',
                    'theme': 'National service, tough decisions',
                    'story': "Officer\'s mission to implement Article 370 abrogation.",
                    'motivation': "Sometimes you must make tough calls for greater good.",
                    'lessons': ['Duty > popularity', 'History demands courage', 'Nation first'],
                    'iconic_scene': "Final operation success"
                }
            ]
        }
    
    def _load_quotes(self) -> Dict[str, List[str]]:
        """Motivational quotes from movies"""
        return {
            'Dangal': ['"Mahavir Singh Phogat ne khud ladkhiyaan paida ki hain, toh ladkhiyaan hi banayenge!"'],
            'Chhichhore': ['"Mat haar, lad!"', '"Loser jeetne ke liye banta hai!"'],
            '12th Fail': ['" Haar nahi maani, toh jeet gaye!"'],
            'Gangubai': ['"Main yahan ki rani hoon!"'],
            'Secret Superstar': ['"Sapne dekhna band mat karo!"']
        }
    
    def find_motivational_movie(self, query: str) -> Optional[Tuple[str, Dict]]:
        """Find best matching movie"""
        query_lower = query.lower()
        
        # Keyword matching
        keywords = {
            'struggle': 'struggle_to_success',
            'fail|failure': 'life_lessons',
            'career|job|success': 'career_ambition',
            'sport|cricket|wrestling': 'sports_spirit',
            'women|girl|lady': 'struggle_to_success',
            'upsc|exam|study': 'life_lessons'
        }
        
        for keyword, category in keywords.items():
            if re.search(keyword, query_lower):
                movies = self.movies_db[category]
                return category, random.choice(movies)
        
        # General recommendation
        all_movies = []
        for category_movies in self.movies_db.values():
            all_movies.extend(category_movies)
        return 'general', random.choice(all_movies)
    
    def generate_response(self, query: str) -> str:
        """Generate motivational movie response"""
        self.history.append(query)
        
        category, movie = self.find_motivational_movie(query)
        quotes = self._load_quotes().get(movie['title'], [])
        
        response = f"""
 **Recommended Movie: {movie['title']} ({movie['year']})** 🎥

 **IMDb Rating:** {movie['rating']}
 **Core Message:** {movie['motivation']}

 **Quick Story:**
{movie['story']}

 **Why Watch for Motivation:**
- {movie['lessons'][0]}
- {movie['lessons'][1]}
- {movie['lessons'][2]}

 **Iconic Scene:** {movie['iconic_scene']}
 **Power Quote:** {random.choice(quotes) if quotes else 'Kamyabi pakad ke nahi aati, pakadni padti hai!'}

 **Where to Watch:** Netflix/Prime/OTT platforms
"""
        
        # Add category specific motivation
        if category == 'life_lessons':
            response += "\n\n💪 **Today's Mantra:** Failure is progress in disguise!"
        elif category == 'sports_spirit':
            response += "\n\n🏆 **Today's Mantra:** Teamwork makes the dream work!"
        
        response += f"\n\nWhat else motivates you? 🎯"
        self.history.append(response)
        return response
    
    def chat(self):
        """Main chat interface"""
        print("🎥 **BOLLYWOOD MOTIVATION BOT** 🎥")
        print("Get inspired by post-2017 Bollywood movies!")
        print("Ask: 'motivational movies about failure', 'sports movies', 'women empowerment films'\n")
        
        while True:
            query = input("You: ").strip()
            
            if query.lower() in ['quit', 'exit', 'bye', 'thanks']:
                print("\n🚀 Keep getting motivated! 💪\n'Jab tak saans hai, ladte rahenge!'")
                break
            
            if query:
                response = self.generate_response(query)
                print(f"\n🤖 MotivationBot:\n{response}\n{'='*70}\n")
            else:
                print("Tell me what kind of motivation you need! 💬")

# Bonus: Quick movie recommender
def quick_recommend():
    """Quick recommendation function"""
    bot = BollywoodMotivationBot()
    categories = list(bot.movies_db.keys())
    print("\n🎬 **Today's Top Pick:**")
    print(bot.generate_response(f"best {random.choice(categories)} movie"))

if __name__ == "__main__":
    bot = BollywoodMotivationBot()
    bot.chat()
