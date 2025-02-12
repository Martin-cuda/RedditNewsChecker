
import requests

def get_reddit_news_headlines():
    url = "https://www.reddit.com/r/news/top.json"
    headers = {
        'User-Agent': 'redditnewschecker/1.0 (by Martin Weber)' 
    }
    
 
    params = {
        'limit': 15,          
        't': 'day',           
        'show': 'all'         
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status() 
        
        data = response.json()
        posts = data['data']['children']
        
        headlines = []
        for post in posts:
            post_data = post['data']
            
            if not post_data['stickied'] and post_data['is_self'] == False:
                headlines.append(post_data['title'])
            if len(headlines) >= 10:
                break
        
        if not headlines:
            print("No headlines found!")
            return
        
        print("Top 10 r/news Headlines:\n" + "-" * 25)
        for idx, title in enumerate(headlines, 1):
            print(f"{idx}. {title}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except (KeyError, ValueError) as e:
        print(f"Error parsing response: {e}")

if __name__ == "__main__":
    get_reddit_news_headlines()