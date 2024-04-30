import pygame

def play_mp3(file_path):
    pygame.init()
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print("Error:", e)
    finally:
        pygame.mixer.quit()
        pygame.quit()

# Example usage
mp3_file_path = "./audio/hello.mp3"
play_mp3(mp3_file_path)
