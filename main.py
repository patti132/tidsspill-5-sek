def on_button_pressed_a():
    seconds = 0
    if seconds < 6:
        serial.write_string("Bra Jobbet! Det var nesten!!")
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

Juksemodus = 0
resultat = 0
Forsรธk = 0
tid1 = 0
tid2 = 0
serial.redirect_to_usb()
basic.show_string("TS v1", 60)
serial.write_line("๐๐๐ก๐ ๐ค๐ข๐ข๐๐ฃ ๐ฉ๐๐ก ๐๐๐๐จ๐จ๐ฅ๐๐ก๐ก ๐ซ1")

def on_forever():
    global Forsรธk, resultat, Juksemodus
    if input.button_is_pressed(Button.A):
        basic.show_number(Forsรธk)
        Forsรธk += 1
        serial.write_string("๐๐จ๐ซ๐ฌรธ๐ค:")
        serial.write_number(Forsรธk)
        serial.write_line("")
        tid12 = input.running_time_micros()
        grense = 1
        while input.button_is_pressed(Button.A):
            pass
        tid22 = input.running_time_micros()
        serial.write_line("")
        resultat = (tid22 - tid12) / 1000000
        # basic.show_number(resultat,60)
        serial.write_string("๐๐ข๐ญ๐ญ ๐๐๐ฌ๐ฎ๐ฅ๐ญ๐๐ญ:")
        serial.write_number(resultat)
        serial.write_line("")
    if input.logo_is_pressed():
        basic.show_number(Forsรธk)
        Forsรธk += 1
        serial.write_string("๐๐จ๐ซ๐ฌรธ๐ค:")
        serial.write_number(Forsรธk)
        serial.write_line("")
        basic.show_number(Juksemodus)
        Juksemodus = 5000
        serial.write_string("๐๐ข๐ญ๐ญ ๐๐๐ฌ๐ฎ๐ฅ๐ญ๐๐ญ:")
        serial.write_number(Juksemodus)
        serial.write_line("")
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
basic.forever(on_forever)
