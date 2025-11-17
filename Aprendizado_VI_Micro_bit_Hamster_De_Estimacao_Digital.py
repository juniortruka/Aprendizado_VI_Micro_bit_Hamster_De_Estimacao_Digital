# Hamster de estimação Digital
# Ao pressionar a logo da placa

def on_logo_pressed():
    # Mostrar o icone Hamster
    basic.show_icon(IconNames.ASLEEP)
    # Tocar uma música/melodia;
    music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
        music.PlaybackMode.IN_BACKGROUND)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

# Ao agitar/sacudir a placa;

def on_gesture_shake():
    basic.show_icon(IconNames.SURPRISED)
    # Icone triste.
    basic.show_icon(IconNames.SAD)
    # Tocar melodia triste.
    music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
        music.PlaybackMode.IN_BACKGROUND)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# Moistrar icone inicial
basic.show_icon(IconNames.TSHIRT)
basic.show_icon(IconNames.HAPPY)
