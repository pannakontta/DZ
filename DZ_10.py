class Pivo:
    def __init__(self, name: str, volume, IBU) -> None:
        self.name = name
        self.volume = volume
        self.IBU = IBU

    def run (self):
        if self.IBU < 10:
            print(f'{self.name} - Слабое пиво')
        elif 10 <= self.IBU < 30:
            print(f'{self.name} - Среднее пиво')
        else:
            print(f'{self.name} - Крепкое пиво')
    
    def presentation(self):
        print(f'{self.name} ({self.volume})')

    def estimation(self):
        if self.IBU < 10:
            print(f'{self.name} - Очень сладкое пиво')
        elif 10 <= self.IBU < 30:
            print(f'{self.name} - Отличное пиво')
        else:
            print(f'{self.name} - Очень горькое пиво')

pivo1 = Pivo('Жигулевское', 0.5, 4)
pivo2 = Pivo('Крушовице', 0.5, 29)
pivo3 = Pivo('Рижское', 0.45, 37)

# pivo1.run()
# pivo2.presentation()
# pivo3.estimation()


class Barbie:
    def __init__(self, look, mentality, temper) -> None:
        self.look = look
        self.mentality = mentality
        self.temper = temper
    
    def info(self):
        print(f'образ: {self.look}, ментальность: {self.mentality}, характер: {self.temper}')
    
    def change_look(self, new_look):
        self.look = new_look
        return f'Новый образ: {self.look}'
    
    def change_mentality(self, new_mentality):
        self.mentality = new_mentality
        return f'Новая ментальность: {self.mentality}'
    
    def change_temper(self, new_temper):
        self.temper = new_temper
        return f'Новый характер: {self.temper}'
    

class Kukla_Barbie(Barbie):
    def __init__(self, look, mentality, temper, dress_material, dress_color, hair_length, production) -> None:
        super().__init__(look, mentality, temper)
        self.dress_matirial = dress_material
        self.dress_color = dress_color
        self.hair_length = hair_length
        self.production = production

    def info(self):
        print(f'материал платья: {self.dress_matirial}, цвет платья: {self.dress_color}, длина волос: {self.hair_length}, тип производства: {self.production}')


kukla1 = Kukla_Barbie('деловой', 'трудоголик', 'флегматик', 'шелк', 'черный', 'короткая', 'ограниченное')

print(kukla1.change_look('вечерний'))
print(kukla1.info())