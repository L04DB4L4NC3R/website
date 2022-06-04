import requests
import sys

print("fetching post list...")
metadata = "---\ntitle: '{0}'\ndate: '{1}'\nthumb_img_path: '{2}'\ncanonical_url: '{3}'\nexcerpt: '{4}'\nlayout: post\n---\n\n"

data = requests.get("https://dev.to/api/articles?username=l04db4l4nc3r&per_page=1000").json()
print("done")

print("fetching posts....")

for i in data:
    with open("{0}/{1}.md".format(sys.argv[1], i['title']), "w") as file:
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
