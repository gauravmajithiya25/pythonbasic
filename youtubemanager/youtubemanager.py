import json

def load_data():
    try:
        with open('Youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
           return []

def save_data_helper(videos):
    with open('Youtube.txt','w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} - {video['time']}")

def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)

    if not videos:
        return

    try:
        video_index = int(input("Enter video number to update: "))

        if 1 <= video_index <= len(videos):
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")

            videos[video_index - 1] = {
                'name': name,
                'time': time
            }

            save_data_helper(videos)
            print("Video updated successfully!")

        else:
            print("Invalid video number!")

    except ValueError:
        print("Please enter a valid number!")

def delete_video(videos):
    list_all_videos(videos)

    if not videos:
        return

    try:
        video_index = int(input("Enter video number to delete: "))

        if 1 <= video_index <= len(videos):
            deleted_video = videos.pop(video_index - 1)

            save_data_helper(videos)

            print(f"Video '{deleted_video['name']}' deleted successfully!")

        else:
            print("Invalid video number!")

    except ValueError:
        print("Please enter a valid number!")

def main():
    videos = load_data()
    while True:
        print(" \n YouTube Manager | Chose an option")
        print("1. List all Video manager")
        print("2. Add  a youtube video")
        print("3. Update  a youtube video")
        print("4. Delete  a youtube video")
        print("5. Exit the app" )
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("in Valid Choice")

if  __name__ == main() == "__main__":
    main()
