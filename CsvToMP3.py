from youtube_search import YoutubeSearch
from pytube import YouTube
import csv

def find_and_download_songs(text_to_search: str, folder):
    TOTAL_ATTEMPTS = 10

    best_url = None
    attempts_left = TOTAL_ATTEMPTS
    while attempts_left > 0:
        try:
            results_list = YoutubeSearch(text_to_search, max_results=1).to_dict()
            best_url = "https://www.youtube.com{}".format(results_list[0]['url_suffix'])
            break
        except IndexError:
            attempts_left -= 1
            print("No valid URLs found for {}, trying again ({} attempts left).".format(
                text_to_search, attempts_left))
        if best_url is None:
            print("No valid URLs found for {}, skipping track.".format(text_to_search))
            continue
    # Run you-get to fetch and download the link's audio
    print("Download ", text_to_search)

    destination = "./" + folder + "/"
    try:
        video = YouTube(best_url)
        audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
        audio.download(destination)
        print('Download Completed!')

    except:
        print("Connection Error")  # to handle exception

                
if __name__ == "__main__":
    print ("Extract sound list from csv file")
    trackList = []
    
    with open('playlist.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            trackList.append(row['Track Name'] + " "  + row['Artist Name(s)'])
   
