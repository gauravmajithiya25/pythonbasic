
import sqlite3

conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
""")
conn.commit()


# 1. List all videos
def list_video():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()

    if not videos:
        print("No videos found!")
        return

    for video in videos:
        print(f"ID: {video[0]} | Name: {video[1]} | Time: {video[2]}")


# 2. Add a video
def add_video(name, time):
    cursor.execute(
        "INSERT INTO videos (name, time) VALUES (?, ?)",
        (name, time)
    )
    conn.commit()
    print("Video added successfully!")


# 3. Update a video
def update_video(video_id, name, time):
    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (name, time, video_id)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("Video updated successfully!")
    else:
        print("Video ID not found!")


# 4. Delete a video
def delete_video(video_id):
    cursor.execute(
        "DELETE FROM videos WHERE id = ?",
        (video_id,)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("Video deleted successfully!")
    else:
        print("Video ID not found!")


# Main menu
def main():
    while True:
        print("\nYouTube Manager | Choose an option")
        print("1. List all videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_video()

        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)

        elif choice == "3":
            video_id = input("Enter video ID to update: ")
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            update_video(video_id, name, time)

        elif choice == "4":
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)

        elif choice == "5":
            print("Exiting YouTube Manager...")
            break

        else:
            print("Invalid choice! Please try again.")

    conn.close()


if __name__ == "__main__":
    main()
