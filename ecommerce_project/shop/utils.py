menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'Контакты', 'url_name': 'contacts'},
        {'title': 'Оплата и доставка', 'url_name': 'payment'},
        {'title': 'Зарегестрироваться', 'url_name': 'signup'},
        {'title': 'Войти', 'url_name': 'login'},
        {'title': 'Выйти', 'url_name': 'signout'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):

        context = kwargs

        user_menu = menu.copy()  # для главной страницы это условие реализовано отдельно в функции представления
        if self.request.user.is_authenticated:
            user_menu.pop(3)
            user_menu.pop(3)
        else:
            user_menu.pop(5)

        context['menu'] = user_menu

        return context
