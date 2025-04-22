from calendar import TextCalendar
monday_ca1 = TextCalendar()
sunday_ca1 = TextCalendar(6)

monday_ca1.prmonth(2023, 6)
sunday_ca1.prmonth(2023, 6)

m_days = monday_ca1.monthdatescalendar(2023, 6)
s_days = sunday_ca1.monthdatescalendar(2023, 6)

print("\nПервый день первой недели месяца:")

print(m_days[0][0], "- если с понедельника")
print(s_days[0][0], "- если с воскресенья")