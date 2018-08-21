# ForumScraper

ForumScraper is a WIP project designed to achieve two goals:
- Scrape the legacy Overwatch Forum and back it up before it gets deleted eventually
- Allow me to practice with somewhat standard scraping and backend tools that I'm lacking experience in.

As of now this repo is literally just this readme, and there is no guarantee it will progress beyond this.

That said the overall roadmap of the project is as follows:
- Use beautifulsoup and python to crawl across the forum and scrape all the posts
- Store said data in both a postgres db and in an easily shared log format
- Either create a web page to make searches accessible or allow users to serve a page on their own localhost
- Do data science on the logs. Sentiment analysis, clustering users, generate "new" announcements based on how the past ones looked like
