import requests

print("fetching post list...")
metadata = "---\ntitle: '{0}'\ndata: '{1}'\nthumb_img_path: >-\n  '{1}'\ncanonical_url: '{3}'\nexcerpt: >-\n {4}\nlayout: post\n---\n\n"

data = requests.get("https://dev.to/api/articles?username=l04db4l4nc3r&per_page=1000").json()
print("done")

print("fetching posts....")

for i in data:
    with open("./content/posts/{}.md".format(i['title']), "w") as file:
        file.write(
            metadata.format(
                i['title'],
                i['published_at'],
                i['cover_image'],
                i['canonical_url'],
                i['description']
            )
        )
        file.write(
            requests.get(
                "https://dev.to/api/articles/{0}".format(i['id'])).json()['body_markdown']
        )

print("done")
