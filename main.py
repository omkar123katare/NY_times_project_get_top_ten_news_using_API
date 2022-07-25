import requests

class news:
    def __init__(self):
        print("Hello")


        action = input("Do you want to see todays hot news?")
        if action == 'yes':
            self.get_news()

    def get_news(self):
        data=requests.get("https://api.nytimes.com/svc/topstories/v2/home.json?api-key=GJInWB6KuYi0jKRh01GJdHp3o3G42sIL")
        data=data.json()
        print('The top 10 headlines are')
        for i in range(10):
            print(data['results'][i]['title'])
            print(f"written by ------{data['results'][i]['byline']}")
            print(f"News in short ---->>{data['results'][i]['abstract']}")
obj1=news()
