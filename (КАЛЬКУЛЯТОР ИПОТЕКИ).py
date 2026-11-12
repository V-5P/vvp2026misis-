import sys
import math
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QCheckBox, QTextEdit, QMessageBox, QGroupBox)
from PyQt6.QtCore import Qt

class MortgageCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ипотечный калькулятор")
        self.setGeometry(100, 100, 600, 500)
        
        # --- ПУНКТ 10. Компоновщики (Layouts) ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # --- ПУНКТ 1. Главное окно (Заголовок) ---
        title_label = QLabel("Расчет ежемесячного платежа по ипотеке")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
        main_layout.addWidget(title_label)

        # --- ПУНКТ 2. Текстовые элементы (Подписи к полям) ---
        form_layout = QVBoxLayout()
        
        # Сумма кредита
        main_layout.addWidget(QLabel("Сумма кредита (руб):"))
        # --- ПУНКТ 3. Поле ввода ---
        self.sum_input = QLineEdit()
        self.sum_input.setPlaceholderText("Например: 5000000")
        main_layout.addWidget(self.sum_input)
        
        # Процентная ставка
        main_layout.addWidget(QLabel("Процентная ставка (% годовых):"))
        self.rate_input = QLineEdit()
        self.rate_input.setPlaceholderText("Например: 12.5")
        main_layout.addWidget(self.rate_input)
        
        # Срок
        main_layout.addWidget(QLabel("Срок кредита (лет):"))
        self.years_input = QLineEdit()
        self.years_input.setPlaceholderText("Например: 20")
        main_layout.addWidget(self.years_input)

        # --- ПУНКТ 5. Выбор применителей (Check Box) ---
        self.insurance_checkbox = QCheckBox("Добавить страховку (+1% к ставке)")
        main_layout.addWidget(self.insurance_checkbox)

        # --- ПУНКТ 4. Кнопки ---
        button_layout = QHBoxLayout()
        self.calc_button = QPushButton("Рассчитать")
        self.clear_button = QPushButton("Очистить")
        button_layout.addWidget(self.calc_button)
        button_layout.addWidget(self.clear_button)
        main_layout.addLayout(button_layout)

        # --- ПУНКТ 6. Вывод результатов (Поле для текста) ---
        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)
        self.result_output.setPlaceholderText("Здесь появятся результаты расчета...")
        self.result_output.setStyleSheet("background-color: #f0f0f0; font-family: monospace;")
        main_layout.addWidget(self.result_output)

        # --- ПУНКТ 7. Обработка событий (Привязка кнопок к функциям) ---
        self.calc_button.clicked.connect(self.calculate_mortgage)
        self.clear_button.clicked.connect(self.clear_fields)

    # --- ПУНКТ 8. Проверка данных ---
    def validate_inputs(self):
        try:
            sum_val = float(self.sum_input.text().replace(',', '.').replace(' ', ''))
            rate_val = float(self.rate_input.text().replace(',', '.'))
            years_val = float(self.years_input.text().replace(',', '.'))

            if sum_val <= 0 or rate_val <= 0 or years_val <= 0:
                raise ValueError("Все значения должны быть больше нуля.")
            return sum_val, rate_val, years_val
        except ValueError as e:
            # --- ПУНКТ 9. Диалоговое окно (Вывод ошибки) ---
            QMessageBox.critical(self, "Ошибка ввода", 
                                 f"Пожалуйста, введите корректные числа.\nДетали: {str(e)}")
            return None

    # --- ПУНКТ 7. Обработка событий (Логика расчета) ---
    def calculate_mortgage(self):
        inputs = self.validate_inputs()
        if not inputs:
            return

        principal, annual_rate, years = inputs
        
        # Учет страховки (Пункт 5)
        if self.insurance_checkbox.isChecked():
            annual_rate += 1.0

        # Математика ипотеки (Аннуитетный платеж)
        months = years * 12
        monthly_rate = annual_rate / 100 / 12
        
        try:
            monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
            total_payment = monthly_payment * months
            overpayment = total_payment - principal

            # Формирование отчета (Пункт 6)
            report = (
                f"--- РЕЗУЛЬТАТЫ РАСЧЕТА ---\n"
                f"Сумма кредита: {principal:,.2f} руб.\n"
                f"Ставка: {annual_rate:.2f}% годовых\n"
                f"Срок: {years} лет ({int(months)} мес.)\n"
                f"--------------------------\n"
                f"Ежемесячный платеж: {monthly_payment:,.2f} руб.\n"
                f"Общая сумма выплат: {total_payment:,.2f} руб.\n"
                f"Переплата по процентам: {overpayment:,.2f} руб."
            )
            self.result_output.setText(report)
            
        except ZeroDivisionError:
             QMessageBox.warning(self, "Ошибка", "Ставка не может быть равна 0 для данного расчета.")

    def clear_fields(self):
        self.sum_input.clear()
        self.rate_input.clear()
        self.years_input.clear()
        self.insurance_checkbox.setChecked(False)
        self.result_output.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MortgageCalculator()
    window.show()
    sys.exit(app.exec())
   

        


