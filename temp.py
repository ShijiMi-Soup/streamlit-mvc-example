import model

users = model.Users()
posts = model.Posts()

print(posts.add("Hello, World!"))
print(posts.read())