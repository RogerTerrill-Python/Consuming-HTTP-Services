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
    max_width = max(len(f'{int(p.view_count):,}') for p in posts)
    for idx, p in enumerate(posts):
        padded = ' ' * (max_width - len(f'{int(p.view_count):,}'))
        print(f'{idx + 1}. {p.id} [{padded}{int(p.view_count):,}]: {p.title}')
    print()


def get_posts():
    print("TODO: GET POSTS")
    return []


def add_post():
    now = datetime.datetime.now()
    published_text = f'{now.year}-{str(now.month).zfill(2)}-{str(now.day).zfill(2)}'

    print("TODO: ADD POST")


def update_post():
    print("To update a post, choose the number from the list below:")
    posts = get_posts()
    show_posts(posts)
    print()

    print("TODO: UPDATE POST")


def delete_post():
    print("TODO: DELETE POST")


if __name__ == '__main__':
    main()