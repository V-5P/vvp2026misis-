class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    def calculate(self):
        return round(self.weight / (self.height ** 2), 2)
    def category(self):
        bmi = self.calculate()
        if bmi < 18.5:
            return 'Недостаток веса'
        elif bmi < 25:
            return 'Норма'
        elif bmi < 30:
            return 'Избыточный вес'
        else:
            return 'Ожирение'
    def show(self):
        print(f'ИМТ: {self.calculate():.2f}')
        print(f'Категория: {self.category()}')
        
print(" === Калькулятор ИМТ === ")
w = float(input("Введите вес (кг): "))
h = float(input("Введите рост (м): "))
BMI = BMICalculator(w, h)
print()
BMI.show()

    
