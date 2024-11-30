# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import xml.etree.ElementTree as ET
import json as json_module


class UnhandledException(Exception):
    pass


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        >>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        >>> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        >>> print("\\n".join(rss_parser(xmls)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    try:
        root = ET.fromstring(xml)
        channel = root.find('channel')

        title = channel.find('title').text if channel.find('title') is not None else None
        link = channel.find('link').text if channel.find('link') is not None else None
        description = channel.find('description').text if channel.find('description') is not None else None
        category = channel.find('category').text if channel.find('category') is not None else None
        language = channel.find('language').text if channel.find('language') is not None else None
        lastBuildDate = channel.find('lastBuildDate').text if channel.find('lastBuildDate') is not None else None
        managingEditor = channel.find('managingEditor').text if channel.find('managingEditor') is not None else None
        pubDate = channel.find('pubDate').text if channel.find('pubDate') is not None else None

        items = []
        for item in channel.findall('item'):
            item_title = item.find('title').text if item.find('title') is not None else None
            author = item.find('author').text if item.find('author') is not None else None
            pubDate = item.find('pubDate').text if item.find('pubDate') is not None else None
            link = item.find('link').text if item.find('link') is not None else None
            category = item.find('category').text if item.find('category') is not None else None
            description = item.find('description').text if item.find('description') is not None else None
            items.append({
                'title': item_title,
                'author': author,
                'pubDate': pubDate,
                'link': link,
                'category': category,
                'description': description,
            })
            if limit is not None and len(items) >= limit:
                break

    except ET.ParseError as e:
        raise UnhandledException(f'Failed to parse XML: {e}')

    data = {
        'title': title,
        'link': link,
        'description': description,
        'category': category,
        'language': language,
        'lastBuildDate': lastBuildDate,
        'managingEditor': managingEditor,
        'pubDate': pubDate,
        'items': items,
    }

    if json:
        return json_module.dumps(data, indent=2)

    else:
        output = []
        if title: output.append(f"Feed: {title}")
        if link: output.append(f"Link: {link}")
        if lastBuildDate: output.append(f"Last Build Date: {lastBuildDate}")
        if pubDate: output.append(f"Publish Date: {pubDate}")
        if language: output.append(f"Language: {language}")
        if category: output.append(f"Categories: {category}")
        if managingEditor: output.append(f"Editor: {managingEditor}")
        if description: output.append(f"Description: {description}")
        for item in data['items']:
            output.append("\n")
            if item['title']: output.append(f"Title: {item['title']}")
            if item['author']: output.append(f"Author: {item['author']}")
            if item['pubDate']: output.append(f"Published: {item['pubDate']}")
            if item['link']: output.append(f"Link: {item['link']}")
            if item['category']: output.append(f"Categories: {item['category']}")
            if item['description']: output.append(f"Description: {item['description']}")
    return output


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text

    try:
        xml = requests.get(args.source).text
    except requests.exceptions.RequestException as e:
        raise UnhandledException(f'Failed to fetch XML document: {e}')

    try:
        result = rss_parser(xml, args.limit, args.json)
        if args.json:
            print(result)
        else:
            print("\n".join(result))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
