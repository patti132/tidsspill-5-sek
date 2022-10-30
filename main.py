def on_button_pressed_a():
    seconds = 0
    if seconds < 6:
        serial.write_string("Bra Jobbet! Det var nesten!!")
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

Juksemodus = 0
resultat = 0
Forsøk = 0
tid1 = 0
tid2 = 0
serial.redirect_to_usb()
basic.show_string("TS v1", 60)
serial.write_line("𝙑𝙚𝙡𝙠𝙤𝙢𝙢𝙚𝙣 𝙩𝙞𝙡 𝙏𝙞𝙙𝙨𝙨𝙥𝙞𝙡𝙡 𝙫1")

def on_forever():
    global Forsøk, resultat, Juksemodus
    if input.button_is_pressed(Button.A):
        basic.show_number(Forsøk)
        Forsøk += 1
        serial.write_string("𝐅𝐨𝐫𝐬ø𝐤:")
        serial.write_number(Forsøk)
        serial.write_line("")
        tid12 = input.running_time_micros()
        grense = 1
        while input.button_is_pressed(Button.A):
            pass
        tid22 = input.running_time_micros()
        serial.write_line("")
        resultat = (tid22 - tid12) / 1000000
        # basic.show_number(resultat,60)
        serial.write_string("𝐃𝐢𝐭𝐭 𝐑𝐞𝐬𝐮𝐥𝐭𝐚𝐭:")
        serial.write_number(resultat)
        serial.write_line("")
    if input.logo_is_pressed():
        basic.show_number(Forsøk)
        Forsøk += 1
        serial.write_string("𝐅𝐨𝐫𝐬ø𝐤:")
        serial.write_number(Forsøk)
        serial.write_line("")
        basic.show_number(Juksemodus)
        Juksemodus = 5000
        serial.write_string("𝐃𝐢𝐭𝐭 𝐑𝐞𝐬𝐮𝐥𝐭𝐚𝐭:")
        serial.write_number(Juksemodus)
        serial.write_line("")
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
basic.forever(on_forever)
