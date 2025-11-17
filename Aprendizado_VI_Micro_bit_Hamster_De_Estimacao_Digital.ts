// Hamster de estimação Digital
// Ao pressionar a logo da placa
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    // Mostrar o icone Hamster
    basic.showIcon(IconNames.Asleep)
    // Tocar uma música/melodia;
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Dadadadum), music.PlaybackMode.InBackground)
})
// Ao agitar/sacudir a placa;
input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.Surprised)
    // Icone triste.
    basic.showIcon(IconNames.Sad)
    // Tocar melodia triste.
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Dadadadum), music.PlaybackMode.InBackground)
})
// Moistrar icone inicial
basic.showIcon(IconNames.TShirt)
basic.showIcon(IconNames.Happy)
