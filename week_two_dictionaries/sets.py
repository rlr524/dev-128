music_roster = {"Madison", "Olivia", "Tzuyu", "Jisoo", "Rosé"}
sports_roster = {"Nicole", "Mei", "Sarah", "Olivia", "Jason"}

print(music_roster | sports_roster)
print(music_roster & sports_roster)
print(music_roster ^ sports_roster)
print(music_roster - sports_roster)
print(sports_roster - music_roster)