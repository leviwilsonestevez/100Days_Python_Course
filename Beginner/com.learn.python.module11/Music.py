import random
import pygame
from pygame import mixer


def play_playlist() -> None:
    global _currently_playing_song, playlist
    # playlist = ('soundtrack/never_late_smooth_jazz_piano_soft.wav', 'soundtrack/never_late_smooth_jazz_soft.wav',
    # 'soundtrack/mr_mason_jazz.wav', 'soundtrack/music_zapsplat_win_city.wav')
    playlist = ('soundtrack/never_late_smooth_jazz_piano_soft.wav', 'soundtrack/never_late_smooth_jazz_soft.wav')
    _currently_playing_song = random.choice(playlist)
    next_song = random.choice(playlist)
    while next_song == _currently_playing_song:
        next_song = random.choice(playlist)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()
