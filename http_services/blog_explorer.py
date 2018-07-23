import datetime
import json
import requests
import collections

Post = collections.namedtuple("Post", 'id title content published view_count')

base_url = 'http://consumer_services_api.talkpython.fm/'


def main():
    print("Blog explorer (requests version)")

    while True:
        action = input('What to do with this blog api? [l]ist, [a]dd, [u]pdate, [d]elete, e[x]it: ')
        if action == 'x':
            print("Exiting...")
            break
        if action == 'l':
            posts = get_posts()
            show_posts(posts)
        if action == 'a':
            add_post()
        if action == 'u':
            update_post()
        if action == 'd':
            delete_post()


def show_posts(posts):
    if not posts:
        print('Sorry, no posts to show.')
        return

    print("--------------------------------- BLOG POSTS ------------------------------------")
    # Checks the number of characters in the view count to make a uniform list and uses the max
    # By using list comprehension
    # In this case the number is 5 because there are five characters in 1,231
    max_character_width_for_view_count = max(len(f'{int(p.view_count):,}') for p in posts)

    for idx, p in enumerate(posts):
        # Padded pads the front to align view counts to the right
        padding_in_front_of_view_count = ' ' * (max_character_width_for_view_count - len(f'{int(p.view_count):,}'))
        print(f'{idx + 1}. {p.id} [{padding_in_front_of_view_count}{int(p.view_count):,}]: {p.title}')
    print()


def get_posts():
    url = base_url + 'api/blog'
    headers = {'Accept': 'application/json'}
    resp = requests.get(url, headers=headers)

    if resp.status_code != 200:
        print(f"Error downloading posts: {resp.status_code} {resp.text}")
        return []

    return [
        # Uses keyword arguments to fill in the namedtuple since it's 1 to 1
        # Converts the post json to dictionary arguments
        Post(**post)
        for post in resp.json()
    ]


def add_post():
    now = datetime.datetime.now()
    published_text = f'{now.year}-{str(now.month).zfill(2)}-{str(now.day).zfill(2)}'

    title = input('title: ')
    content = input('content: ')
    view_count = int(input('view count: '))

    post_data = dict(title=title, content=content, view_count=view_count, published=published_text)
    url = base_url + 'api/blog'

    resp = requests.post(url, json=post_data)

    if resp.status_code != 201:
        print(f'Error creating posts: {resp.status_code} {resp.text}')
        return

    post = resp.json()
    print("created this: ")
    print(post)


def update_post():
    print("To update a post, choose the number from the list below:")
    posts = get_posts()
    show_posts(posts)
    print()

    # Ask for post number and then insert into variable post
    post = posts[int(input('Enter number of post to edit: '))-1]

    # Enter new title or second line says if blank, then just reenter old title
    title = input('title: [' + post.title + '] ')
    title = title if title else post.title

    content = input('content: [' + post.content + '] ')
    content = content if content else post.content

    view_count = input('view count: [' + str(post.view_count) + '] ')
    view_count = int(view_count if view_count else post.view_count)

    post_data = dict(title=title, content=content, view_count=view_count, published=post.published)

    url = base_url + 'api/blog/' + post.id
    resp = requests.put(url, data=json.dumps(post_data))

    if resp.status_code != 204:
        print(f"Error updating post: {resp.status_code} {resp.text}")
        return

    print(f"Successfully updated {post.title}")


def delete_post():
    print("TODO: DELETE POST")


if __name__ == '__main__':
    main()