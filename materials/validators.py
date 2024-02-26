from rest_framework import serializers


def wrong_links_validator(text):
    links = text.split(' ')
    example_links = ['.com', '.ru', '.org']
    right_link = 'youtube'
    having_links = []
    for link in links:
        for example in example_links:
            if example in link.lower():
                having_links.append(link)
                if right_link not in link.lower():
                    raise serializers.ValidationError("You should delete wrong links (only on www.youtube.com)")
    if len(having_links) == 0:
        raise serializers.ValidationError("You should add link (for example, www.youtube.com")