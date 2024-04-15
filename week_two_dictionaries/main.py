anime_tags: [str, str] = {"Shingeki no Kyojin": "war", "K-On!": "music",
                          "Steins;Gate": "physics", "Kimetsu no Yaiba": "demons"}

print(anime_tags)
anime_tags["Noragami"] = "kami"
print(anime_tags)

new_tags = anime_tags.pop("Noragami")
print(new_tags)
print(anime_tags)

for a in anime_tags.keys():
    print(f"{a} : {anime_tags[a]}")
