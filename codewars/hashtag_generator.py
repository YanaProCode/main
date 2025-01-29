"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
"""

def generate_hashtag(s):
    res = "#" + s.strip().title()
    if " " in res:
        list = res.split()
        result = "".join(list)
        if result == "#" or len(result) > 140:
            return False
        return result
    if res == "#" or len(res) > 140:
        return False
    return res