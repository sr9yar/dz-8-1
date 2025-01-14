from requests import get
from json import loads



def get_posts():
  res = get("https://jsonplaceholder.typicode.com/posts")
  body = loads(res.text)
  return body



def main():
  print("Выводим 5 первых постов.\n\n")

  posts = [ item for item in get_posts()[0:5] ]

  for index in range(len(posts)):
    post = posts[index]
    print(f"Пост {index+1}. {post["title"]}\n")
    print(f"{post["body"]}\n\n")



main()


