import connexion
import six
import json

from swagger_server.models.clothing_article import ClothingArticle  # noqa: E501
from swagger_server import util


def clothing_get():  # noqa: E501
    """Retrieve a list of clothing articles

    Returns a list of clothing articles with price and category.

    :rtype: List[ClothingArticle]
    """
    with open('./clothing-inventory.json', 'r') as f:
        clothing_data = json.load(f)

    clothing_articles = []
    for article_data in clothing_data:
        article = ClothingArticle(
            id=article_data['id'],
            category=article_data['category'],
            price=article_data['price']
        )
        clothing_articles.append(article)

    return clothing_articles

import sys
import os


import json
from typing import Dict


def clothing_post(article: Dict) -> None:
    """Add a new clothing article

    Adds a new clothing article with price and category.

    :param article: Clothing article object
    :type article: dict

    :rtype: None
    """
    # Load existing clothing articles from file


    print(article['category'])
    with open('./clothing-inventory.json', 'r') as f:
        clothing_data = json.load(f)

    # Find the latest ID and increment by 1
    latest_id = max(article['id'] for article in clothing_data)
    new_id = latest_id + 1


    # Create a new ClothingArticle object with the provided data
    new_article = ClothingArticle(
        id=new_id,
        category=article['category'],
        price=article['price']
    )



    # Append the new article to the list of clothing articles
    clothing_data.append(new_article.to_dict())

    # Write the updated list of clothing articles back to the file
    with open('./clothing-inventory.json', 'w') as f:
        json.dump(clothing_data, f)

    return None
