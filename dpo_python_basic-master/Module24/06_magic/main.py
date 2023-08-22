class Water:
    title = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Shtorm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()

    def __str__(self):
        return Water.title


class Air:
    title = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Shtorm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()

    def __str__(self):
        return Air.title


class Fire:
    title = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()

    def __str__(self):
        return Fire.title


class Earth:
    title = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()

    def __str__(self):
        return Earth.title


class Shtorm:
    title = 'Шторм'

    def __str__(self):
        return Shtorm.title


class Steam:
    title = 'Пар'

    def __str__(self):
        return Steam.title


class Dirt:
    title = 'Грязь'

    def __str__(self):
        return Dirt.title


class Lightning:
    title = 'Молния'

    def __str__(self):
        return Lightning.title


class Dust:
    title = 'Пыль'

    def __str__(self):
        return Dust.title


class Lava:
    title = 'Лава'

    def __str__(self):
        return Lava.title


w = Water()
e = Earth()
mix = w + e

print(f'Смешиваем "{w.title}" c "{e.title}" и получаем "{mix.title}"')

air = Air()
fire = Fire()
print(f'{air} + {fire} = {air + fire}')

earth = Earth()
fire = Fire()
print(f'{earth} + {fire} = {earth + fire}')
