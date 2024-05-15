import os
import pytube
import youtube_downloader

choice = input("ecrire start: ")

if choice == "start":
    quality = input("Please choose a quality (low, medium, high, very high):")
    if True:
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")

        filename = youtube_downloader.download_video(link, quality)
        print("Downloaded video:", os.path.abspath(filename))  # Affiche le chemin absolu du fichier téléchargé


else:
    print("Invalid input! Terminating...")

# Afficher le message dans le terminal
print("Operation finished!")
