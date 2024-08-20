from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime
from kivy.graphics import Color, Rectangle
import random

class ClockApp(App):
    def build(self):
        # إعداد الواجهة الرئيسية كـ FloatLayout
        self.layout = FloatLayout()

        with self.layout.canvas.before:
            # تعيين لون الخلفية الأسود الداكن
            Color(0, 0, 0, 1)  # لون خلفية أسود داكن
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
            self.layout.bind(size=self._update_rect, pos=self._update_rect)

        # إضافة اسم التطبيق في الأعلى
        self.title_label = Label(
            text='\n\nMonter\n{mahamat tahir}',
            font_size='24sp',
            size_hint_y=None,
            height=50,
            color=(1, 1, 1, 1),  # لون النص أبيض
            bold=True,
            halign='center',
            valign='middle',
            pos_hint={'center_x': 0.5, 'top': 1}
        )

        # إضافة التسمية لعرض الوقت
        self.time_label = Label(
            font_size='48sp',
            halign='center',
            valign='middle',
            color=(1, 1, 1, 1),  # لون النص أبيض
            bold=True,
            size_hint=(None, None),
            size=(200, 100),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}  # وضع الوقت في المنتصف
        )

        # إضافة التسمية لعرض التاريخ
        self.date_label = Label(
            font_size='24sp',
            halign='center',
            valign='middle',
            color=(1, 1, 1, 1),  # لون النص أبيض
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}  # وضع التاريخ أسفل الوقت
        )

        # إضافة العناصر إلى الواجهة
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.time_label)
        self.layout.add_widget(self.date_label)

        # تحديث الوقت والتاريخ كل ثانية
        Clock.schedule_interval(self.update_time_and_date, 1)
        self.layout.bind(on_touch_down=self.change_text_color)
        return self.layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def update_time_and_date(self, dt):
        now = datetime.now()
        self.time_label.text = now.strftime("%H:%M:%S")
        self.date_label.text = now.strftime("%Y-%m-%d")

    def change_text_color(self, instance, touch):
        if instance.collide_point(*touch.pos):
            # تغيير لون النص عند النقر
            self.time_label.color = [random.random() for _ in range(3)] + [1]
            self.date_label.color = [random.random() for _ in range(3)] + [1]

if __name__ == '__main__':
    ClockApp().run()
