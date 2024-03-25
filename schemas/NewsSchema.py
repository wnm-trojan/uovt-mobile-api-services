"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - News schema.
"""

from app import ma

class NewsSchema(ma.Schema):
    class Meta:
        fields = ('news_code', 'title', 'author', 'category', 'news_id', 'link', 'imgSrc', 'placeholder', 'summary', 'contentLength', 'status')