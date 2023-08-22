def main():

    violator_songs = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83]
    ]
    dur = 0.0
    count = int(input('Сколько песен выбрать? '))
    for i in range(count):
        song = input('Название ' + str(i + 1) + ' песни: ')
        for i_song in violator_songs:
            if i_song[0] == song:
                dur += i_song[1]

    print(f'Общее время звучания песен: {round(dur, 2)} минут')

main()
